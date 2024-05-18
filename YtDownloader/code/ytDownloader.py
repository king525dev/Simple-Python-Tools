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

link = input("\nType in the link to your video: ")
print("\n")

# Get arguements
try:
     yt = YouTube(link)
except Exception as e:
     print(f"""\033[1;31m---> An error occured, please check the link or try again later\033[0m\n\033[5;1;31m\n\tERROR_MSG: \033[0m\033[31m{e}\033[0m""")

# If video exist, run downloading function
print("Title:\t", yt.title)
print("Views:\t", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download(get_downloads_folder())

print("\nnYouTube Video Downloaded Successfully, Check your \"Downloads\" Folder")


# Library Used: https://pytube.io/en/latest/