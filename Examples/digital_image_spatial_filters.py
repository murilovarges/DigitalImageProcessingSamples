from asyncio.windows_events import NULL
import cv2
import numpy as np

global mask 
global filter_name 

def change_mask(new_mask, name):
  global mask
  mask = new_mask
  global filter_name 
  filter_name = name
  print(name)
  print(mask)

def main():
  # identity  
  identity = np.array((
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]), dtype="int")

  # mean  
  mean = np.array((
    [0.1111, 0.1111, 0.1111],
    [0.1111, 0.1111, 0.1111],
    [0.1111, 0.1111, 0.1111]), dtype="float")

  # construct the Laplacian kernel used to detect edge-like regions of an image
  laplacian = np.array((
    [0,  1, 0],
    [1, -4, 1],
    [0,  1, 0]), dtype="int")
  
  # construct the Sobel x-axis kernel
  sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="int")
  
  # construct the Sobel y-axis kernel
  sobelY = np.array((
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]), dtype="int")  

  # boost 
  boost = np.array((
    [ 0,  -1,  0],
    [-1, 5.2, -1],
    [ 0,  -1,  0]), dtype="float")

  
  # define a video capture object
  vid = cv2.VideoCapture(0)
  font = cv2.FONT_HERSHEY_SIMPLEX
  fps = vid.get(cv2.CAP_PROP_FPS)
  print("FPS: {0}".format(fps)) 
  
  global mask 
  mask = identity
  global filter_name
  filter_name = 'Identity'
  while(True):        
    # Capture the video frame by frame
    ret, image = vid.read()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray = cv2.flip(image_gray, 1)
    image_filtered = cv2.filter2D(src=image_gray, ddepth=-1, kernel=mask)    
    
    # Display the resulting frame      
    cv2.putText(image_gray, "FPS: {0}".format(fps), (5,20), font, 0.5, 0, 1, cv2.LINE_AA)
    cv2.imshow('Original', image_gray)
    cv2.putText(image_filtered, filter_name, (5,20), font, 0.5, 125, 1, cv2.LINE_AA)
    cv2.imshow('Filtered', image_filtered)    
    
    # the 'q' and ESC buttons are set as the quitting button
    key = cv2.waitKey(10)
    if key == 27 or key == ord('q'): 
      break
    elif key == ord('i'):
      change_mask(identity, 'Identity')
    elif key == ord('m'):
      change_mask(mean, 'Mean')
    elif key == ord('l'): 
      change_mask(laplacian, 'Laplacian')
    elif key ==ord('x'):
      change_mask(sobelX, 'Sobel X')
    elif key == ord('y'):
      change_mask(sobelY, 'Sobel Y')
    elif key == ord('b'):
      change_mask(boost, 'Boost')
  # After the loop release the cap object
  vid.release()
  # Destroy all the windows
  cv2.destroyAllWindows()


if __name__ == "__main__":
    main()