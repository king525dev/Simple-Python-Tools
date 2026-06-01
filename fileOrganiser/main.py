import os;
import shutil;

# Initialise File Structure
FILE_STRUCTURE = {
     "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"],
     "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
     "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
     "Audio": [".mp3", ".wav", ".aac", ".flac"],
     "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
     "Data": [".csv", ".json", ".xml"],
     "Others": []
};

def organiseFiles(directory):
     """Organizes files in the given directory by their file types."""
     
     # Skip if directory is not valid
     if not os.path.isdir(directory):
          print(f"Error: {directory} is not a valid directory.");
          return
     
     # Create folders for each category if they don’t already exist
     for category in FILE_STRUCTURE:
          folder_path = os.path.join(directory, category);
          os.makedirs(folder_path, exist_ok=True);
          
     # Move files into appropriate folders
     for filename in os.listdir(directory):
          filePath = os.path.join(directory, filename);

          # Skip if it’s a directory
          if os.path.isdir(filePath):
               continue;
     
          # Check file extension and move to the corresponding folder
          fileMoved = False;
          changesMade = 0;
          for category, extensions in FILE_STRUCTURE.items():
               if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(filePath, os.path.join(directory, category, filename));
                    fileMoved = True;
                    changesMade += 1
                    break;

          # Move to "Others" if no match
          if not fileMoved:
               shutil.move(filePath, os.path.join(directory, "Others", filename));
               
     
     print(f"Files in '{directory}' have been organized with {changesMade} change(s) made")