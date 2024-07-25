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
               )

main()

#Reference: https://realpython.com/python-generate-qr-code/