'''
zipping annoys me and I couldnt sleep so...
'''


def unEqualZipandFlatten(ArrayofArrays):
    # in python if zipping unequal lists, you end up stopping at the first end point,
    # thus to stop that, let's use map and NONE, finally, let's flatten it too with
    # just list comprhension rather than itertools.chain()

    # Notice use of *args so can have as many nested lists as needed

    print 'Zip normal means you stop too soon!\n', zip(*ArrayofArrays)

    c = map(None, *ArrayofArrays)

    print 'Map with NONE instead to get all values:', c
    print 'Now replace NONE with empty str: ', [[a if a is not None else '' for a in n] for n in c]

    def flatten(nested):
        return [e for l in nested for e in l]

    v = flatten(c)
    print 'flattened: ', v
    print 'lets filter out the NONEs', filter(None, v)


if __name__ == '__main__':
    unEqualZipandFlatten(((1, 2, 3), ('a', 'b'), ['grapes', 'bananas', 'oranges', 'limes']))
