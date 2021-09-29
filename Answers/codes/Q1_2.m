% Clear the command window.
clc;    
% Close all figures (except those of imtool.)
close all;  
% Erase all existing variables.
clear;  
% Make sure the workspace panel is showing.
workspace;

% read image file
Irgb = imread('1.jpg');

%defining threshold
threshold = 128;

%obtain gray image
Igray = rgb2gray(Irgb);

Ibw = Igray>threshold;

%show binary image
imshow(Ibw);

%save binary image
imwrite(Ibw, 'binary.jpg');

