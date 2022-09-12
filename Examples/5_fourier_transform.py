import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist

def main():
    lena_image = imread('images/newspaper_shot_woman.tif')    
    plt.figure(num=None, figsize=(8, 6), dpi=80)
    plt.imshow(lena_image, cmap='gray')

    # transformada de fourier
    lena_image_fourier = np.fft.fft2(lena_image)
    plt.figure(num=None, figsize=(8, 6), dpi=80)    
    plt.imshow(np.log(abs(lena_image_fourier)), cmap='gray')

    # centralização do espectro de fourie
    lena_image_fourier_shift = np.fft.fftshift(lena_image_fourier)
    plt.figure(num=None, figsize=(8, 6), dpi=80, frameon=False)
    plt.axis('off')
    plt.imshow(np.log(abs(lena_image_fourier_shift)), cmap='gray')
    plt.savefig('images/woman-fourier-amplitude.png', bbox_inches='tight', pad_inches=0)
    
    plt.show()


if __name__ == "__main__":
    main()