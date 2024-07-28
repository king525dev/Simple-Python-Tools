import asyncio
import os
from pytube import YouTube
from sys import argv

# Get downloads folder
def get_downloads_folder():
     home_dir = os.path.expanduser("~")
     downloads_folder = os.path.join(home_dir, "Downloads")
     return downloads_folder

# User Query

print("""
===================================
     YOUTUBE VIDEO DOWNLOADER
===================================
""")

def main():
     link = input("\nType in the link to your video: ")
     print("\n")

     # Get arguements
     try:
          yt = YouTube(link)
     except Exception as e:
          print(f"""\033[1;31m---> An error occured, please check the link or try again later\033[0m\n\033[5;1;31m\n\tERROR_MSG: \033[0m\033[31m{e}\033[0m""")
          end = input("Press enter to close....")

     # If video exist, run downloading function
     print("Title:\t", yt.title)
     print("Views:\t", yt.views)

     yd = yt.streams.get_highest_resolution()

     down = input("\n Do you wan to save the video to your Downloads folder? (y or n): ")

     if down == "y":
          yd.download(get_downloads_folder())

          print("\nnYouTube Video Downloaded Successfully, Check your \"Downloads\" Folder")
          end = input("Press enter to close....")
          return

     yd.download()

     print("\nnYouTube Video Downloaded Successfully, Check your \"Downloads\" Folder")
     end = input("Press enter to close....")
     return

main()

#Add playlist feature
# Library Used: https://pytube.io/en/latest/