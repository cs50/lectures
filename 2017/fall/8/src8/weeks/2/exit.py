# Exits with explicit value

import sys

if len(sys.argv) != 2:
    print("missing command-line argument")
    sys.exit(1)

print(f"hello, {argv[1]}")
sys.exit(0)
