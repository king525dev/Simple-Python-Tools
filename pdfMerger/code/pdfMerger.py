import sys
import os
from PyPDF2 import PdfMerger, PdfReader

print("""
=================================
     PDF MERGER
=================================
""")

# Create a PdfFileMerger
merger = PdfMerger()

print("This program will merge a copy of every PDF document in this directory and save it to a single PDF")
name = input("Name the output file: ") or "document-output"
start = input("Press enter to start...\n")

print("=====")
# Append pages from PDF files
for file in os.listdir(os.curdir):
     if file.endswith(".pdf"):
          print(file);
          merger.append(PdfReader(file))

# Write the merged output to a new file
merger.write(f"{name}.pdf")

print("=====")

print("\nFiles Successfully Merged")
end = input("Press enter to close...")