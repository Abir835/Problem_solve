class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push_begining(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def push_end(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            self.head.next = None
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(new_data)

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


llist = LinkedList()
llist.push_end(20)
llist.push_end(4)
llist.push_end(15)
llist.push_end(85)

print("Given linked list")
llist.printList()
llist.reverse()
print("\nReversed linked list")
llist.printList()
