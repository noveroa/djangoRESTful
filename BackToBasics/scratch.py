import numpy as np


def unique(a=[1, 3, 4, 5, 2, 3, 4, 6, 6, 7, 8]):
    print ('The array {0}: {1}'.format(type(a), a))

    print ('Make it a set, then recast as list: {}'.format(list(set(a))))

    print ('Numpy unique: {}'.format(np.unique(a)))

    print('List comprehension, keeps the order {}'.format([x for i, x in enumerate(a) if x not in a[0:i]]))


## Fibonacci sequence
# a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is
# the series 1, 1, 2, 3, 5, 8, etc.

def fibLoop(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def fibRecursion(n):
    if n == 1 or n == 2:
        return 1
    return fibRecursion(n - 1) + fibRecursion(n - 2)


memo = {}


def fib(n):
    if n <= 2:
        return 1
    if not n in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


def grid(n=10):
    for i in range(n):
        for j in range(n):
            print ('({0}, {1})'.format(i, j)),
        print('\n')


def orderedPairs(n=10):
    # runtime STILL O(N**2)
    for i in range(n):
        for j in range(i, n):
            print ('({0}, {1})'.format(i, j)),
        print('\n')


# unique()
# print(fibLoop(5))
# print(fibRecursion(5))
# print(fib(5))
# orderedPairs()

def intersec(a=[1, 2, 4, 12, 15, 17, 20, 21], b=[2, 5, 7, 12, 17, 24]):
    a, b = sorted(a), sorted(b)

    intersection = [i for i in b if i in a]
    print intersection

    # Function prints Intersection of arr1[] and arr2[]
    # m is the number of elements in arr1[]
    # n is the number of elements in arr2[]
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:
            j += 1
        else:
            print(b[j])
            j += 1
            i += 1

    print (zip(a, b))
    print zip(b, a)


# intersec()

def performOps(A):
    m = len(A)

    n = len(A[0])
    B = []
    for i in xrange(len(A)):
        B.append([0] * n)
        for j in xrange(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    return B


A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


def runB():
    B = performOps(A)

    for i in xrange(len(B)):
        for j in xrange(len(B[i])):
            print B[i][j],


# runB()
def hammingWeight(n):
    # Write a function that takes an unsigned integer
    # and returns the number of '1' bits it has (also known as the Hamming weight).
    #
    # For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011,
    # so the function should return 3.
    #
    result = bin(n).count("1")
    return result


print(hammingWeight(11))


#
def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


print(anagramSolution2('abcde', 'edcba'))


def anabanana(s1, s2):
    s1, s2 = list(s1), list(s2)
    s1.sort()
    s2.sort()
    return s1 == s2


print(anabanana('abcde', 'edfba'))
