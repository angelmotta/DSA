class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def print(self):
        print(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        node = self.head
        while(node != None):
            node.print()
            node = node.next


# Start execution
if __name__ == '__main__':
    linkedList = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    linkedList.head = node1
    node1.next = node2
    node2.next = node3

    linkedList.traverse()
