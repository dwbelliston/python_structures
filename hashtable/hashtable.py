from abc import ABCMeta, abstractmethod
from tree import BTree


class Hashtable(metaclass=ABCMeta):
    def __init__(self):
        '''
        Create an array of 10 buckets
        '''
        self.buckets = [BTree() for i in range(10)]

    def set(self, key, value):
        index = self.get_hash(key)
        self.buckets[index].set(key, value)

    def get(self, key):
        index = self.get_hash(key)
        return self.buckets[index].get(key)

    def remove(self, key):
        pass

    def debug_print(self):
        for i, bucket in enumerate(self.buckets):
            print('{}: '.format(i), end='')
            bucket.print_values()
            print('')


    @abstractmethod
    def get_hash(self, key):
        '''returns the hash key for the data type being supported'''
        '''returns a number in the 0-9 range, index of the bucket the key will be assigned to'''
        pass


class StringHashtable(Hashtable):
    def get_hash(self, key):
        '''The StringHashtable should compute the index based on the contents of the string.'''
        # x = [ord(c) for c in key]
        return len(key) % 10


class GuidHashtable(Hashtable):
    def get_hash(self, key):
        random = int(key[16:24], 16)
        last = (str(random)[-1:])
        return int(last)


class ImageHashtable(Hashtable):
    def get_hash(self, key):
        index = None
        with open('images/{}'.format(key), 'rb') as i:
            k = i.read()
            k = str(len(k))
            index = int(k) % 1000 % 100 % 10
        return index
