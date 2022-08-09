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
        # Case: Insert Existing node (Move node)
        if (nodeToInsert.prev != None or nodeToInsert.next != None):
            nodeToInsert = self.utilExtractNode(nodeToInsert)
        # Case: Insert new stand-alone node
        # Sub-Case: node is Head
        if self.head == node:
            nodeToInsert.next = node
            node.prev = nodeToInsert
            self.head = nodeToInsert
        # Other-Case: list.length >= 2
        else:
            runnerNode = self.head
            while runnerNode.next != node:
                if runnerNode.next == None:
                    # Case: reached end of List and node does not exist in LinkedList
                    return
                runnerNode = runnerNode.next

            # Insert node
            nodeToInsert.prev = runnerNode
            nodeToInsert.next = runnerNode.next
            runnerNode.next.prev = nodeToInsert
            runnerNode.next = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Case: Insert Existing node (Move node)
        if (nodeToInsert.prev != None or nodeToInsert.next != None):
            nodeToInsert = self.utilExtractNode(nodeToInsert)
        # Insert stand-alone node
        # Case I: nodeAfter is tail
        if node == self.tail:
            self.tail.next = nodeToInsert
            nodeToInsert.prev = self.tail
            self.tail = nodeToInsert
        else:
            # Case II: nodeAfter is any node of Linked List
            runnerNode = self.head
            while runnerNode != node:
                if runnerNode.next == None:
                    return
                runnerNode = runnerNode.next
            # Insert Node
            nodeToInsert.prev = runnerNode
            nodeToInsert.next = runnerNode.next
            if runnerNode.next != None:
                runnerNode.next.prev = nodeToInsert
            runnerNode.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Observation 1: this method could change head or tail
        # Observation 2: Order matters, to re-insert existing nodes check before neighbours node before extract nodeToInsert
        if position == 1:
            self.setHead(nodeToInsert)
            return

        idx = 1
        runnerNode = self.head
        while (idx != position or runnerNode != None):
            runnerNode = runnerNode.next
            idx += 1

        if runnerNode == None:
            self.setTail(nodeToInsert)
            return

        # Insert other position
        self.insertBefore(runnerNode, nodeToInsert)

    def removeNodesWithValue(self, value):
        runner = self.head
        while (runner != None):
            nextNode = runner.next  # Potentially None
            if runner.value == value:
                _ = self.utilExtractNode(runner)
            runner = nextNode

    def remove(self, node):
        _ = self.utilExtractNode(node)

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
