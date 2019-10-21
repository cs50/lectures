# Exits with explicit value, importing sys

import sys

if len(sys.argv) != 2:
    sys.exit("missing command-line argument")
print(f"hello, {sys.argv[1]}")
sys.exit(0)
