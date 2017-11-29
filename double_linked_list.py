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
    
    def prepend(self,item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return item
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return item
        return None

    def delete(self, item):
        #delete head
        if self.head.data == item:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return item
        
        #delete tail
        elif self.tail.data == item:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return item
        #delete item in the middle
        else:
            current = self.head
            while current is not None:
                if current.data == item:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                    return item
                current = current.next
        return None

    def find(self,quality):
        current_node = self.head
        while current_node is not None:
            if quality(current_node.data):
                return current_node.data
            current_node = current_node.next
        return None

    def replace(self,new_item,old_item):
        current_node = self.head
        while current_node is not None:
            if current_node.data == old_item:
                current_node.data = None
                current_node.data = new_item
                return new_item
            current_node = current_node.next
        return None
        


                    

