# Example of Hough Transform for Lines Detection
# Course: Digital Image Processing
# Bachelor in Computer Engineering
# IFSP - Campus Birgui 2022
# Professor Murilo Varges da Silva

import math
import cv2
import numpy as np

def main():
  img = cv2.imread('../../Images/paper.png', 0)  
  img_blur = cv2.GaussianBlur(img, (5,5), 0)
  img_canny = cv2.Canny(image=img_blur,  threshold1=50, threshold2=200, apertureSize = 3)
  img_color1 = cv2.cvtColor(img_canny, cv2.COLOR_GRAY2BGR)
  img_color2 = np.copy(img_color1)
  
  # Hough Transform Standard
  lines = cv2.HoughLines(img_canny, 1, np.pi / 180, 150, None, 0, 0)
  if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv2.line(img_color1, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)  
  
  # Hough Transform Probabilistic
  linesP = cv2.HoughLinesP(img_canny, 1, np.pi / 180, 50, 100, minLineLength=10, maxLineGap=250)
  if linesP is not None:
      for i in range(0, len(linesP)):
          l = linesP[i][0]
          cv2.line(img_color2, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)  

  cv2.imshow('Original', img)  
  cv2.imshow('Canny', img_canny)
  cv2.imshow('Detected Lines - Standard Hough Transform', img_color1)
  cv2.imshow('Detected Lines - Probabilistic Hough Transform', img_color2)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == "__main__":
    main()