class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Base case
        if self.head == None:
            self.head = node
            self.tail = node
            return
        # Case: stand-alone node
        if (node.next == None and node.prev == None):
            initialHead = self.head
            node.next = initialHead
            self.head = node
            initialHead.prev = node
        # TODO: Case existing node

    def setTail(self, node):
        pass

    def insertBefore(self, node, nodeToInsert):
        pass

    def insertAfter(self, node, nodeToInsert):
        pass

    def insertAtPosition(self, position, nodeToInsert):
        pass

    def removeNodesWithValue(self, value):
        pass

    def remove(self, node):
        pass

    def containsNodeWithValue(self, value):
        pass

    def traverseForward(self):
        node = self.head
        while(node != None):
            print(node.value)
            node = node.next
        print("")

    def traverseBackward(self):
        node = self.tail
        while(node != None):
            print(node.value)
            node = node.prev
        print("")


# Start execution
if __name__ == '__main__':
    mylist = DoublyLinkedList()

    node3 = Node(3)
    node2 = Node(2)
    node1 = Node(1)

    mylist.setHead(node3)
    mylist.setHead(node2)
    mylist.setHead(node1)

    mylist.traverseForward()
    mylist.traverseBackward()
