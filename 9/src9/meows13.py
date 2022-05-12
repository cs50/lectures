# Adds description, help

import argparse
import sys

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args(sys.argv[1:])

for _ in range(int(args.n)):
    print("meow")
