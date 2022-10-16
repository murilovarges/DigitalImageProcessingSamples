import numpy as np
import cv2

def fourier(frame):
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dft = cv2.dft(np.float32(img_gray),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    img_fft_amplitude = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))    
    return img_fft_amplitude, img_gray

def grab_frame(cap):
    key = cv2.waitKey(20)
    ret,frame = cap.read()
    return cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

def opencamera():
    # Initiate camera
    vid = cv2.VideoCapture(0) # mudar para 0 se tiver apenas uma camera        
    
    while True:
        frame_img = grab_frame(vid)
        img_fft_amplitude, img_gray = fourier(frame_img)
        cv2.imshow('Original', img_gray)
        cv2.imshow('Fourier Amplitude', img_fft_amplitude)            
        # the 'q' and ESC buttons are set as the quitting button
        key = cv2.waitKey(10)
        if key == 27 or key == ord('q'): 
            break
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
   

if __name__ == "__main__":
    opencamera()