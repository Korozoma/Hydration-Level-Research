import cv2
import numpy as np
import colorsys
import sys
import os

ave_color = ''
global r, g, b

def ave_color_extractbroccoli():
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
    inp1 = np.array([r,g,b]) #inserted plant rgb code
    dehy = np.array([122,135,123]) #dehydrated plant rgb code
    rm = 0.5 * (inp1[0] + dehy[0])
    rd = ((2 + rm) * (inp1[0] - dehy[0])) ** 2
    gd = (4 * (inp1[1] - dehy[1])) ** 2
    bd = ((3 - rm) * (inp1[2] - dehy[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    
    hydration_level = (ans/6835) * 100 #distance hydrate & dehydrate
    round_off = round(hydration_level, 2)
    print(round_off, "% Hydration Level")
    
    range_1 = range(0, 25)
    range_2 = range(26, 50)
    range_3 = range(51, 75)
    range_4 = range(76, 100)
    if int(hydration_level) in range_1:
        print("Your Plant is Dehydrated")
    elif int(hydration_level) in range_2:
        print("Your Plant is Slightly Dehydrated")
    elif int(hydration_level) in range_3:
        print("Your Plant is Slightly Hydrated")
    elif int(hydration_level) in range_4:
        print("Your Plant is Well-Hydrated")
    else:
        print("Invalid Percent")
        
def ave_color_extractcabbage():
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
    inp1 = np.array([r,g,b]) #inserted plant rgb code
    dehy = np.array([99,120,92]) #dehydrated plant rgb code
    rm = 0.5 * (inp1[0] + dehy[0])
    rd = ((2 + rm) * (inp1[0] - dehy[0])) ** 2
    gd = (4 * (inp1[1] - dehy[1])) ** 2
    bd = ((3 - rm) * (inp1[2] - dehy[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    
    hydration_level = (ans/5243) * 100
    round_off = round(hydration_level, 2)
    print(round_off, "% Hydration Level")
    
    range_1 = range(0, 25)
    range_2 = range(26, 50)
    range_3 = range(51, 75)
    range_4 = range(76, 100)
    if int(hydration_level) in range_1:
        print("Your Plant is Dehydrated")
    elif int(hydration_level) in range_2:
        print("Your Plant is Slightly Dehydrated")
    elif int(hydration_level) in range_3:
        print("Your Plant is Slightly Hydrated")
    elif int(hydration_level) in range_4:
        print("Your Plant is Well-Hydrated")
    else:
        print("Invalid Percent")
        
def ave_color_extractceleryleaf():
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
    inp1 = np.array([r,g,b]) #inserted plant rgb code
    dehy = np.array([157,155,33]) #dehydrated plant rgb code
    rm = 0.5 * (inp1[0] + dehy[0])
    rd = ((2 + rm) * (inp1[0] - dehy[0])) ** 2
    gd = (4 * (inp1[1] - dehy[1])) ** 2
    bd = ((3 - rm) * (inp1[2] - dehy[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    
    hydration_level = (ans/8036) * 100
    round_off = round(hydration_level, 2)
    print(round_off, "% Hydration Level")
    
    range_1 = range(0, 25)
    range_2 = range(26, 50)
    range_3 = range(51, 75)
    range_4 = range(76, 100)
    if int(hydration_level) in range_1:
        print("Your Plant is Dehydrated")
    elif int(hydration_level) in range_2:
        print("Your Plant is Slightly Dehydrated")
    elif int(hydration_level) in range_3:
        print("Your Plant is Slightly Hydrated")
    elif int(hydration_level) in range_4:
        print("Your Plant is Well-Hydrated")
    else:
        print("Invalid Percent")
        
def ave_color_extractcelerystem():
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
    inp1 = np.array([r,g,b]) #inserted plant rgb code
    dehy = np.array([149,137,70]) #dehydrated plant rgb code
    rm = 0.5 * (inp1[0] + dehy[0])
    rd = ((2 + rm) * (inp1[0] - dehy[0])) ** 2
    gd = (4 * (inp1[1] - dehy[1])) ** 2
    bd = ((3 - rm) * (inp1[2] - dehy[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    
    hydration_level = (ans/7123) * 100 #distance hydrate & dehydrate
    round_off = round(hydration_level, 2)
    print(round_off, "% Hydration Level")
    
    range_1 = range(0, 25)
    range_2 = range(26, 50)
    range_3 = range(51, 75)
    range_4 = range(76, 100)
    if int(hydration_level) in range_1:
        print("Your Plant is Dehydrated")
    elif int(hydration_level) in range_2:
        print("Your Plant is Slightly Dehydrated")
    elif int(hydration_level) in range_3:
        print("Your Plant is Slightly Hydrated")
    elif int(hydration_level) in range_4:
        print("Your Plant is Well-Hydrated")
    else:
        print("Invalid Percent")
        
def ave_color_extractkangkongleaf():
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
    inp1 = np.array([r,g,b]) #inserted plant rgb code
    dehy = np.array([62,111,89]) #dehydrated plant rgb code
    rm = 0.5 * (inp1[0] + dehy[0])
    rd = ((2 + rm) * (inp1[0] - dehy[0])) ** 2
    gd = (4 * (inp1[1] - dehy[1])) ** 2
    bd = ((3 - rm) * (inp1[2] - dehy[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    
    hydration_level = (ans/4212) * 100 #distance hydrate & dehydrate
    round_off = round(hydration_level, 2)
    print(round_off, "% Hydration Level")
    
    range_1 = range(0, 25)
    range_2 = range(26, 50)
    range_3 = range(51, 75)
    range_4 = range(76, 105)
    if int(hydration_level) in range_1:
        print("Your Plant is Dehydrated")
    elif int(hydration_level) in range_2:
        print("Your Plant is Slightly Dehydrated")
    elif int(hydration_level) in range_3:
        print("Your Plant is Slightly Hydrated")
    elif int(hydration_level) in range_4:
        print("Your Plant is Well-Hydrated")
    else:
        print("Invalid Percent")
         
def ave_color_extractkangkongstem():
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
    inp1 = np.array([r,g,b]) #inserted plant rgb code
    dehy = np.array([85,99,39]) #dehydrated plant rgb code
    rm = 0.5 * (inp1[0] + dehy[0])
    rd = ((2 + rm) * (inp1[0] - dehy[0])) ** 2
    gd = (4 * (inp1[1] - dehy[1])) ** 2
    bd = ((3 - rm) * (inp1[2] - dehy[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    
    hydration_level = (ans/4878) * 100 #distance hydrate & dehydrate
    round_off = round(hydration_level, 2)
    print(round_off, "% Hydration Level")
    
    range_1 = range(0, 25)
    range_2 = range(26, 50)
    range_3 = range(51, 75)
    range_4 = range(76, 105)
    if int(hydration_level) in range_1:
        print("Your Plant is Dehydrated")
    elif int(hydration_level) in range_2:
        print("Your Plant is Slightly Dehydrated")
    elif int(hydration_level) in range_3:
        print("Your Plant is Slightly Hydrated")
    elif int(hydration_level) in range_4:
        print("Your Plant is Well-Hydrated")
    else:
        print("Invalid Percent")
        
def ave_color_extractmint():
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
    inp1 = np.array([r,g,b]) #inserted plant rgb code
    dehy = np.array([133,148,71]) #dehydrated plant rgb code
    rm = 0.5 * (inp1[0] + dehy[0])
    rd = ((2 + rm) * (inp1[0] - dehy[0])) ** 2
    gd = (4 * (inp1[1] - dehy[1])) ** 2
    bd = ((3 - rm) * (inp1[2] - dehy[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    
    hydration_level = (ans/3423) * 100 #distance hydrate & dehydrate
    round_off = round(hydration_level, 2)
    print(round_off, "% Hydration Level")
    
    range_1 = range(0, 25)
    range_2 = range(26, 50)
    range_3 = range(51, 75)
    range_4 = range(76, 105)
    if int(hydration_level) in range_1:
        print("Your Plant is Dehydrated")
    elif int(hydration_level) in range_2:
        print("Your Plant is Slightly Dehydrated")
    elif int(hydration_level) in range_3:
        print("Your Plant is Slightly Hydrated")
    elif int(hydration_level) in range_4:
        print("Your Plant is Well-Hydrated")
    else:
        print("Invalid Percent")
       
def ave_color_extractmonstera():
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
    inp1 = np.array([r,g,b]) #inserted plant rgb code
    dehy = np.array([139,126,31]) #dehydrated plant rgb code
    rm = 0.5 * (inp1[0] + dehy[0])
    rd = ((2 + rm) * (inp1[0] - dehy[0])) ** 2
    gd = (4 * (inp1[1] - dehy[1])) ** 2
    bd = ((3 - rm) * (inp1[2] - dehy[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    
    hydration_level = (ans/7957) * 100 #distance hydrate & dehydrate
    round_off = round(hydration_level, 2)
    print(round_off, "% Hydration Level")
    
    range_1 = range(0, 25)
    range_2 = range(26, 50)
    range_3 = range(51, 75)
    range_4 = range(76, 105)
    if int(hydration_level) in range_1:
        print("Your Plant is Dehydrated")
    elif int(hydration_level) in range_2:
        print("Your Plant is Slightly Dehydrated")
    elif int(hydration_level) in range_3:
        print("Your Plant is Slightly Hydrated")
    elif int(hydration_level) in range_4:
        print("Your Plant is Well-Hydrated")
    else:
        print("Invalid Percent")
       
def ave_color_extractparsley():
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
    inp1 = np.array([r,g,b]) #inserted plant rgb code
    dehy = np.array([136,181,47]) #dehydrated plant rgb code
    rm = 0.5 * (inp1[0] + dehy[0])
    rd = ((2 + rm) * (inp1[0] - dehy[0])) ** 2
    gd = (4 * (inp1[1] - dehy[1])) ** 2
    bd = ((3 - rm) * (inp1[2] - dehy[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    
    hydration_level = (ans/4974) * 100 #distance hydrate & dehydrate
    round_off = round(hydration_level, 2)
    print(round_off, "% Hydration Level")
    
    range_1 = range(0, 25)
    range_2 = range(26, 50)
    range_3 = range(51, 75)
    range_4 = range(76, 130)
    if int(hydration_level) in range_1:
        print("Your Plant is Dehydrated")
    elif int(hydration_level) in range_2:
        print("Your Plant is Slightly Dehydrated")
    elif int(hydration_level) in range_3:
        print("Your Plant is Slightly Hydrated")
    elif int(hydration_level) in range_4:
        print("Your Plant is Well-Hydrated")
    else:
        print("Invalid Percent")
       
def ave_color_extractspronion():
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
    inp1 = np.array([r,g,b]) #inserted plant rgb code
    dehy = np.array([77,88,42]) #dehydrated plant rgb code
    rm = 0.5 * (inp1[0] + dehy[0])
    rd = ((2 + rm) * (inp1[0] - dehy[0])) ** 2
    gd = (4 * (inp1[1] - dehy[1])) ** 2
    bd = ((3 - rm) * (inp1[2] - dehy[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    
    hydration_level = (ans/599) * 100 #distance hydrate & dehydrate
    round_off = round(hydration_level, 2)
    print(round_off, "% Hydration Level")
    
    range_1 = range(0, 25)
    range_2 = range(26, 50)
    range_3 = range(51, 75)
    range_4 = range(76, 130)
    if int(hydration_level) in range_1:
        print("Your Plant is Dehydrated")
    elif int(hydration_level) in range_2:
        print("Your Plant is Slightly Dehydrated")
    elif int(hydration_level) in range_3:
        print("Your Plant is Slightly Hydrated")
    elif int(hydration_level) in range_4:
        print("Your Plant is Well-Hydrated")
    else:
        print("Invalid Percent")
       
def ave_color_extractspinachleaf():
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
    inp1 = np.array([r,g,b]) #inserted plant rgb code
    dehy = np.array([83,108,54]) #dehydrated plant rgb code
    rm = 0.5 * (inp1[0] + dehy[0])
    rd = ((2 + rm) * (inp1[0] - dehy[0])) ** 2
    gd = (4 * (inp1[1] - dehy[1])) ** 2
    bd = ((3 - rm) * (inp1[2] - dehy[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    
    hydration_level = (ans/2002) * 100
    round_off = round(hydration_level, 2)
    print(round_off, "% Hydration Level")
    
    range_1 = range(0, 25)
    range_2 = range(26, 50)
    range_3 = range(51, 75)
    range_4 = range(76, 100)
    if int(hydration_level) in range_1:
        print("Your Plant is Dehydrated")
    elif int(hydration_level) in range_2:
        print("Your Plant is Slightly Dehydrated")
    elif int(hydration_level) in range_3:
        print("Your Plant is Slightly Hydrated")
    elif int(hydration_level) in range_4:
        print("Your Plant is Well-Hydrated")
    else:
        print("Invalid Percent")
        
def ave_color_extractspinachstem():
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
    inp1 = np.array([r,g,b]) #inserted plant rgb code
    dehy = np.array([133,153,95]) #dehydrated plant rgb code
    rm = 0.5 * (inp1[0] + dehy[0])
    rd = ((2 + rm) * (inp1[0] - dehy[0])) ** 2
    gd = (4 * (inp1[1] - dehy[1])) ** 2
    bd = ((3 - rm) * (inp1[2] - dehy[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    
    hydration_level = (ans/10351) * 100
    round_off = round(hydration_level, 2)
    print(round_off, "% Hydration Level")
    
    range_1 = range(0, 25)
    range_2 = range(26, 50)
    range_3 = range(51, 75)
    range_4 = range(76, 100)
    if int(hydration_level) in range_1:
        print("Your Plant is Dehydrated")
    elif int(hydration_level) in range_2:
        print("Your Plant is Slightly Dehydrated")
    elif int(hydration_level) in range_3:
        print("Your Plant is Slightly Hydrated")
    elif int(hydration_level) in range_4:
        print("Your Plant is Well-Hydrated")
    else:
        print("Invalid Percent")
        
def ave_color_extractrubbertree():
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
    inp1 = np.array([r,g,b]) #inserted plant rgb code
    dehy = np.array([108,65,64]) #dehydrated plant rgb code
    rm = 0.5 * (inp1[0] + dehy[0])
    rd = ((2 + rm) * (inp1[0] - dehy[0])) ** 2
    gd = (4 * (inp1[1] - dehy[1])) ** 2
    bd = ((3 - rm) * (inp1[2] - dehy[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    
    hydration_level = (ans/3616) * 100 #distance hydrate & dehydrate
    round_off = round(hydration_level, 2)
    print(round_off, "% Hydration Level")
    
    range_1 = range(0, 25)
    range_2 = range(26, 50)
    range_3 = range(51, 75)
    range_4 = range(76, 130)
    if int(hydration_level) in range_1:
        print("Your Plant is Dehydrated")
    elif int(hydration_level) in range_2:
        print("Your Plant is Slightly Dehydrated")
    elif int(hydration_level) in range_3:
        print("Your Plant is Slightly Hydrated")
    elif int(hydration_level) in range_4:
        print("Your Plant is Well-Hydrated")
    else:
        print("Invalid Percent")
       
def ave_color_extracttest():
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
    inp1 = np.array([r,g,b]) #inserted plant rgb code
    dehy = np.array([134,165,133]) #dehydrated plant rgb code
    rm = 0.5 * (inp1[0] + dehy[0])
    rd = ((2 + rm) * (inp1[0] - dehy[0])) ** 2
    gd = (4 * (inp1[1] - dehy[1])) ** 2
    bd = ((3 - rm) * (inp1[2] - dehy[2])) ** 2
    ans = (rd + gd + bd) ** 0.5
    print (f"Distance is: {ans}")
    
    hydration_level = (ans/11138) * 100
    round_off = round(hydration_level, 2)
    print(round_off, "% Hydration Level")
    
    range_1 = range(0, 25)
    range_2 = range(26, 50)
    range_3 = range(51, 75)
    range_4 = range(76, 100)
    if int(hydration_level) in range_1:
        print("Your Plant is Dehydrated")
    elif int(hydration_level) in range_2:
        print("Your Plant is Slightly Dehydrated")
    elif int(hydration_level) in range_3:
        print("Your Plant is Slightly Hydrated")
    elif int(hydration_level) in range_4:
        print("Your Plant is Well-Hydrated")
    else:
        print("Invalid Percent")
        
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
    
    hydration_level = (2687/ans) * 100
    print(hydration_level, "%")

plantdir = input("File Directory: ")
