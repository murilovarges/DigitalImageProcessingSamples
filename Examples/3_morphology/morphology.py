# Example of Morphological Transformations
# Course: Digital Image Processing
# Bachelor in Computer Engineering
# IFSP - Campus Birgui 2022
# Professor Murilo Varges da Silva

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():  
    img = np.array([[0,0,0,0,0,0,0,0,0,0,0],
                    [0,1,1,1,1,1,1,1,1,0,0],
                    [0,1,1,1,1,0,0,1,1,1,0],
                    [0,1,1,1,1,0,0,1,1,1,0],
                    [0,1,1,1,1,0,0,1,1,1,0],
                    [0,1,1,1,1,1,1,1,1,0,0],
                    [0,1,1,1,1,0,0,1,1,1,0],
                    [0,1,1,1,1,0,0,1,1,1,0],
                    [0,1,1,1,1,0,0,1,1,1,0],
                    [0,1,1,1,1,1,1,1,1,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0]],  dtype="float")
    print(img.shape)
    print(img)        

    cross_structuring_element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    print(cross_structuring_element)

    # Erosion  
    erosion = cv2.erode(img, cross_structuring_element, iterations = 1) 
    print('erosion')
    print(erosion)

    # Dilation
    dilation  = cv2.dilate(img, cross_structuring_element, iterations = 1)
    print('dilation')
    print(dilation)  

    fig = plt.figure(1, figsize=(10, 5))
    ax = fig.add_subplot(1, 3, 1)
    ax.imshow(1-img, cmap='gray')
    ax = fig.add_subplot(1, 3, 2)
    ax.imshow(1-erosion, cmap='gray')
    ax = fig.add_subplot(1, 3, 3)
    fig.tight_layout()
    ax.imshow(1-dilation, cmap='gray')
    plt.show()  


if __name__ == "__main__":
    main()