# Approach:
- First I have created a class Node for crating each node.
- Then again I have created a DoublyLinkedlist class For adding the nodes to the doublyLinked list.
- Then I have created individual functions inside this doublylinked list class for inserting,deleting and tarversing.
- When the objects are created for these two classes we can acsess the methods inside the classes and preform the operations given.

# Documentation:

- class Node => This class defines a node for doublyLinked list
  - ##### Attributes:
    - data : This Stores the data that should be present in the each node.
    - next : This is the pointer to the next node.
    - prev : This is the pointer to the previous node.
  - ##### Methods:
    - __init__(self,data) :
      - This method initializes a new node with the given data.
      - This nethod also sets the pointers for both next and prev to **None**
- class DoublyLinkedlist => This class defines the structure and operations for a doubly linked list.
  - ##### Attributes:
    - head: Points to the first node of the list.
    - tail: Points to the last node of the list.
  - ##### Methods:
    - insert_beginning(self, data):
      - Inserts a new node with the given data at the beginning of the list.
      - If the list is empty, the new node becomes both the head and tail.
      - Otherwise, the new node is inserted before the current head, and the head pointer is updated.

    - insert_ending(self, data):
      - Inserts a new node with the given data at the end of the list.
      - If the list is empty, the new node becomes both the head and tail.
      - Otherwise, the new node is inserted after the current tail, and the tail pointer is updated.

    - insert_at_specificnode(self, node, data):
      - Inserts a new node with the given data at a specific position (node).
      - If the position is invalid (<= 0), an error message is printed.
      - The function iterates through the list until the given position is reached.
      - If the position exceeds the list length, an error message is printed.
      - Otherwise, the new node is inserted at the correct position, and the surrounding nodes' next and prev pointers are adjusted.
      - If the node is inserted at the beginning, the head pointer is updated.

    - delete_at_beginning(self):
      - Deletes the first node (the head) of the list.
      - If the list is empty, an error message is printed.
      - If the list contains only one node, both head and tail are set to None.
      - Otherwise, the head pointer is updated to point to the next node, and the previous first node is disconnected.

    - delete_at_end(self):
      - Deletes the last node (the tail) of the list.
      - If the list is empty, an error message is printed.
      - If the list contains only one node, both head and tail are set to None.
      - Otherwise, the tail pointer is updated to the previous node, and the last node is disconnected.

    - delete_at_specificnode(self, node):
      - Deletes the node at the specified position (node).
      - If the position is invalid (<= 0), an error message is printed.
      - The function iterates through the list until the given position is reached.
      - If the position exceeds the list length, an error message is printed.
      - Otherwise, the node is deleted, and the surrounding nodes' next and prev pointers are adjusted.
      - If the node to be deleted is the head, the head pointer is updated.
      - If the node to be deleted is the tail, the tail pointer is updated.

    - traversal_forward(self):
      - Traverses the list from the head to the tail and prints the data of each node in a single line.

    - traversal_backward(self):
      - Traverses the list from the tail to the head and prints the data of each node in a single line.
