import cv2
import numpy as np

def noisy(noise_typ, image):
  if noise_typ == "gauss":
      row, col, ch = image.shape
      mean = 0
      var = 0.1
      sigma = var**0.5
      gauss = np.random.normal(mean, sigma, (row, col, ch))
      gauss = gauss.reshape(row, col, ch)
      noisy = image + gauss
      return noisy
  elif noise_typ == "s&p":
      #row, col, ch = image.shape
      s_vs_p = 0.5
      amount = 0.05
      out = np.copy(image)
      # Salt mode
      num_salt = np.ceil(amount * image.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
      out[coords] = 255     

      # Pepper mode
      num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
      out[coords] = 0
      return out
  elif noise_typ == "poisson":
      vals = len(np.unique(image))
      vals = 2 ** np.ceil(np.log2(vals))
      noisy = np.random.poisson(image * vals) / float(vals)
      return noisy
  elif noise_typ =="speckle":
      row,col,ch = image.shape
      gauss = np.random.randn(row,col,ch)
      gauss = gauss.reshape(row,col,ch)        
      noisy = image + image * gauss
      return noisy

def change_mask(new_mask, name):
  global mask
  mask = new_mask
  global filter_name 
  filter_name = name
  print(name)
  print(mask)

def main():
  
  mean = np.array((
    [0.1111, 0.1111, 0.1111],
    [0.1111, 0.1111, 0.1111],
    [0.1111, 0.1111, 0.1111]), dtype="float")
  
  # define a video capture object
  vid = cv2.VideoCapture(0)
  font = cv2.FONT_HERSHEY_SIMPLEX
  fps = vid.get(cv2.CAP_PROP_FPS)
  print("FPS: {0}".format(fps)) 
  

  while(True):        
    # Capture the video frame by frame
    ret, image = vid.read()
    #image_flip =  cv2.flip(image, 3)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    
    image_gray = cv2.flip(image_gray, 1)
   
    image_noise = noisy('s&p', image_gray)    
    image_mean = cv2.blur(src=image_noise, ksize=(5,5))
    image_median = cv2.medianBlur(src=image_noise, ksize=3)    
    
    
    # Display the resulting frame      
    cv2.putText(image_gray, "FPS: {0}".format(fps), (5,20), font, 0.5, 0, 1, cv2.LINE_AA)
    cv2.imshow('Original', image_gray)    
    cv2.imshow('Noise', image_noise)    
    cv2.imshow('Mean Blur', image_mean)    
    cv2.imshow('Median Blur', image_median)    
    
    # the 'q' and ESC buttons are set as the quitting button
    key = cv2.waitKey(10)
    if key == 27 or key == ord('q'): 
      break
   
  # After the loop release the cap object
  vid.release()
  # Destroy all the windows
  cv2.destroyAllWindows()


if __name__ == "__main__":
    main()