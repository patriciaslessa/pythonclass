# a = 2
# b = 3

def sorted_number(a,b,c):
    """
    >>> sorted_number(1,2,3)
    1 2 3
    >>> sorted_number(1,3,2)
    1 2 3
    >>> sorted_number(2,1,3)
    1 2 3
    >>> sorted_number(2,3,1)
    1 2 3
    >>> sorted_number(3,1,2)
    1 2 3
    >>> sorted_number(3,2,1)
    1 2 3
    """
    if (a < b) and (b < c):
        print(a,b,c)
    elif (a < c) and (c < b):
        print(a,c,b)
    elif (b < a) and (a < c):
        print(b,a,c)
    elif (b < c) and (c < a):
        print(b,c,a)
    elif (c < a) and (a < b):
        print(c,a,b)
    else:
        print(c,b,a)

import doctest
doctest.testmod(verbose=True)

# x = 4
# y = 3
# z = 2

#sorted_two_number(x,y)
