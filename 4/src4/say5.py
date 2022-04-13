# Demonstrates own module

import sys

from sayings2 import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
