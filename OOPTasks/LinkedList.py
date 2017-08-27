class Node(object):
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def getNext(self):
        return self.next

    def setNext(self, next_node):
        self.next = next_node

    def getPrev(self):
        return self.prev

    def setPrev(self, prev_node):
        self.prev = prev_node

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def get(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()

        if current is None:
            raise ValueError("Data is not in the list")

        return current.getData()

    def put(self, data):
        new = Node(data)
        new.setNext(self.head)
        self.head = new

    def delete(self, data):
        current = self.head
        found = False
        prev = None

        while not found:
            if current.getData() == data:
                found = True
            else:
                prev = current
                current = current.getNext()

            if prev is None:
                self.head = current.getNext()
            else:
                prev.setNext(current.getNext())

    def indexOf(self, data):
        current = self.head
        index = 0
        found = False

        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                index += 1
                current = current.getNext()

        if current is None:
            raise ValueError("Data is not in the list")

        return index

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count
