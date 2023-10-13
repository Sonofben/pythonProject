import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("ImageOptiSize - Image Resizer")

# Function to open a file dialog for image selection
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    # Display the selected image in the GUI
    image = Image.open(file_path)
    image.thumbnail((200, 200))
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.photo = photo
    # Store the selected file path for resizing
    global selected_file_path
    selected_file_path = file_path

# Create an "Open File" button
open_file_button = tk.Button(window, text="Open File", command=open_file_dialog)
open_file_button.pack()

# Create a label to display the selected image
image_label = tk.Label(window)
image_label.pack()

# Function to resize the image
def resize_image():
    if selected_file_path:
        new_size = (300, 300)  # Change this size as needed
        resized_image = Image.open(selected_file_path)
        resized_image.thumbnail(new_size)
        resized_image.save("resized_image.jpg")
        tk.messagebox.showinfo("Image Resized", "Image has been resized and saved as 'resized_image.jpg'")

# Create a "Resize" button
resize_button = tk.Button(window, text="Resize", command=resize_image)
resize_button.pack()

# Initialize the selected_file_path variable
selected_file_path = None

# Start the GUI main loop
window.mainloop()
