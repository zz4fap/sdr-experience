clear all;clc

NFFTv = [512, 1024, 2048, 4096];
pd = zeros(4,length(-30:0.1:30));
snr_vector = zeros(4,length(-30:1:30));

for i=1:1:4
    counter = 0;
    fft = NFFTv(i);
    for snr=-30:0.1:30
        if(fft==2048)
            filename = sprintf('pd_vs_snr_%dv2.mat',snr);
        else
            filename = sprintf('fft_%d_pd_vs_snr_%dv2.mat',fft,snr);
        end
        load(filename);
        
        counter = counter + 1;
        snr_vector(i,counter) = snr;
        pd(i,counter) = detection_rate;
    end
end

hold on
plot(snr_vector(1,:),pd(1,:),'r') % FFT: 512
plot(snr_vector(2,:),pd(2,:),'g') % FFT: 1024
plot(snr_vector(3,:),pd(3,:))     % FFT: 2048
plot(snr_vector(4,:),pd(4,:),'y') % FFT: 4096
legend('512','1024','2048','4096')
title('SNR vs Achieved Pfa')
xlabel('SNR [dB]');
ylabel('Achieved Pfa');
grid on
