import cv2
import numpy as np

def main():
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
  
  mask = mean
  while(True):        
    # Capture the video frame by frame
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    filteredImage = cv2.filter2D(src=gray, ddepth=-1, kernel=mask)    
    
    # Display the resulting frame      
    cv2.putText(gray, "FPS: {0}".format(fps), (5,20), font, 0.5, 0, 1, cv2.LINE_AA)
    cv2.imshow('Original', gray)
    cv2.imshow('Filtered', filteredImage)    
    
    # the 'q' and ESC buttons are set as the quitting button
    key = cv2.waitKey(10)
    if key == 27 or key == ord('q'): 
      break
    elif key == ord('m'):
      mask = mean
    elif key == ord('l'):      
      mask = laplacian
      print(mask)      
    elif key ==ord('x'):
      mask = sobelX
      print(mask)
    elif key == ord('y'):
      mask = sobelY
      print(mask)
    elif key == ord('b'):
      mask = boost
      print(mask)
  # After the loop release the cap object
  vid.release()
  # Destroy all the windows
  cv2.destroyAllWindows()


if __name__ == "__main__":
    main()