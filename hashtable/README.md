# Assignment: Hashtable

In this assignment, you'll create four primary classes: an abstract Hashtable superclass and three concrete subclasses of it.  The three subclasses define one additional method, `get_hash()`, which returns the hash key for the data type being supported.  You'll support three types of keys: strings, guids, and image bytes.  The three classes are as follows:

```
                Hashtable (abstract class)
                 /           |           \
                /            |            \
    StringHashtable    GuidHashtable    ImageHashtable
```

Our hashtable implementation only allows one value under a given key.  If a second value is added with an existing key, the previous value is removed.

## The Hash Function

Each of your subclasses will define the `get_hash()` method differently.  In all cases, it returns a number in the 0-9 range, which is the length of your bucket list (i.e. the index of the bucket the key will be assigned to).  In all cases, you do not have to process the entire contents of the keys -- just process enough to get a uniform distribution.

Your hash should be stable for a given key, meaning that repeated calls with the same key will always return the same hash index.

* The StringHashtable should compute the index based on the contents of the string.
* The GuidHashtable should compute the index based on the given guid.  Each guid is composed of 40 hex charaters: 0-15 is the millisecond the guid was created, 16-23 is a counter that resets at a random number at each change in millisecond, and 24-39 is the IP address where the guid was created.
* The ImageHashtable should compute the index based on the given image bytes.  The parameter will be sent in as the filename of the graphic, but your method needs to open the image, read (some of or all of) the bytes, and calculate the index based on the bytes of the image.

A significant portion of your grade on this assignment will come from your hash logic.  In each case, try to implement a clever, fast, effective hash function that will load your list of buckets as uniformly as possible.  Do not use the built-in hash functionality of your language, and do not use the built-in `md5` or `sha` algorithms.  The logic needs to be your creation.

## Constructor

In your constructor, create an array of 10 buckets.  We're using a low number so debugging and printing is easier (even though it will load up fairly quickly).  Initialize each bucket as a BinaryTree from your last assignment.  If you didn't get the binary tree assignment finished, ask another student or the teacher for an implementation.

In other words, your buckets do not start with `null` values.  They start with 10 empty binary trees.


## Methods

The methods you need to support are given below.  Note that the `get_hash()` method is abstract in the superclass.

```
Hashtable class:
    Constructor
    set(key, value)
    get(key)
    remove(key)
    get_hash(key)

StringHashtable class (Hashtable subclass):
    get_hash(key)

GuidHashtable class (Hashtable subclass):
    get_hash(key)

ImageHashtable class (Hashtable subclass):
    get_hash(key)

```


## Debug Printing

Create a `debug_print()` method for debugging and grading purposes.  This method should print the index followed by the values in each bucket.  An example is the following:

```
0: 00000158691797bd77464872000a0018001b000c, 00000158691797bd7746487c000a001800388ccf, 00000158691797bd77464886000a001800388ccf, 00000158691797bd77464890000a001991ef0003
1: 00000158691797bd77464873000a0018001b000c, 00000158691797bd7746487d000a001800388ccf, 00000158691797bd77464887000a001991ef0003, 00000158691797bd77464891000a001991ef0003
2: 00000158691797bd77464874000a0018001b000c, 00000158691797bd7746487e000a001800388ccf, 00000158691797bd77464888000a001991ef0003, 00000158691797bd77464892000a001991ef0003
3: 00000158691797bd77464875000a001800388ccf, 00000158691797bd7746487f000a001800388ccf, 00000158691797bd77464889000a001991ef0003, 00000158691797bd77464893000a001991ef0003
4: 00000158691797bd77464876000a001800388ccf, 00000158691797bd77464880000a001800388ccf, 00000158691797bd7746488a000a001991ef0003, 00000158691797bd77464894000a001991ef0003
5: 00000158691797bd77464877000a001800388ccf, 00000158691797bd77464881000a001800388ccf, 00000158691797bd7746488b000a001991ef0003, 00000158691797bd77464895000a001991ef0003
6: 00000158691797bd7746486e000a0018001b000c, 00000158691797bd77464878000a001800388ccf, 00000158691797bd77464882000a001800388ccf, 00000158691797bd7746488c000a001991ef0003
7: 00000158691797bd7746486f000a0018001b000c, 00000158691797bd77464879000a001800388ccf, 00000158691797bd77464883000a001800388ccf, 00000158691797bd7746488d000a001991ef0003
8: 00000158691797bd77464870000a0018001b000c, 00000158691797bd7746487a000a001800388ccf, 00000158691797bd77464884000a001800388ccf, 00000158691797bd7746488e000a001991ef0003
9: 00000158691797bd77464871000a0018001b000c, 00000158691797bd7746487b000a001800388ccf, 00000158691797bd77464885000a001800388ccf, 00000158691797bd7746488f000a001991ef0003
```



## Main Method

Your main method should do the following:

1. Create a StringHashtable.
1. Add each bug in `strings.txt` with the key being the lowercased string and the value being the normal (as-is) version.
1. Print the hashtable (debug_print)
1. Do two lookups with `get()`: 'indian meal moth' and 'orb-weaving spiders (banded garden spider)'.
1. Create a GuidHashtable.
1. Add each guid in `guids.txt` with the key being the lowercased string and the value being the normal (as-is) version. Note that your **key should be calculated from the number parts in the guid**, not simply from the string representation of the guid.
1. Print the hashtable (debug_print)
1. Do two lookups with `get()`: '00000158691797bd77464883000a001800388ccf' and '00000158691797bd7746488c000a001991ef0003'.
1. Create an ImageHashtable.
1. Add each image in `images.txt` with the key being the filename and the value being filename.  Note that your **key should be calculated from the bytes of the file**, not from the filename.
1. Print the hashtable (debug_print)
1. Do two lookups with `get()`: 'document.png' and 'security_keyandlock.png'.

Run your program and send the output to `output.txt`.



## Submitting the Assignment

Submit your code and output file as a single zip file (even if they are not together in your actual program).  Submit this file on Learning Suite.
