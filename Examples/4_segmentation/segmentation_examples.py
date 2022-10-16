# Example of Segmentation Using Canny Edge Detection
# Course: Digital Image Processing
# Bachelor in Computer Engineering
# IFSP - Campus Birgui 2022
# Professor Murilo Varges da Silva

import cv2
import numpy as np

def main():
  img = cv2.imread('../../Images/biel.png', 0)  
  img_blur = cv2.GaussianBlur(img, (3,3), 0)

  img_sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
  img_sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
  img_sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)  
  img_canny = cv2.Canny(image=img_blur, threshold1=50, threshold2=100)

  cv2.imshow('Original', img)
  cv2.imshow('Blur', img_blur)
  cv2.imshow('Sobel X', img_sobelx)
  cv2.imshow('Sobel Y', img_sobely)
  cv2.imshow('Sobel XY', img_sobelxy)
  cv2.imshow('Canny', img_canny)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == "__main__":
    main()