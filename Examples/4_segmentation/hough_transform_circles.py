# Example of Hough Transform for Circles Detection
# Course: Digital Image Processing
# Bachelor in Computer Engineering
# IFSP - Campus Birgui 2022
# Professor Murilo Varges da Silva

import cv2 as cv
import numpy as np

def main():  
  img_color = cv.imread('../../Images/circles.png', cv.IMREAD_COLOR)  
  img = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
   
  img_blur = cv.GaussianBlur(img, (3,3), 0)  
  rows = img.shape[0]
  circles = cv.HoughCircles(img_blur, cv.HOUGH_GRADIENT,
                          dp=1,minDist=50,param1=30,param2=15,minRadius=0,maxRadius=0)
  
  print(circles)
  if circles is not None:
      circles = np.uint16(np.around(circles))
      for i in circles[0, :]:
        # draw the outer circle
        cv.circle(img_color,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv.circle(img_color,(i[0],i[1]),2,(0,0,255),3) 
  
  img_canny = cv.Canny(image=img_blur, threshold1=100, threshold2=200, apertureSize=3)  
  cv.imshow('Original', img)  
  cv.imshow('Canny', img_canny)
  cv.imshow('Detected Circle -  Hough Transform', img_color) 

  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
    main()