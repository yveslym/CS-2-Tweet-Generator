from node import Node

class DoubleLinkedList(object):
    def __init__(self,iterable = None):
        self.head = None
        self.tail = None
        self.size = 0
        if iterable is not None:
            for item in iterable:
                self.append(item)
    
    '''function to append new element and update size'''
    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.size += 1
            return item
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size += 1
            return item
        return None
            

