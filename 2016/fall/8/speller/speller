#!/usr/bin/env python3

import re
import sys
import time
from dictionary import Dictionary

# maximum length for a word
# (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
LENGTH = 45

# default dictionary
WORDS = "/home/cs50/pset5/dictionaries/large"

# check for correct number of args
if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("Usage: ./speller [dictionary] text")
    exit(1) 

# benchmarks
time_load, time_check, time_size, time_unload = 0.0, 0.0, 0.0, 0.0

# determine dictionary to use
dictionary = sys.argv[1] if len(sys.argv) == 3 else WORDS

# load dictionary
d = Dictionary()
before = time.process_time()
loaded = d.load(dictionary)
after = time.process_time()

# abort if dictionary not loaded
if not loaded: 
    print("Could not load $dictionary.")
    exit(1)

# calculate time to load dictionary
time_load = after - before

# try to open file
file = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1]
fp = open(file, "r", encoding="latin_1")
if not fp:
    print("Could not open {}.".format(file))
    exit(1)

# prepare to report misspellings
print("\nMISSPELLED WORDS\n")

# prepare to spell-check
word = ""
index, misspellings, words = 0, 0, 0

# spell-check each word in file
while True:
    c = fp.read(1)
    if not c:
        break
    
    # allow alphabetical characters and apostrophes (for possessives)
    if re.match(r"[A-Za-z]", c) or (c == "'" and index > 0):

        # append character to word
        word += c
        index += 1

        # ignore alphabetical strings too long to be words
        if index > LENGTH:

            # consume remainder of alphabetical string
            while True:
                c = fp.read(1)
                if not c or not re.match(r"[A-Za-z]", c):
                    break

            # prepare for new word
            index, word = 0, ""

    # ignore words with numbers (like MS Word)
    elif c.isdigit():
        
        # consume remainder of alphabetical string
        while True:
            c = fp.read(1)
            if not c or (not c.isalpha() and not c.isdigit()):
                break

        # prepare for new word
        index, word = 0, ""

    # we must have found a whole word
    elif index > 0:

        # update counter
        words += 1

        # check word's spelling
        before = time.process_time()
        misspelled = not d.check(word)
        after = time.process_time()

        # update benchmark
        time_check += after - before

        # print word if misspelled
        if misspelled:
            print(word)
            misspellings += 1

        # prepare for next word
        index, word = 0, ""

# close file
fp.close()

# determine dictionary's size
before = time.process_time()
n = d.size()
after = time.process_time()

# calculate time to determine dictionary's size
time_size = after - before

# unload dictionary
before = time.process_time()
unloaded = d.unload()
after = time.process_time();

# abort if dictionary not unloaded
if not unloaded:
    print("Could not load $dictionary.")
    exit(1)

# calculate time to determine dictionary's size
time_unload = after - before

# report benchmarks
print("\nWORDS MISSPELLED:     {}".format(misspellings))
print("WORDS IN DICTIONARY:  {}".format(n))
print("WORDS IN TEXT:        {}".format(words))
print("TIME IN load:         {:.2f}".format(time_load))
print("TIME IN check:        {:.2f}".format(time_check))
print("TIME IN size:         {:.2f}".format(time_size))
print("TIME IN unload:       {:.2f}".format(time_unload))
print("TOTAL TIME:           {:.2f}\n".format(time_load + time_check + time_size + time_unload))
