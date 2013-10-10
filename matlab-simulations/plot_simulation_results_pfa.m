clear all;clc

dbw_vector = zeros(1,length(-30:1:30));
pfa = zeros(1,length(-30:1:30));
counter = 0;
for i=-30:1:30
    
    fileName= sprintf('pfa_vs_dbw_%dv2.mat',i);
    load(fileName);
    
    counter = counter + 1;
    dbw_vector(counter) = dbW;
    pfa(counter) = false_alarm_rate;
end

plot(dbw_vector,pfa)