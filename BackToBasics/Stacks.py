class Stack():
    # LIFO
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def printMe(self):
        print self.items


# s = Stack()
#
# # s.push('hello')
# #
# # s.push('true')
# # s.printMe()
# # print(s.pop())
# # s.printMe()
#
class Queue():
    # FIFO
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):  # push()
        self.items.insert(0, item)

    def dequeue(self):  # pop()
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def printMe(self):
        print self.items


class DoubleQueue():
    # dequeue;  double-ended queue,
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):  # push()
        self.items.insert(0, item)

    def popFront(self):  # pop()
        return self.items.pop(0)

    def addRear(self, item):  # push()
        self.items.append(item)

    def popRear(self):  # pop()
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def printMe(self):
        print self.items

# d = DoubleQueue()
# print(d.isEmpty())
# d.addRear(4)
# d.addRear('dog')
# d.addFront('cat')
# d.addFront(True)
# print(d.size())
# print(d.isEmpty())
# d.addRear(8.4)
# print(d.popRear())
# print(d.popFront())
# d.printMe()
