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

    def insert_value(self, data):
        self.head = None
        for data_ in data:
            self.push_end(data_)

    def count_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.count_length():
            raise Exception('invalid index')

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, data, index):
        if index < 0 or index >= self.count_length():
            raise Exception('invalid index')

        if index == 0:
            self.push_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data)
                node.next = itr.next
                itr.next = node
                break
            itr = itr.next
            count += 1


    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


llist = LinkedList()
# llist.push_end(20)
# llist.push_end(4)
# llist.push_end(15)
# llist.push_end(85)
#
# print("Given linked list")
# llist.printList()
# llist.reverse()
# print("\nReversed linked list")
llist.insert_value(['abir', 'haddu', 'guddu'])
print(llist.count_length())
# llist.remove_at(1)
print(llist.count_length())
llist.insert_at('hasan', 1)
llist.printList()
