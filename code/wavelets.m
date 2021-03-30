% Wavelet Coherence script
% Sandy Herho <herho@umd.edu>
% 2021/03/31
% from Grinsted et al. (2004)


clear all; close all; clc

%% Set Path
addpath('wavelet-coherence-master');

%% Read data
seriesname = {'MEI' 'SPI-12'};
d1 = readtable('../data/mei.csv');
d2 = readtable('../data/spi12.csv');
d1 = normalize(detrend(d1.MEI));
d2 = normalize(detrend(d2.SPI12));

%% Change series to pdf
d1 = boxpdf(d1);
d2 = boxpdf(d2);

%% Wavelet Coherence
figure('color',[1 1 1])
wtc(d1,d2)
colormap('hot')
xlabel('time')
ylabel('Period (months)')
set(gca, 'XTickLabel', ...
    {'1929', '1937', '1946', ...
    '1954', '1962', '1971', ...
    '1979', '1987', '1996', ...
    '2004', '2012'})