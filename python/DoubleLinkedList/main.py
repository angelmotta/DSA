class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def utilExtractNode(self, node):
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
        return node

    def setHead(self, node):
        # Base case
        if self.head == None:
            self.head = node
            self.tail = node
            return
        # Case: existing node
        if node.prev != None or node.next != None:
            node = self.utilExtractNode(node)
        # Default case: stand-alone node
        self.head.prev = node
        node.next = self.head
        self.head = node

    def setTail(self, node):
        # Base case
        if self.tail == None:
            self.tail = node
            self.head = node
            return
        # Case existing node
        if node.prev != None or node.next != None:
            node = self.utilExtractNode(node)
        # Default case: stand-alone node
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

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
            print("<- ", end="")
            print(node.value, end="")
            print(" -> ", end="")
            node = node.next
        print("")

    def traverseBackward(self):
        print("traverseBackward:")
        node = self.tail
        while(node != None):
            print("<- ", end="")
            print(node.value, end="")
            print(" -> ", end="")
            node = node.prev
        print("")


# Start execution
if __name__ == '__main__':
    mylist = DoublyLinkedList()

    node3 = Node(3)
    node2 = Node(2)
    node1 = Node(1)

    mylist.setTail(node3)
    mylist.setTail(node2)
    mylist.setTail(node1)

    mylist.traverseForward()
    mylist.traverseBackward()

    mylist.setTail(node2)
    mylist.traverseForward()
    mylist.traverseBackward()
