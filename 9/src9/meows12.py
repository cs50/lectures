# Uses command-line argument

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args(sys.argv[1:])

for _ in range(int(args.n)):
    print("meow")
