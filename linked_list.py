
import pdb
from node import Node
class Linked_list(object):
    def __init__(self,iterable = None):
        self.head = None
        self.tail = None
        self.size = 0
        if iterable is not None:
            for item in iterable:
                self.append(item)
    ''' function to happend to the end and update the size'''
    def append(self,item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length()
       
    '''function to happend to the front and update the size'''
    def prepend(self,new_node):
        new_node.next = self.head
        self.head = new_node
        self.length()

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        self.size = count

    def find(self,quality):
        current_node = self.head
        while current_node is not None:
            if quality(current_node.data):
                return current_node.data
            current_node = current_node.next
        
        return None

    def delete(self,item):
        
        current_node = self.head
        previous_node = current_node

        #delete first node and update size
        if item == self.head.data:
            self.head = self.head.next
            self.length()
            return item

        #delete last node and update size
        elif item == self.tail.data:
            while current_node is not None:
                if current_node.next.data == self.tail.data:
                    current_node.next = None
                    self.tail = current_node
                    self.length()
                    return item
                current_node = current_node.next

        #delte node in the middle & update size
        else:
            while current_node is not None:
                if current_node.data == item:
                    current_node = current_node.next
                    previous_node.next = current_node
                    self.length()
                    return item

                previous_node = current_node
                current_node = current_node.next
        return None

        
