class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node at the begining of the linked list
    def prepand(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    # Add a node at the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
    
    # Add a node anywhere on the linked list using the previous node
    def insert(self, data, prev_data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.data != prev_data:
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    # Print the linked list
    def display(self):
        current_node = self.head
        llstring = ''
        while current_node:
            llstring +=str(current_node.data) + '-->'
            current_node = current_node.next
        print(llstring)

    # Remove a node
    def remove(self, data):
         current_node =  self.head
         prev_node = None
         while current_node is not None:
            if current_node.data == data:
                if prev_node is None:
                    # If the node to be deleted is the head, update head
                    self.head = current_node.next
                else:
                    # If the node to be deleted is not the head, update the previous node's next pointer
                    prev_node.next = current_node.next
            # Move prev and temp pointers forward
            prev_node = current_node
            current_node = current_node.next

        



myLinkedList = LinkedList()
myLinkedList.append(20)
myLinkedList.append(30)
myLinkedList.display()
myLinkedList.insert(10,20)
myLinkedList.display()
myLinkedList.remove(20)
myLinkedList.display()




