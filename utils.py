import os

def clean_temp_files():
    if os.path.exists("temp_img.jpg"):
        os.remove("temp_img.jpg")