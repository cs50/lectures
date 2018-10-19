import sys
from PIL import Image

if len(sys.argv) != 4:
    sys.exit("Usage: python resize.py n infile outfile")

n = int(sys.argv[1])
infile = sys.argv[2]
outfile = sys.argv[3]

inimage = Image.open(infile)
width, height = inimage.size
outimage = inimage.resize((width * n, height * n))

outimage.save(outfile)
