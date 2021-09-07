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
    npImageFilter = np.empty(npImage.shape)

    # values os a windows 5 X 5 
    print(npImage[0:5, 0:5])

    m = npImage.shape[0] # qtd lines
    n = npImage.shape[1] # qtd cols
    for x in range(1, m-2):
        for y in range (1, n-2):
            w = npImage[x-1:x+2 , y-1:y+2]
            #print(x,y)
            #print(w)
            #print(np.mean(w).astype(int))
            npImageFilter[x,y] = np.mean(w).astype(int)
    
    # values os a windows 5 X 5 
    print(npImage[0:5, 0:5])        
    #Convert ndarray image to Pillow image
    image2 = Image.fromarray(npImageFilter)
    image2.show()


if __name__ == "__main__":
    main()