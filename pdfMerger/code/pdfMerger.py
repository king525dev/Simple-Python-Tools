import sys
import os
from PyPDF2 import PdfMerger, PdfReader

# Create a PdfFileMerger
merger = PdfMerger()

# Append pages from PDF files
for file in os.listdir(os.curdir):
     if file.endswith(".pdf"):
          print(file);
          merger.append(PdfReader(file))

# Write the merged output to a new file
merger.write("document-output.pdf")
