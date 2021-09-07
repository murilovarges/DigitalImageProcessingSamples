import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist
from PIL import Image


def fourier(frame):
    ndImage =  np.array(Image.fromarray(frame))
    image_gray = rgb2gray(ndImage)
    image_fourier = np.fft.fftshift(np.fft.fft2(image_gray))
    image_fourier = np.log(abs(image_fourier))
    return image_fourier, image_gray


def grab_frame(cap):
    key = cv2.waitKey(20)
    ret,frame = cap.read()
    return cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)


def opencamera():
    # Initiate camera
    cap1 = cv2.VideoCapture(1)

    # Create two subplots
    fig = plt.figure()
    ax1 = plt.subplot(1,2,1)
    ax2 = plt.subplot(1,2,2)
    
    # Create two image plots
    frame = grab_frame(cap1)
    fourier_img, image_gray = fourier(frame)
    im1 = ax1.imshow(image_gray, cmap='gray')
    im2 = ax2.imshow(fourier_img, cmap='gray')
    plt.ion()
    while True:
        frame_img = grab_frame(cap1)
        fourier_img, image_gray = fourier(frame_img)
        #im1.set_data(image_gray)
        im1.set_data(frame_img)
        im2.set_data(fourier_img)

        extent = ax2.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        plt.savefig('test.png')
        fig.savefig('fourier.png', bbox_inches=extent)

        plt.pause(0.01)
   

if __name__ == "__main__":
    opencamera()