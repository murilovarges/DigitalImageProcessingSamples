import numpy as np
from PIL import Image  
import matplotlib.pyplot as plt
import scipy.misc
from mpl_toolkits.mplot3d import Axes3D
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv


def main():
    # load image
    #img = Image.open('images/lena.jpg')
    img = Image.open('images/sinc-fourier-amplitude.png')
    if img.mode != 'L':
        img = rgb2gray(np.array(img))
        img = Image.fromarray(img)
    
    # downscaling has a "smoothing" effect        
    size = tuple((np.array(img.size) * 0.15).astype(int))
    img =  np.array(img.resize(size, Image.BICUBIC))
    #img =  np.array(img)

    # create the x and y coordinate arrays (here we just use pixel indices)
    xx, yy = np.mgrid[0:img.shape[0], 0:img.shape[1]]

    # create the figure
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(xx, yy, img ,rstride=1, cstride=1, cmap=plt.cm.hot,linewidth=0)

    # show it
    plt.show()


if __name__ == "__main__":
    main()