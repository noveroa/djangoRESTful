import os


def walkpath(path):
    # Walking through a directory without using os.walk!

    for f in os.listdir(path):
        sdirectory = os.path.join(path, f)

        if os.path.isdir(sdirectory):
            walkpath(sdirectory)

        else:
            print sdirectory


def zipper():
    # Just practice with the behavior of zipping in general
    A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
    A1 = range(10)
    A2 = sorted([i for i in A1 if i in A0])
    A3 = sorted([A0[s] for s in A0])
    A4 = [i for i in A1 if i in A3]
    A5 = {i: i * i for i in A1}
    A6 = [[i, i * i] for i in A1]

    print A0, 'don\'\t know!  a dictionary!'
    print A1, '0-9'
    print A2, 'none'
    print A3, '1,2,3,4,5'
    print A4, '1,2,3,4,5'
    print A5, '{0:0, 1:1^2, ..9:81}'
    print A6, '[[0,0]...[9,81]]'


def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)


# Use *args when we aren't sure how many arguments are going to be passed to a function,
# or if we want to pass a stored list or tuple of arguments to a function.
# **kwargs is used when we dont know how many keyword arguments will be passed to a function,
# or it can be used to pass the values of a dictionary as keyword arguments.
# The identifiers args and kwargs are a convention, you could also use *bob and **billy but
# that would not be wise.

def playArgKwargGame():
    def argkwarg(*args, **kwargs):
        print(args, kwargs)

    def argkwarg2(arg1, arg2, *args, **kwargs):
        print(arg1, arg2, args, kwargs)

    l = [1, 2, 3]
    t = (4, 5, 6)
    d = {'a': 7, 'b': 8, 'c': 9}

    argkwarg()
    argkwarg(1, 2, 3)  # (1, 2, 3) {}
    argkwarg(1, 2, 3, "groovy")  # (1, 2, 3, 'groovy') {}
    argkwarg(a=1, b=2, c=3)  # () {'a': 1, 'c': 3, 'b': 2}
    argkwarg(a=1, b=2, c=3, zzz="hi")  # () {'a': 1, 'c': 3, 'b': 2, 'zzz': 'hi'}
    argkwarg(1, 2, 3, a=1, b=2, c=3)  # (1, 2, 3) {'a': 1, 'c': 3, 'b': 2}

    argkwarg(*l, **d)  # (1, 2, 3) {'a': 7, 'c': 9, 'b': 8}
    argkwarg(*t, **d)  # (4, 5, 6) {'a': 7, 'c': 9, 'b': 8}
    argkwarg(1, 2, *t)  # (1, 2, 4, 5, 6) {}
    argkwarg(q="winning", **d)  # () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
    argkwarg(1, 2, *t, q="winning", **d)  # (1, 2, 4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}

    argkwarg2(1, 2, 3)  # 1 2 (3,) {}
    argkwarg2(1, 2, 3, "groovy")  # 1 2 (3, 'groovy') {}
    argkwarg2(arg1=1, arg2=2, c=3)  # 1 2 () {'c': 3}
    argkwarg2(arg1=1, arg2=2, c=3, zzz="hi")  # 1 2 () {'c': 3, 'zzz': 'hi'}
    argkwarg2(1, 2, 3, a=1, b=2, c=3)  # 1 2 (3,) {'a': 1, 'c': 3, 'b': 2}

    argkwarg2(*l, **d)  # 1 2 (3,) {'a': 7, 'c': 9, 'b': 8}
    argkwarg2(*t, **d)  # 4 5 (6,) {'a': 7, 'c': 9, 'b': 8}
    argkwarg2(1, 2, *t)  # 1 2 (4, 5, 6) {}
    argkwarg2(1, 1, q="winning", **d)  # 1 1 () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
    argkwarg2(1, 2, *t, q="winning", **d)  # 1 2 (4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}


# A decorator is a special kind of function that either takes a function and returns a function,
# or takes a class and returns a class. The @ symbol is just syntactic sugar that allows you to
# decorate something in a way that's easy to read.
def time_this(original_function):
    def new_function(*args, **kwargs):
        import datetime
        before = datetime.datetime.now()
        x = original_function(*args, **kwargs)
        after = datetime.datetime.now()
        print "Elapsed Time = {0}".format(after - before)
        return x

    return new_function


@time_this
def func_a(stuff):
    import time
    time.sleep(3)


def NodeStuff():
    class Node(object):
        def __init__(self, sName):
            self._lChildren = []
            self.sName = sName

        def __repr__(self):
            return "<Node '{}'>".format(self.sName)

        def append(self, *args, **kwargs):
            self._lChildren.append(*args, **kwargs)

        def print_all_1(self):
            print(self)
            for oChild in self._lChildren:
                oChild.print_all_1()

        def print_all_2(self):
            def gen(o):
                lAll = [o, ]
                while lAll:
                    oNext = lAll.pop(0)
                    lAll.extend(oNext._lChildren)
                    yield oNext

            for oNode in gen(self):
                print(oNode)

    oRoot = Node("root")
    oChild1 = Node("child1")
    oChild2 = Node("child2")
    oChild3 = Node("child3")
    oChild4 = Node("child4")
    oChild5 = Node("child5")
    oChild6 = Node("child6")
    oChild7 = Node("child7")
    oChild8 = Node("child8")
    oChild9 = Node("child9")
    oChild10 = Node("child10")

    oRoot.append(oChild1)
    oRoot.append(oChild2)
    oRoot.append(oChild3)
    oChild1.append(oChild4)
    oChild1.append(oChild5)
    oChild2.append(oChild6)
    oChild4.append(oChild7)
    oChild3.append(oChild8)
    oChild3.append(oChild9)
    oChild6.append(oChild10)

    oRoot.print_all_1()  # depth
    oRoot.print_all_2()  # width generator


# Profiling and efficiency!
import cProfile, random


def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i < 0.5]
    return [i * i for i in l2]


def f2(lIn):
    l1 = [i for i in lIn if i < 0.5]
    l2 = sorted(l1)
    return [i * i for i in l2]


def f3(lIn):
    l1 = [i * i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i < (0.5 * 0.5)]


lIn = [random.random() for i in range(100000)]


def profiler():
    cProfile.run('f1(lIn)')
    cProfile.run('f2(lIn)')
    cProfile.run('f3(lIn)')


if __name__ == '__main__':
    print 'hey there, unhash which funciton you want to run'
# path = sys.argv[1]
##   walkwithout os.walk()
# walkpath(path)
#   ziptest
## zipper()
#   kwarg stuff
# playArgKwargGame()
#   Looking at Tree structures, generators
# NodeStuff()

#   testing profiling efficiency
# Most to least efficient: f2, f1, f3.To prove Python profiling package
# profiler()
