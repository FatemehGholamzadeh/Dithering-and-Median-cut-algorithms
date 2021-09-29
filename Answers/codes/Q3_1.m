% Clear the command window.
clc;    
% Close all figures (except those of imtool.)
close all;  
% Erase all existing variables.
clear;  
% Make sure the workspace panel is showing.
workspace;

% read image file
image = imread('2.jpg');

%Split into RGB Channels
Red = image(:,:,1);
Green = image(:,:,2);
Blue = image(:,:,3);
%Get histValues for each channel
[yRed, x] = imhist(Red);
[yGreen, x] = imhist(Green);
[yBlue, x] = imhist(Blue);
%Plot them together in one plot
plot(x, yRed, 'Red', x, yGreen, 'Green', x, yBlue, 'Blue');
    
    