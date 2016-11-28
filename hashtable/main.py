#!/usr/bin/env python3
import os
import sys
import argparse
import re
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
    guid_hash = GuidHashtable()
    # Add each guid in `guids.txt` with the key being the lowercased string and the value being the normal (as-is) version. Note that your **key should be calculated from the number parts in the guid**, not simply from the string representation of the guid.
    with open('guids.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            v = line
            k = line.lower()
            guid_hash.set(k, v)

    # Print the hashtable (debug_print)
    print('\nGuid hash table:')
    guid_hash.debug_print()

    # Do two lookups with `get()`: 'indian meal moth' and 'orb-weaving spiders (banded garden spider)'.
    lookups = ['00000158691797bd77464883000a001800388ccf', '00000158691797bd7746488c000a001991ef0003']
    print('\nGuid lookups:')
    for key in lookups:
        val = guid_hash.get(key)
        print(val)


    # Create an ImageHashtable.
    image_hash = ImageHashtable()
    # Add each image in `images.txt` with the key being the filename and the value being filename.  Note that your **key should be calculated from the bytes of the file**, not from the filename.
    with open('images.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            image_hash.set(line.lower(), line)

    # Print the hashtable (debug_print)
    print('\nImage hash table:')
    image_hash.debug_print()

    # Do two lookups with `get()`: 'document.png' and 'security_keyandlock.png'.
    lookups = ['document.png', 'security_keyandlock.png']
    print('\nImage lookups:')
    for line in lookups:
        with open('images/{}'.format(line), 'rb') as i:
            k = i.read()
            k = str(len(k))
            val = image_hash.get(line)
            print(val)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
