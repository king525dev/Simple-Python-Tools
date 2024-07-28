import os
import segno

print("""
=================================
     QR CODE GENERATOR
=================================
""")

def main():

     link = input("Input the link to encode: ")
     name = input("Name the QR Code: ")
     edit = input("Do you want to customize the QR Code (y or n): ")

     if(edit == "n"):
          qrCode = segno.make_qr(link)
          qrCode.save(
               f"{name}.png",
               scale=10
               );
          print("\nQR Code Successfully Generated")
          end = input("Press enter to close....")
          return;
     
     bgColour = input("\nInput your desired background colour: ") or "white"
     fgColour = input("Input your desired foreground colour: ") or "black"
     size = int(input("Input your desired QR code size: ") or "10")
     borderSize = int(input("Input your desired QR code border size: ") or "5") 
     borderColour = input("Input your desired QR code border colour: ") or "white"
     fileFormat = input("What format do you want to save you QR code in?: ") or "png"

     qrCode = segno.make_qr(link)
     qrCode.save(
          f"{name}.{fileFormat}",
          scale=size,
          light=bgColour,
          dark=fgColour,
          quiet_zone=borderColour,
          border=borderSize,
          );
     print("\nQR Code Successfully Generated")
     end = input("Press enter to close....")
     return;

main()

#Reference: https://realpython.com/python-generate-qr-code/