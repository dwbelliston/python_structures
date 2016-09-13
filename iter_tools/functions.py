from itertools import chain, izip, islice, tee, imap, count, cycle,repeat
from itertools import dropwhile, takewhile, ifilter, ifilterfalse
from itertools import groupby

'''This is very similar to adding lists together,
but it will return an itertools chain object which
computes values when asked for making it better suited
for larger lists.'''
chainer = list(chain([1,2,3,4,5], [5,4,3,2,1]))
print(chainer)


lister = list(izip([1,2,3,4,5], [5,4,3,2,1]))
for i in lister:
    print(i)

''' The first parameter is an iterable object. The
second parameter is a starting index. The third parameter
is the end index. The final parameter is a step or a
number to skip after each iteration.'''
for i in islice(range(20), 0, 20, 4):
    print(i)


'''The first is an iterable and the second is the number
of copies you'd like to make. With Python's multiple
assignment, we can assign each created iterable to a
different variable. As we can see, each iterable that we
create can be iterated through separately giving us a few
instances to play with in the case that we exhaust one.'''
i1, i2, i3 = tee(range(10), 3)
print(list(i1))
print(list(i1))


def lambme(x):
    return [x, x*x]

mapper = imap(lambda x: lambme(x), range(11))
print(list(mapper))



for number, letter in izip(count(0, 9), ['a', 'b', 'c', 'd', 'e', 'f']):
    print('{} {}'.format(number, letter))

for number, letter in izip(cycle(range(2)), ['a', 'b', 'c', 'd', 'e', 'f']):
    print('{} {}'.format(number, letter))

print(list(repeat('yaya', 2)))

'''drop everything until condition is false, then take that
(thats why the 1 is still there)'''
dropper = dropwhile(lambda x: x < 10, [1, 4, 6, 7, 11, 34, 66, 100, 1])
print(list(dropper)) # 11, 34, 66, 100, 1

'''take it until the condition is false'''
taker = takewhile(lambda x: x < 10, [1, 4, 6, 7, 11, 34, 66, 100, 1])
print(list(taker)) # 1, 4, 6, 7


print list(ifilter(lambda x: x < 10, [1, 4, 6, 7, 11, 34, 66, 100, 1]))
# [1, 4, 6, 7, 1]


print list(ifilterfalse(lambda x: x < 10, [1, 4, 6, 7, 11, 34, 66, 100, 1]))
# [11, 34, 66, 100]


peeplo = [
    ('dan', 87),
    ('erik', 95),
    ('jason', 79),
    ('erik', 97),
    ('dan', 100)
]

peeplo.sort(key=lambda x: x[0])
grouper = groupby(peeplo, key=lambda x:x[0])
grouper = {key: map(lambda x:x[1], value) for key, value in grouper}
print(grouper)




with open('testers.txt', 'a') as file:
    file.writelines(list(repeat('yaya.\n', 2)))














#
