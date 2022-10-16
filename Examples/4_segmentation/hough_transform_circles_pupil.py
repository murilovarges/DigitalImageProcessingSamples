# Example of Hough Transform for Circles Detection
# Course: Digital Image Processing
# Bachelor in Computer Engineering
# IFSP - Campus Birgui 2022
# Professor Murilo Varges da Silva

import math
import cv2 as cv
import numpy as np

def main():
  # Reading image  
  img_color = cv.imread('../../Images/pupil.jpg', cv.IMREAD_COLOR )  
  img = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
  
  # Blurring and erasing little details
  kernel = np.ones((5,5),np.uint8)
  img = cv.GaussianBlur(img, (9,9), 0)
  img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
  img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
  
  #Thresholding to highlight the more dark areas
  img = cv.threshold(img, 40, 255, cv.THRESH_BINARY_INV)[1]
  img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
  rows = img.shape[0]
  circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT,
                          dp=1.1,minDist=300,param1=200,param2=40,minRadius=20,maxRadius=400)
  
  print(circles)
  if circles is not None:
      circles = np.uint16(np.around(circles))
      for i in circles[0, :]:
        # draw the outer circle
        cv.circle(img_color,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv.circle(img_color,(i[0],i[1]),2,(0,0,255),3) 
 
  img_canny = cv.Canny(image=img, threshold1=50, threshold2=100, apertureSize=3) 
  cv.imshow('Original', img)  
  cv.imshow('Canny', img_canny)
  cv.imshow('Detected Circle -  Hough Transform', img_color) 

  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
    main()