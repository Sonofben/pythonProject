import os
from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    resized_image = original_image.resize(size)
    resized_image.save(output_image_path)
def compress_image(input_image_path, output_image_path, quality=10):
    original_image = Image.open(input_image_path)
    original_image.save(output_image_path, optimize=True, quality=quality)
def batch_resize_images(file_paths, output_folder, size):
    for file_path in file_paths:
        filename = os.path.basename(file_path)
        output_path = os.path.join(output_folder, filename)
        resize_image(file_path, output_path, size)


