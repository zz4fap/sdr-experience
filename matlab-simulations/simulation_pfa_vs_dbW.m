clear all;clc

plot_figures = false;

%% ----------------------------- FM Signal Generation ---------------------
L = 8000;
fs = 2e6; % Sampling frequency.
BWfm = 200e3; % in Hz

fc = 2000*(fs/L); % Carrier Frequency
fm = 60*(fs/L); % Maximum allowed frequency for commercial FM.
delta_f = 75e3; % Maximum allowed frequency deviation for commercial FM.

Ac = 1; % Amplitude of the modulated signal.

n = 0:1/fs:(L-1)*(1/fs);

m_fm = delta_f/fm;
e_fm  = Ac*sin(2*pi*fc*n - m_fm*cos(2*pi*fm*n));

%% ----------------------------- Compliance filter ------------------------
b = compliance_filter;

% Filter signal so that it has a bandwidth of 180 KHz and we can use the
% 20KHz band guard to estimate Zref instead of using the algorithm.
e_fm_filtered = filter(b,1,e_fm);

%% ----------------------------- Hilbert Transform ------------------------

% After the hilbert transform the spectral content of the fm signal lies in
% the positive Nyquist interval and thus avoiding the detection of the
% negative interval.

e_fm_hil = hilbert(e_fm);

%% --------------------------- Monte Carlo Trials -------------------------
numTrials = 10000;

tx_noise_only = true;
complex_noise = true;
calculate_pfa = true; % False: Pd, True: Pfa

SNR = 0; % in dB
noisePower = 0; % in dBW
Pfd = 0.001;
numSamplesSegment = 16;
Tcme = 6.9078; % for 16 samples
Pfa = 0.01/100; % 0.01%
NFFT = 2048;
BWfm_useful = 180e3;

numOfSegments = NFFT/numSamplesSegment; % Number of energy segments.
Z = zeros(1,numOfSegments);
numOfSegsToCheck = floor(BWfm_useful/(numSamplesSegment*(fs/NFFT))); % Number of segments to check around the given primary user position.
band_location = floor(fc/(numSamplesSegment*(fs/NFFT))); % Location of center frequency of the primary user.

trials_counter = 0;
false_alarm_counter = 0;
correct_rejection_counter = 0;
correct_detection_counter = 0;
false_rejection_counter = 0;
counter = 0;
pfa_vs_dbW = zeros(2,length(-30:1:30));

for dbW=-30:1:30
    
    for trial = 1:1:numTrials
        
        %% ----------------------------- AWGN Channel -------------------------
        if(tx_noise_only)
            if(complex_noise)
                tx_signal = wgn(1,L,dbW,'complex');
            else
                tx_signal = wgn(1,L,dbW);
            end
        else
            tx_signal = awgn(e_fm_hil,SNR,'measured');
        end
        
        %% ---------------------- Dectection Algorithm ------------------------
        % Transform received signal into Frequency Domain.
        rx_signal_fd = fft(tx_signal,NFFT);
        
        % Segment spectrum in energy subbands.
        for seg=1:1:numOfSegments
            Z(seg) = sum(abs(rx_signal_fd((numSamplesSegment*(seg-1)+1):numSamplesSegment*seg)).^2);
        end
        Z_orig = Z;
        
        % This is the implemenatation of the algorithm proposed in [1]
        % Sort Segmented Z vector in increasing order of energy.
        for i=1:1:length(Z)
            for k=1:1:length(Z)-1
                if(Z(k)>Z(k+1))
                    temp = Z(k+1);
                    Z(k+1) = Z(k);
                    Z(k) = temp;
                end
            end
        end
        
        % Algorithm used to discard samples. Indeed, it is used to find a
        % speration between noisy samples and signal+noise samples.
        if(numOfSegments < 20)
            I_initial = 3;
        else
            I_initial = 20;
        end
        
        for I=I_initial:1:numOfSegments-1
            limiar = Tcme/I;
            if(Z(I+1) > limiar*sum(Z(1:I)))
                break;
            end
        end
        
        % Output of the disposal module. It's used as a noise reference.
        Zref = sum(Z(1:I));
        
        % Calculate the scale factor.
        alpha = finv(1-Pfa,2*numSamplesSegment,(2*numSamplesSegment*I))/I;
        
        %% --------------------- Calculate Pfa and Pd -------------------------
        if(calculate_pfa)
            for j=1:1:numOfSegments
                trials_counter = trials_counter + 1;
                ratio = Z_orig(j)/Zref;
                if(ratio > alpha)
                    false_alarm_counter = false_alarm_counter + 1;
                else
                    correct_rejection_counter = correct_rejection_counter + 1;
                end
            end
            false_alarm_rate = false_alarm_counter/trials_counter;
            correct_rejection_rate = correct_rejection_counter/trials_counter;
        else
            start_seg = band_location-floor(numOfSegsToCheck/2);
            end_seg = band_location+floor(numOfSegsToCheck/2);
            for j=start_seg:1:end_seg
                trials_counter = trials_counter + 1;
                ratio = Z_orig(j)/Zref;
                if(ratio > alpha)
                    correct_detection_counter = correct_detection_counter + 1;
                else
                    false_rejection_counter = false_rejection_counter + 1;
                end
                detection_rate = correct_detection_counter/trials_counter;
                false_rejection_rate = false_rejection_counter/trials_counter;
            end
        end
    end
    
    filename = sprintf('pfa_vs_dbw_%d.mat',dbW);
    save(filename, 'dbW','false_alarm_rate','correct_rejection_rate');
    
    counter = counter + 1;
    pfa_vs_dbW(:,counter) = [dbW;false_alarm_rate];
end

if(calculate_pfa)
    fprintf(1,'Estimated Pfa: %f\n',false_alarm_rate);
else
    fprintf(1,'Estimated Pd: %f\n',detection_rate);
end

%% -------------------------------- Figures -------------------------------
if(plot_figures)
    f = fs/2*linspace(0,1,L/2+1);
    
    % Plot single-sided amplitude spectrum.
    Y = fft(e_fm,L)/L;
    figure(1)
    stem(f,(2*abs(Y(1:L/2+1))))
    %plot(f,10*log10(2*abs(Y(1:L/2+1))))
    title('Single-Sided Amplitude Spectrum of y(t)')
    xlabel('Frequency (Hz)')
    ylabel('|Y(f)|')
    grid on
    
    % Plot single-sided amplitude spectrum.
    Y = fft(tx_signal,L)/L;
    figure(2)
    stem(f,(2*abs(Y(1:L/2+1))))
    %plot(f,10*log10(2*abs(Y(1:L/2+1))))
    title('Single-Sided Amplitude Spectrum of y(t)')
    xlabel('Frequency (Hz)')
    ylabel('|Y(f)|')
    grid on
    
    % Plot single-sided amplitude spectrum.
    Y = fft(e_fm_filtered,L)/L;
    figure(3)
    stem(f,(2*abs(Y(1:L/2+1))))
    %plot(f,10*log10(2*abs(Y(1:L/2+1))))
    title('Single-Sided Amplitude Spectrum of y(t)')
    xlabel('Frequency (Hz)')
    ylabel('|Y(f)|')
    grid on
    
    Y = fft(e_fm_hil,L)/L;
    figure(4)
    stem(f,(2*abs(Y(1:L/2+1))))
    %plot(f,10*log10(2*abs(Y(1:L/2+1))))
    title('Single-Sided Amplitude Spectrum of y(t)')
    xlabel('Frequency (Hz)')
    ylabel('|Y(f)|')
    grid on
end

%% ---------------------------- References --------------------------------

% [1] Jane J. Lehtomake, Markku Juntti, Harri Saarnisaari, “CFAR Strategies for Channelized
%     Radiometer”, IEEE Signal Processing Letters, Vol. 12, No. 1, January, 2005.