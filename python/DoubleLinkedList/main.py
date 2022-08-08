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
        # Observation: this method could only change the head (not the tail)
        # Case insert existing Node
        if (nodeToInsert.prev != None or nodeToInsert.next != None):
            nodeToInsert = self.utilExtractNode(nodeToInsert)
        # Case: stand-alone Node
        # Base case: Head
        if position == 1:
            nodeToInsert.next = self.head
            self.head.prev = nodeToInsert
            self.head = nodeToInsert
        else:
            runnerNode = self.head
            idx = 1
            while (idx < position - 1):
                idx += 1
                if runnerNode.next == None:
                    return  # position input is longer than list.length
                runnerNode = runnerNode.next
            # Insert Node
            nodeToInsert.prev = runnerNode
            nodeToInsert.next = runnerNode.next
            runnerNode.next.prev = nodeToInsert  # 'runnerNode.next' is always != Null
            runnerNode.next = nodeToInsert

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

    node4 = Node(4)
    node3 = Node(3)
    node2 = Node(2)
    node1 = Node(1)

    mylist.setTail(node1)
    mylist.setTail(node2)
    mylist.setTail(node3)
    mylist.setTail(node4)

    mylist.traverseForward()
    mylist.traverseBackward()

    node5 = Node(5)
    node6 = Node(6)

    mylist.insertAfter(node2, node5)
    mylist.traverseForward()
    mylist.traverseBackward()

    mylist.insertAtPosition(2, node6)
    mylist.traverseForward()
    mylist.traverseBackward()

    node6_2 = Node(6)
    mylist.setTail(node6_2)
    mylist.traverseForward()
    mylist.traverseBackward()

    mylist.removeNodesWithValue(4)
    mylist.traverseForward()
    mylist.traverseBackward()

    mylist.removeNodesWithValue(6)
    mylist.traverseForward()
    mylist.traverseBackward()

    mylist.remove(node1)
    mylist.traverseForward()
    mylist.traverseBackward()
