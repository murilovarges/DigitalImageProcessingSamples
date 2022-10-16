# Example of Morphological Transformations
# Course: Digital Image Processing
# Bachelor in Computer Engineering
# IFSP - Campus Birgui 2022
# Professor Murilo Varges da Silva

import cv2
import numpy as np

def main():
  # Read images and 
  img1 = cv2.imread('../../Images/morphology/Imagem1.tif', 0)  
  img2 = cv2.imread('../../Images/morphology/Imagem2.tif', 0)  
  
  # Create structuring element
  # Using only Numpy
  # square_structuring_element = np.ones((3,3), np.uint8)
  # Using OpenCV functions
  # square_structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
  # elliptical_structuring_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
  cross_structuring_element = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

  # Erosion  
  erosion = cv2.erode(img1, cross_structuring_element, iterations = 1) 
  showImages(img1, erosion) 

  # Dilation
  dilation  = cv2.dilate(img2, cross_structuring_element, iterations = 1)
  showImages(img2, dilation)

  # Opening
  # Direct mode using OpenCV
  # opening   = cv2.morphologyEx(img1, cv2.MORPH_OPEN, cross_structuring_element)  
  # Applying erosion + ditation
  erosion = cv2.erode(img1, cross_structuring_element, iterations = 1) 
  opening  = cv2.dilate(erosion, cross_structuring_element, iterations = 1)
  showImages(img1, opening )

  # Closing
  # Direct mode using OpenCV
  # closing   = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, cross_structuring_element)  
  # Applying ditation + erosion
  dilation  = cv2.dilate(img2, cross_structuring_element, iterations = 1)
  closing = cv2.erode(dilatation, cross_structuring_element, iterations = 1) 
  showImages(img2, closing)


def showImages(img1, img2):
  cv2.imshow('Original', img1)
  cv2.imshow('Result', img2)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == "__main__":
    main()