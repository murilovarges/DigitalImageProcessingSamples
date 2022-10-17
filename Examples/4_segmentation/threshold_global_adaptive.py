# Example of Segmentation Using Global and Adaptive Threshold
# Course: Digital Image Processing
# Bachelor in Computer Engineering
# IFSP - Campus Birgui 2022
# Professor Murilo Varges da Silva

import cv2 as cv
import numpy as np

def main():
  img = cv.imread('../../Images/hand_text.tif', cv.IMREAD_GRAYSCALE)
  
  # global thresholding
  ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)  
  
  # Otsu's thresholding
  ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)  
  
  # Otsu's thresholding after Gaussian filtering
  blur = cv.GaussianBlur(img,(5,5),0)
  ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
  
  # Adaptive thresholding
  th4 = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
  th5 = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
  
  cv.imshow('Original', img)
  cv.imshow('Global threshold', th1)
  cv.imshow('Otsu threshold', th2)
  cv.imshow('Blur + Otsu threshold', th3)
  cv.imshow('Mean threshold', th4)
  cv.imshow('Gaussian threshold', th5)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
    main()