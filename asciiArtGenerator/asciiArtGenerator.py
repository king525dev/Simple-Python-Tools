import os
import pyfiglet
import ascii_magic
from PIL import Image

print("""
=================================
     ASCII ART GENERATOR
=================================
""")

inputType = input("Are you generating an Image or Text (img or txt): ")

if inputType == "txt": 

     styles = [
          "slant",
          "3-d",
          "3x5 (you can set custom dimensions)",
          "5lineoblique", 
          "alphabet",
          "banner3-D",
          "doh", 
          "isometric1",
          "letters",
          "alligator",
          "dotmatrix",
          "bubble",
          "bulbhead",
          "digital"
     ]
     
     text =  input("Enter Text you want to convert to ASCII art : ")

     print("\n")
     for style in styles:
          print("- %s" % style)
     print("\n")

     fontStyle = input("Pick an ASCII Art style: ")

     asciiArt = pyfiglet.figlet_format(text,font=fontStyle)

     with open("output.txt", 'w') as file:
          file.write(asciiArt)

     print("\n")
     print(asciiArt);
     print("\nFile Created")

elif inputType == "img":
     imgLnk = input("Enter the path to the image: ")

     try:
          img = Image.open(imgLnk);
     except:
          print(imgLnk, "Unable to find image ");

     imgType = input("Do you want your image to be colour coded or character coded (char or colr): ")

     if( imgType == "colr"):
          columnNo = int(input("How many columns wide do you want your image: "))

          output = ascii_magic.from_pillow_image(img)
          output.to_terminal(columns=columnNo);
          output.to_html_file("output.html", columns=columnNo)
          print("\nFile Created")
     else: 
          columnNo = int(input("How many columns wide do you want your image: "))

          # Re-adjust width and height
          width, height = img.size[:2]

          if height > width: 
               baseHeight = columnNo
               heightPercentage = baseHeight / float(img.size[1])
               widthSize = int(float(img.size[0]) * float(heightPercentage))
               img = img.resize((widthSize, baseHeight), Image.LANCZOS)
          else:
               baseWidth = columnNo
               widthPercentage = baseWidth / float(img.size[0])
               heightSize = int(float(img.size[1]) * float(widthPercentage))
               img = img.resize((baseWidth, heightSize), Image.LANCZOS)

          # Convert image to greyscale
          img = img.convert('L')

          # Character List
          chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]

          pixels = img.getdata()

          pixels = img.getdata()
          new_pixels = [chars[pixel//25] for pixel in pixels]
          new_pixels = ''.join(new_pixels)

          new_pixels_count = len(new_pixels)
          ascii_image = [new_pixels[index:index + baseWidth] for index in range(0, new_pixels_count, baseWidth)]
          ascii_image = "\n".join(ascii_image)
          print(ascii_image)

          # write to a text file.
          with open("output.txt", "w") as f:
               f.write(ascii_image)
          
          print("\nFile Created")
else: 
     # Generate random Ascii Image
     ascii_magic.AsciiArt.quick_test()