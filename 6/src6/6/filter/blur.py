# Blurs an image

from PIL import Image, ImageFilter
from sys import argv

# Blur image
if len(argv) == 3:
    before = Image.open(argv[1])
    after = before.filter(ImageFilter.BLUR)
    after.save(argv[2])
