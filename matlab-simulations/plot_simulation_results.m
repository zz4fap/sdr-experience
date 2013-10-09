clear all;clc

snr_vector = zeros(1,length(-30:1:30));
pd = zeros(1,length(-30:1:30));
counter = 0;
for i=-30:1:30
    
    fileName= sprintf('pd_vs_snr_%d.mat',i);
    load(fileName);
    
    counter = counter + 1;
    snr_vector(counter) = snr;
    pd(counter) = detection_rate;
end

stem(snr_vector,pd)