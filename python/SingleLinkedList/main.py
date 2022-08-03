class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def print(self):
        print(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def push_back(self, data):
        newNode = Node(data)
        node = self.head
        # Base case
        if node == None:
            self.head = newNode
            return

        # Insert node at the end
        while (node.next != None):
            node = node.next

        # Insert new node
        node.next = newNode

    def traverse(self):
        node = self.head
        while(node != None):
            node.print()
            node = node.next
        print("")


def removeDuplicates(linkedList):
    # Base case: empty linkedList or It has only one element
    if linkedList.head == None or linkedList.head.next == None:
        return linkedList

    current = linkedList.head
    forewardNode = current.next
    while (forewardNode != None):
        if current.data == forewardNode.data:
            forewardNode = forewardNode.next
        else:
            current.next = forewardNode
            current = forewardNode
            forewardNode = forewardNode.next

    # Check edge case
    if current.next != None and current.data == current.next.data:
        current.next = None

    return linkedList


# Start execution
if __name__ == '__main__':
    myllist = LinkedList()
    #node1 = Node(1)
    #node2 = Node(2)
    #node3 = Node(3)

    #linkedList.head = node1
    #node1.next = node2
    #node2.next = node3

    # Test
    inputList = [1, 1, 1, 3, 4, 4, 4, 5, 6, 6]

    for elem in inputList:
        myllist.push_back(elem)

    myllist.traverse()

    myUniqueLlist = removeDuplicates(myllist)
    myUniqueLlist.traverse()
