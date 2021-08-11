# Geometric transforms

import numpy as np
from numpy import asarray
from PIL import Image
from scipy import ndimage

  
def main():
    # Open image
    image_in = Image.open('images/lena.jpg')
    image_in.show()
    # convert image to numpy array    
    image_np = np.array(image_in) 
    print(image_np.shape)

    # Zoom or Shrink image
    image_np_zoom = ndimage.zoom(image_np, (2, 2))
    print(image_np_zoom.shape)
    image_out = Image.fromarray(image_np_zoom)   
    image_out.show()
        
    # Rotation image 45º
    image_np_rotate  = ndimage.rotate(image_np, 45, cval=128)
    image_out = Image.fromarray(image_np_rotate)
    image_out.show()    


if __name__ == "__main__":
    main()