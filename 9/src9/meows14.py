# Adds default, type; removes int()

import argparse
import sys

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args(sys.argv[1:])

for _ in range(args.n):
    print("meow")
