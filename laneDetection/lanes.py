import cv2
import numpy as np
import matplotlib.pyplot as plt


def canny_image(img):
    #Convert to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    return cv2.Canny(blur, 50,150)

def region_of_interested(img):
    height = img.shape[0]
    print(height)
    
    polygons = np.array([[(200,height), (1100, height), (550,250)]])
    
    #np array of zeros, with the same shape of the img
    mask = np.zeros_like(img)

    #Create a maks, based on polygon generate before
    cv2.fillPoly(mask, polygons, 255)
    
    #Generete a masked image, with & operation between image and maks
    masked_image = cv2.bitwise_and(img , mask)

    return masked_image

def display_lines(img, lines):
    line_image = np.zeros_like(img)

    if(lines is not None):
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            #Draw lines based on cordinates
            cv2.line(line_image, (x1,y1), (x2,y2), (0, 255, 0), thickness=10)
        
    return line_image

#Read the image
img = cv2.imread('test_image.jpg')

#Make a copy
lane_image = np.copy(img)

canny =  canny_image(lane_image)

cropped_image = region_of_interested(canny)

#threshold is the minimum number of v otes needed to accept a candidate line
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)

line_image = display_lines(lane_image, lines)

combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)
#Show image
cv2.imshow('Combo_image',combo_image)
cv2.waitKey(0)
