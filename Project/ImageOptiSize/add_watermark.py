from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, imageopti):
    original_image = Image.open(input_image_path)

    # Create a drawing context
    draw = ImageDraw.Draw(original_image)

    # Define the watermark text
    watermark = imageopti

    # Load a font
    font = ImageFont.load_default()

    # Position the watermark
    text_width, text_height = draw.textsize(watermark, font)
    width, height = original_image.size
    x = width - text_width - 10  # Adjust the position as needed
    y = height - text_height - 10

    # Define the text color
    text_color = (255, 255, 255)  # White

    # Add the watermark
    draw.text((x, y), watermark, fill=text_color, font=font)

    original_image.save(output_image_path)
