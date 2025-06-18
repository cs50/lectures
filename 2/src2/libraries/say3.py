# Demonstrates own module

import sys

from sayings1 import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
