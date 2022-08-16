import cv2
import numpy as np
import colorsys
import sys
import os

def ave_color_extract():
    src_img = cv2.imread(plantdir)
    average_color_row = np.average(src_img, axis=0)
    average_color = np.average(average_color_row, axis=0)
    print(average_color)

    d_img = np.ones((312,312,3), dtype=np.uint8)
    d_img[:,:] = average_color

    cv2.imshow('Source image',src_img)
    cv2.imshow('Average Color',d_img)
    cv2.waitKey(0)
    
def color_distance(rgb1, rgb2):
    rm = 0.5 * (rgb1[0] + rgb2[0])
    rd = ((2 + rm) * (rgb1[0] - rgb2[0])) ** 2
    gd = (4 * (rgb1[1] - rgb2[1])) ** 2
    bd = ((3 - rm) * (rgb1[2] - rgb2[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    print (f"Distance is: {ans}")

plantdir = input("Insert Plant Directory: ")
print(plantdir)
ave_color_extract()

rgb1 = np.array([75,102,35])
rgb2 = np.array([99,120,92])
color_distance(rgb1,rgb2)
