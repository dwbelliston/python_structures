# Remember, an Iterable is just an object capable of returning its members one at a time.

# generators are used to generate a series of values
# yield is like the return of generator functions
# The only other thing yield does is save the "state" of a generator function
# A generator is just a special type of iterator
# Like iterators, we can get the next value from a generator using next()
# for gets values by calling next() implicitly

def simple():
    yield 1
    yield 2
    yield 3

og = simple()

print(og)
print(next(og))
print(next(og))
print(next(og))


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1
