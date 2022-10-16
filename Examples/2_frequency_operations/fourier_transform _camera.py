# Example of Fourier Transformations
# Course: Digital Image Processing
# Bachelor in Computer Engineering
# IFSP - Campus Birgui 2022
# Professor Murilo Varges da Silva

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
    img_gray = rgb2gray(ndImage)
    img_ftt = np.fft.fftshift(np.fft.fft2(img_gray))
    img_fft_amplitude = np.log(abs(img_ftt))
    img_fft_phase= np.angle(img_ftt)
    return img_fft_amplitude, img_fft_phase, img_gray


def grab_frame(cap):
    key = cv2.waitKey(20)
    ret,frame = cap.read()
    return cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)


def opencamera():
    # Initiate camera
    cap1 = cv2.VideoCapture(0) # mudar para 0 se tiver apenas uma camera

    # Create two subplots
    fig = plt.figure()
    ax1 = plt.subplot(1,3,1)
    ax2 = plt.subplot(1,3,2)
    ax3 = plt.subplot(1,3,3)
    ax1.title.set_text('Original Image')
    ax2.title.set_text('Fourier Amplitude')
    ax3.title.set_text('Fourier Phase')
    
    # Create two image plots
    frame = grab_frame(cap1)
    img_fft_amplitude, img_fft_phase, img_gray = fourier(frame)
    im1 = ax1.imshow(img_gray, cmap='gray')
    im2 = ax2.imshow(img_fft_amplitude, cmap='gray')
    im3 = ax3.imshow(img_fft_phase, cmap='gray')
    plt.ion()
    while True:
        frame_img = grab_frame(cap1)
        img_fft_amplitude, img_fft_phase, img_gray = fourier(frame_img)
        #im1.set_data(image_gray)
        im1.set_data(frame_img)
        im2.set_data(img_fft_amplitude)
        im3.set_data(img_fft_phase)

        extent = ax1.get_window_extent().transformed(fig.dpi_scale_trans.inverted())        
        fig.savefig('images/fourier-original.png', bbox_inches=extent)
        extent = ax2.get_window_extent().transformed(fig.dpi_scale_trans.inverted())        
        fig.savefig('images/fourier-amplitude.png', bbox_inches=extent)
        extent = ax3.get_window_extent().transformed(fig.dpi_scale_trans.inverted())        
        fig.savefig('images/fourier-phase.png', bbox_inches=extent)

        plt.pause(0.00001)
   

if __name__ == "__main__":
    opencamera()