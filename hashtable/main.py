#!/usr/bin/env python3
import os
import sys
import argparse
from hashtable import *


def main(arguments):
    # Create a StringHashtable.
    string_hash = StringHashtable()
    # Add each bug in `strings.txt` with the key being the lowercased string and the value being the normal (as-is) version.
    with open('strings.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            v = line
            k = line.lower()
            string_hash.set(k, v)

    # Print the hashtable (debug_print)
    print('String hash table:')
    string_hash.debug_print()

    # Do two lookups with `get()`: 'indian meal moth' and 'orb-weaving spiders (banded garden spider)'.
    lookups = ['indian meal moth', 'orb-weaving spiders (banded garden spider)']
    print('\nString lookups:')
    for key in lookups:
        val = string_hash.get(key)
        print(val)


    # Create a GuidHashtable.
    # Add each guid in `guids.txt` with the key being the lowercased string and the value being the normal (as-is) version. Note that your **key should be calculated from the number parts in the guid**, not simply from the string representation of the guid.
    # Print the hashtable (debug_print)
    # Do two lookups with `get()`: '00000158691797bd77464883000a001800388ccf' and '00000158691797bd7746488c000a001991ef0003'.


    # Create an ImageHashtable.
    # Add each image in `images.txt` with the key being the filename and the value being filename.  Note that your **key should be calculated from the bytes of the file**, not from the filename.
    # Print the hashtable (debug_print)
    # Do two lookups with `get()`: 'document.png' and 'security_keyandlock.png'.

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
