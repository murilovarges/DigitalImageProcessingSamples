# Apply a mean filter
import numpy as np
from PIL import Image  
from numpy import asarray
  
def main():
    # Open image
    image = Image.open('images/lena.jpg')
    image.show()
    # convert image to numpy array    
    npImage = np.array(image) 

    # values os a windows 5 X 5 
    print(npImage[0:5, 0:5])

    m = npImage.shape[0]
    n = npImage.shape[1]
    for x in range(1, m-2):
        for y in range (1, n-3):
            npImage[x,y] = np.mean(npImage[x-1:x+2,y-1:y+2]).astype(int);
    
    # values os a windows 5 X 5 
    print(npImage[0:5, 0:5])        
    #Convert ndarray image to Pillow image
    image2 = Image.fromarray(npImage)
    image2.show()


if __name__ == "__main__":
    main()