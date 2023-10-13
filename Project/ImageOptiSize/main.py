import tkinter as tk
from user_interface import create_ui
from image_resizer import resize_image, add_watermark

# Your main application logic here

if __name__ == "__main__":
    create_ui()

# Assuming you've resized the image and saved it in the user interface after the "Resize" button is clicked
# Call the add_watermark function here
add_watermark("resized_image.jpg", "watermarked_image.jpg", "Your Watermark Text")
