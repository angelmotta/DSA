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
        # Case: existing node
        if node.prev != None or node.next != None:
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            if nextNode != None:
                nextNode.prev = prevNode
            else:
                self.tail = prevNode
            # Make node stand-alone
            node.prev = None
            node.next = None
        # Default case: stand-alone node
        self.head.prev = node
        node.next = self.head
        self.head = node

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
        print("traverseForward:")
        node = self.head
        while(node != None):
            print(node.value)
            node = node.next
        print("")

    def traverseBackward(self):
        print("traverseBackward:")
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

    mylist.setHead(node2)
    mylist.traverseForward()
    mylist.traverseBackward()
