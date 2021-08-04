
import numpy as np
from PIL import Image  
from numpy import asarray
  
def main():
    # Open image
    image = Image.open('images/lena.jpg')
    print(image.format)
    print(image.size)
    print(image.mode)
    # convert image to numpy array    
    npImage = np.array(image) 
    print(type(npImage ))
    # summarize shape
    print(npImage.shape)
    
    # value of pixel 0 0
    print(npImage[0][0])
    print(npImage[10][10])
    
    #Change values os lines 10 - 25
    npImage[10:25,:] = 255;
    print(npImage[10][10])

    #Convert ndarray image to Pillow image
    image2 = Image.fromarray(npImage)
    image2.show()

    # create the histogram
    histogram, bin_edges = np.histogram(npImage, bins=256, range=(0, 255))
    print(histogram.shape)

if __name__ == "__main__":
    main()