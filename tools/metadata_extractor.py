"""
Tool: Metadata Extractor
Author: PatrickWorthey
Description:
    This tool extracts and displays EXIF metadata from image files.
    A file picker window allows users to choose the image interactively.
    If no EXIF metadata is found, will print a statement saying 'No EXIF metadata found'.

Dependencies:
    pip install Pillow
"""

from PIL import Image                   #Open and read image files
from PIL.ExifTags import TAGS           
from tkinter import Tk, filedialog      #Open GUI to select the image

def extract_exif_data(image_path):
    '''Opens the image and prints the EXIF tags, if present'''
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()

        if not exif_data:
            print("No EXIF metadata found.")
            return

        print(f"\n Metadata for: {image_path}\n" + "-" * 40) # Visual display of progress for the user
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)                   # Convert tag to a readable format
            print(f"{tag:25}: {value}")                      # Print each tag and value

    except Exception as e:
        print(f" Error reading image: {e}")

def choose_file():
    root = Tk()
    root.withdraw()                                         # Hide the empty tkinter window
    file_path = filedialog.askopenfilename(                 # Open window for file selection
        title="Select an image file",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    return file_path

def main():
    image_path = choose_file()
    if image_path:
        extract_exif_data(image_path)
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()
