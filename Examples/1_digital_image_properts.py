
from PIL import Image  
  
image = Image.open('images/lena.jpg')
  
def main():
    print(image.format)
    print(image.size)
    print(image.mode)

if __name__ == "__main__":
    main()