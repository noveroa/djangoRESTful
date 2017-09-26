from FBPrep.Stacks import Queue, DoubleQueue


def hottater(players, time):
    rollcall = Queue()
    for person in players:
        rollcall.enqueue(person)
    while rollcall.size() > 1:
        for i in xrange(time):
            rollcall.enqueue(rollcall.dequeue())
        print 'Sorry!: ', rollcall.dequeue()

    return rollcall.dequeue()


names = ['Aileen', 'Breanne', 'Caitlin', 'Molly', 'Ryon', 'John', 'Willa']


# print  hottater(names, 8)

def palindrome(word):
    chars = DoubleQueue()
    equal = True
    for w in word: chars.addRear(w.lower())
    chars.printMe()

    while chars.size() > 1 and equal:
        if chars.popFront() != chars.popRear():
            equal = False
    return equal


print palindrome('raCecar')
