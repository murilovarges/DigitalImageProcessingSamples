# Image Geometric transforms
import numpy as np
from numpy import asarray
from PIL import Image
from scipy import ndimage

  
def main():
    # Image filtered using ImageJ for comparison
    image_in = Image.open('images/lena_filtered1_imagej.tiff')
    image_np = np.array(image_in)
    print('Image filtered in ImagJ')
    print(image_np)
    print(image_np.min(),image_np.max())
    
    # Open image
    image_in = Image.open('images/lena.jpg')
    image_in.show()
    # convert image to numpy array    
    # convert to int to allow negative values
    image_np = np.array(image_in).astype(int) 
    print('Image original')    
    print(image_np)
    print(image_np.min(),image_np.max())

    # Convolution filter usingo mode reflect
    kernel = np.array([[ 1, 0,-1],
                       [ 0, 0, 0],
                       [-1, 0, 1]])
    print('Image after convolution')    
    im1 = ndimage.convolve(image_np, kernel, mode='reflect')
    print()
    print(im1)
    print(im1.min(),im1.max())
    # replace negative values with 0
    im1 = np.where(im1<0, 0, im1)
    print('Image after convolution and zero replace')    
    print(im1)
    print(im1.min(),im1.max())
    # convert array to image usint uint8 type
    image_out = Image.fromarray(im1.astype('uint8'))   
    image_out.show()       
    image_out.save('images/lena_filtered1.tiff')

    
if __name__ == "__main__":
    main()