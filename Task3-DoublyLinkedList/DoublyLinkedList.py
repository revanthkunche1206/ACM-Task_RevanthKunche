class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_ending(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_specificnode(self, node, data):
        if node <= 0:
            print("Invalid position!")
            return
        new_node = Node(data)
        current = self.head
        i = 1

        while current is not None and i < node:
            current = current.next
            i += 1
        
        if current is None: 
            print("Position exceeds the list length!")
        else:
            new_node.next = current
            new_node.prev = current.prev
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node

            if current == self.head:
                self.head = new_node
            if current == self.tail:
                self.tail = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("Empty list")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_end(self):
        if self.tail is None:
            print("Empty list")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_at_specificnode(self, node):
        if node <= 0:
            print("Invalid position!")
            return
        current = self.head
        i = 1
        while current and i < node:
            current = current.next
            i += 1

        if current is None: 
            print("Position exceeds the list length!")
        else:
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev

            if current == self.head:
                self.head = current.next 
            if current == self.tail:
                self.tail = current.prev 
    def traversal_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def traversal_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

DLL = DoublyLinkedList()

DLL.insert_beginning(5)
DLL.insert_beginning(4)
DLL.insert_beginning(3)
DLL.insert_beginning(2)
DLL.insert_beginning(1)

DLL.insert_beginning(10)
DLL.insert_ending(15)

DLL.insert_at_specificnode(3, 30)

DLL.delete_at_specificnode(5)

DLL.traversal_backward()
DLL.traversal_forward()

