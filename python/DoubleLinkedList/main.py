class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Time O(1) | Space(1)
    def setHead(self, node):
        # Base case
        if self.head == None:
            self.head = node
            self.tail = node
            return
        # Case: existing node
        if node.prev != None or node.next != None:
            self.remove(node)
        # Default case: stand-alone node
        self.head.prev = node
        node.next = self.head
        self.head = node

    # Time O(1) | Space(1)
    def setTail(self, node):
        # Base case
        if self.tail == None:
            self.tail = node
            self.head = node
            return
        # Case existing node
        if node.prev != None or node.next != None:
            self.remove(node)
        # Default case: stand-alone node
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    # Time O(1) | Space O(1)
    def insertBefore(self, node, nodeToInsert):
        # Case: Insert Existing node (Move node)
        if (nodeToInsert.prev != None or nodeToInsert.next != None):
            self.remove(nodeToInsert)
        # Case: Insert new stand-alone node
        # Sub-Case: node is Head
        if self.head == node:
            nodeToInsert.next = node
            node.prev = nodeToInsert
            self.head = nodeToInsert
        # Other-Case: list.length >= 2
        else:
            # Insert node
            nodeToInsert.prev = node.prev
            nodeToInsert.next = node
            node.prev.next = nodeToInsert   # At this point node.prev is always != null
            node.prev = nodeToInsert

    # Time O(1) | Space O(1)
    def insertAfter(self, node, nodeToInsert):
        # Case: Insert Existing node (Move node)
        if (nodeToInsert.prev != None or nodeToInsert.next != None):
            self.remove(nodeToInsert)
        # Insert stand-alone node
        # Case I: node is tail
        if node == self.tail:
            self.tail.next = nodeToInsert
            nodeToInsert.prev = self.tail
            self.tail = nodeToInsert
        else:
            # Case II: node is any position of Linked List
            nodeToInsert.prev = node
            nodeToInsert.next = node.next
            if node.next != None:
                node.next.prev = nodeToInsert
            node.next = nodeToInsert

    # Time O(n) | Space O(1)
    def insertAtPosition(self, position, nodeToInsert):
        # Observation 1: this method could change head or tail
        # Observation 2: Order matters, to re-insert existing nodes check before neighbours node before extract nodeToInsert
        if position == 1:
            self.setHead(nodeToInsert)
            return

        idx = 1
        runnerNode = self.head
        # Time worst case: O(n)
        while (idx != position and runnerNode != None):
            runnerNode = runnerNode.next
            idx += 1

        if runnerNode == None:
            self.setTail(nodeToInsert)
            return

        # Insert in other position:  O(1)
        self.insertBefore(runnerNode, nodeToInsert)

    # Time O(n) | Space O(1)
    def removeNodesWithValue(self, value):
        runner = self.head
        while (runner != None):
            nextNode = runner.next  # Potentially None
            if runner.value == value:
                self.remove(runner)
            runner = nextNode

    # Time O(1) | Space I(1)
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        # Check potential case of Head
        if prevNode != None:  # Node is Not Head
            prevNode.next = nextNode
        else:  # Node is Head
            self.head = nextNode

        # Check: potential case of Tail
        if nextNode != None:  # Node is Not Tail
            nextNode.prev = prevNode
        else:  # Node is Tail
            self.tail = prevNode

        # Make original node stand-alone
        node.prev = None
        node.next = None

    # Time O(n) | Space O(1)
    def containsNodeWithValue(self, value):
        runner = self.head
        while (runner != None):
            if runner.value == value:
                return True
            runner = runner.next
        return False

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

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    mylist.setHead(node1)
    mylist.insertAfter(node1, node2)
    mylist.insertAfter(node2, node3)
    mylist.insertAfter(node3, node4)
    mylist.insertAfter(node4, node5)
    mylist.insertAfter(node5, node6)
    mylist.insertAfter(node6, node7)

    mylist.traverseForward()
    print("-------")
    mylist.insertAtPosition(7, node1)
    mylist.traverseForward()

    print("-------")
    mylist.insertAtPosition(1, node1)
    mylist.traverseForward()

    print("-------")
    mylist.insertAtPosition(2, node1)
    mylist.traverseForward()

    print("-------")
    mylist.insertAtPosition(3, node1)
    mylist.traverseForward()

    print("-------")
    mylist.insertAtPosition(4, node1)
    mylist.traverseForward()

    print("-------")
    mylist.insertAtPosition(5, node1)
    mylist.traverseForward()

    print("-------")
    mylist.insertAtPosition(6, node1)
    mylist.traverseForward()
