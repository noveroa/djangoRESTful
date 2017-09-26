class Node():
    def __init__(self, initdata=None, link=None, count=0):
        self.data = initdata
        self.link = link
        self.count = count

    def getData(self):
        return self.data

    def setData(self, newdata):
        self.data = newdata

    def getNext(self):
        return self.link

    def setNext(self, newNext):
        self.link = newNext


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def isEmpty(self):
        if self.head: return False

    def size(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.getNext()
        return count

    def insert(self, item):

        new = Node(item)

        new.setNext(self.head)
        self.head = new

    def search(self, query):
        cur = self.head
        f = True
        stp = False
        while cur and not stp and not f:
            if cur.getData() == query:
                f = True
            else:
                cur = cur.getNext()
        return 'Found? {0}'.format(f)

    def delete(self, query):
        cur = self.head
        prev = None
        while cur:
            if cur.getData() == query:
                print('todelete')
                if cur == self.head:
                    self.head = cur.getNext()
                else:
                    prev.setNext(cur.getNext())
                return cur

            prev = cur
            cur = cur.getNext()
        return None

    def printMe(self):
        cur = self.head
        while cur:
            print cur.getData(),
            cur = cur.getNext()

    def removeDups(self):
        cur = sec = self.head

        while cur and sec.getNext():
            if sec.getNext().data == cur.data:
                sec.setNext(sec.getNext().getNext())
            else:
                sec = sec.getNext()  # put this line in an else, to avoid skipping items
                cur = sec = cur.getNext()


class OrderedLL():
    def __init__(self, head=None):
        self.head = head

    def isEmpty(self):
        if self.head: return False

    def size(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.getNext()
        return count

    def insert(self, item):
        cur = self.head
        prev = None
        stp = False
        while cur and not stp:
            if cur.getData() > item:
                stp = True
            else:
                prev = cur
                cur = cur.getNext()

        new = Node(item)

        if prev:
            new.setNext(cur)
            prev.setNext(new)
        else:
            new.setNext(self.head)
            self.head = new

    def search(self, query):
        cur = self.head
        f = True
        stp = False
        while cur and not stp and not f:
            if cur.getData() == query:
                f = True
            elif cur.getData() > query:
                stp = True
            else:
                cur = cur.getNext()
        return 'Found? {0}'.format(f)

    def delete(self, query):
        cur = self.head
        prev = None
        while cur:
            if cur.getData() == query:
                print('todelete')
                if cur == self.head:
                    self.head = cur.getNext()
                else:
                    prev.setNext(cur.getNext())
                return cur

            prev = cur
            cur = cur.getNext()
        return None

    def printMe(self):
        cur = self.head
        while cur:
            print cur.getData(),
            cur = cur.getNext()

    def removeDups(self):
        cur = sec = self.head

        while cur and sec.getNext():
            if sec.getNext().data == cur.data:
                sec.setNext(sec.getNext().getNext())
            else:
                sec = sec.getNext()  # put this line in an else, to avoid skipping items
                cur = sec = cur.getNext()

    def insertONCE(self, item):
        cur = self.head
        prev = None
        stp = False
        while cur and not stp:
            if cur.getData() == item:
                cur.count += 1
                stp = True

            if cur.getData() > item:
                stp = True

            else:
                prev = cur
                cur = cur.getNext()

        new = Node(item)

        if prev:
            if prev.count == 0:
                new.setNext(cur)
                prev.setNext(new)
        else:
            new.setNext(self.head)
            self.head = new


            # ll = OrderedLL()
            # ll.insert(31)
            # ll.insert(77)
            # ll.insert(17)
            # ll.insert(93)
            # ll.insert(26)
            # ll.insert(26)
            # ll.insert(54)
            # ll.insert(54)
            #
            # print(ll.size())
            # print(ll.search(93))
            # print(ll.search(100))
            # ll.printMe()
            # ll.delete(31)
            # ll.printMe()
            # ll.removeDups()
            # print('\n')
            # ll.printMe()
