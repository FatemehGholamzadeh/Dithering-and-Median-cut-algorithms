
from argparse import ArgumentParser
from math import floor
from PIL import Image
import cv2
import os


class Dither():
    def __init__(self, path, output=None):
        # self.path = self.get_path(path)
        self.func1 = self.dither_by_error(path)
        self.func2=self.floyd_steinberg_dither_without_error(path)
        self.output=output
    def find_closest_palette_color(self, value ):

        return  floor(value/64)*64

    def dither_by_error(self, image_file):


        newPic = cv2.imread(image_file,)


        XL, YL ,channels= newPic.shape

        for y in range(1, YL):
            for x in range(1, XL):
                red_oldpixel, green_oldpixel, blue_oldpixel = newPic[x, y]

                newRed = self.find_closest_palette_color(red_oldpixel)
                newGreen = self.find_closest_palette_color(green_oldpixel)
                newBlue = self.find_closest_palette_color(blue_oldpixel)

                newPic[x, y] = newRed, newGreen, newBlue

                red_error = red_oldpixel - newRed
                blue_error = blue_oldpixel - newBlue
                green_error = green_oldpixel - newGreen

                if x < XL - 1:
                    red =newPic[x+1, y][0] + round(red_error * 7/16)
                    green =newPic[x+1, y][1] + round(green_error * 7/16)
                    blue =newPic[x+1, y][2] + round(blue_error * 7/16)

                    newPic[x+1, y] = (red, green, blue)

                if x > 1 and y < YL - 1:
                    red =newPic[x-1, y+1][0] + round(red_error * 3/16)
                    green =newPic[x-1, y+1][1] + round(green_error * 3/16)
                    blue =newPic[x-1, y+1][2] + round(blue_error * 3/16)

                    newPic[x-1, y+1] = (red, green, blue)

                if y < YL - 1:
                    red =newPic[x, y+1][0] + round(red_error * 5/16)
                    green =newPic[x, y+1][1] + round(green_error * 5/16)
                    blue =newPic[x, y+1][2] + round(blue_error * 5/16)

                    newPic[x, y+1] = (red, green, blue)

                if x < XL - 1 and y < YL - 1:
                    red =newPic[x+1, y+1][0] + round(red_error * 1/16)
                    green =newPic[x+1, y+1][1] + round(green_error * 1/16)
                    blue =newPic[x+1, y+1][2] + round(blue_error * 1/16)

                    newPic[x+1, y+1] = (red, green, blue)
        cv2.imwrite("image_by_error.jpg",newPic)
        cv2.imshow("image by error computation",newPic)
        # cv2.waitKey(10000)

    def floyd_steinberg_dither_without_error(self, image_file):

        newPic = cv2.imread(image_file)
        XL, YL, channels = newPic.shape

        for y in range(1, YL):
            for x in range(1, XL):
                red_oldpixel, green_oldpixel, blue_oldpixel =newPic[x, y]
                newRed = self.find_closest_palette_color(red_oldpixel)
                newGreen = self.find_closest_palette_color(green_oldpixel)
                newBlue = self.find_closest_palette_color(blue_oldpixel)
                newPic[x,y]=(newRed,newGreen,newBlue)
        # if self.output:
        #     newPic.save(self.output)
        # else:
        cv2.imwrite("image_without_error.jpg", newPic)
        cv2.imshow("image without error", newPic)



def main():
    path=""
    Dither("2.jpg")
    cv2.waitKey(100000)
main()