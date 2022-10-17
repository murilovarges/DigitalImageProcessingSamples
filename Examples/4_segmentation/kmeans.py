# Example of Segmentation Using K-means and Adaptive Threshold
# Course: Digital Image Processing
# Bachelor in Computer Engineering
# IFSP - Campus Birgui 2022
# Professor Murilo Varges da Silva

import cv2 as cv
import numpy as np

def main():
  img = cv.imread('../../Images/sushi.jpg', cv.IMREAD_COLOR)
  
  # Covert 3D image in a flatten vector
  Z = img.reshape((-1,3))
  print(Z.shape)
  # convert to np.float32
  Z = np.float32(Z)
  # Define criteria, number of clusters(K) and apply kmeans()
  criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
  K = 8
  ret,label,center=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
  print(center)
  print(label.flatten())
  print(ret)
  # Now convert back into uint8, and make original image
  center = np.uint8(center)
  res = center[label.flatten()]
  res2 = res.reshape((img.shape))

  colors =  np.array((
    [255, 0, 0],      # red
    [0, 255, 0],      # green
    [0, 0, 255],      # green
    [0, 0, 0],        # black
    [255, 255, 255],  # white
    [0, 255, 0],      # lime    
    [255, 255, 0],    # yellow    
    [192, 192, 192],  # silver 
    ), dtype="float")
  print(colors)
  res = colors[label.flatten()]
  res3 = res.reshape((img.shape))
  
  cv.imshow('Original', img)
  cv.imshow('K-means result', res2)
  cv.imshow('K-means result colors', res3)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
    main()