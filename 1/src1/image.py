from PIL import Image


def convert(image):
    ascii_str = ""
    width, height = image.size
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            if pixel > 128:
                ascii_str += "0"
            else:
                ascii_str += "1"
        ascii_str += "\n"
    return ascii_str


image = Image.open("image.jpg")
image = image.resize((103, 26)).convert("L")  # Manually sized for Google Slide
print(convert(image))
