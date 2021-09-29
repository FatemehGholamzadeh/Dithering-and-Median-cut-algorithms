% Clear the command window.
clc;    
% Close all figures (except those of imtool.)
close all;  
% Erase all existing variables.
clear;  
% Make sure the workspace panel is showing.
workspace;

% read image file
X = imread('1.jpg');

%obtain gray image
Y = rgb2gray(X);

%quantize gray image to 8 levels
quantizedImage = uint8(mat2gray(Y) * (255));

%show 8 bit grey level image
imshow(quantizedImage, []);

%save 8 bit grey level image
imwrite(quantizedImage, '8_bit_grey_level.jpg');

