
from PIL import Image  
from numpy import asarray
  
def main():
    # Open image
    image = Image.open('images/lena.jpg')
    print(image.format)
    print(image.size)
    print(image.mode)
    # convert image to numpy array
    data = asarray(image)
    print(type(data))
    # summarize shape
    print(data.shape)
    # value of pixel 0 0
    print(data[0][0])

if __name__ == "__main__":
    main()