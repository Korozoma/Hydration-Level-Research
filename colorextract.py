import cv2
import numpy as np
import colorsys
import sys
import os

ave_color = ''
global r, g, b

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
    ave_color = average_color

    (b, g, r) = ave_color
    hyd = np.array([r,g,b])
    inp = np.array([118,118,34])
    rm = 0.5 * (hyd[0] + inp[0])
    rd = ((2 + rm) * (hyd[0] - inp[0])) ** 2
    gd = (4 * (hyd[1] - inp[1])) ** 2
    bd = ((3 - rm) * (hyd[2] - inp[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    print (f"Distance is: {ans}")


plantdir = input("File Directory: ")
