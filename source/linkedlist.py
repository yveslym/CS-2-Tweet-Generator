
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
            self.size += 1
            return item
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
            return item

    '''function to happend to the front and update the size'''

    def prepend(self,item):

        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.size += 1
            return item
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return item

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
            self.size -= 1
            return item

        #delete last node and update size
        elif item == self.tail.data:
            while current_node is not None:
                if current_node.next.data == self.tail.data:
                    current_node.next = None
                    self.tail = current_node
                    self.size -= 1
                    return item
                current_node = current_node.next

        #delte node in the middle & update size
        else:
            while current_node is not None:
                if current_node.data == item:
                    current_node = current_node.next
                    previous_node.next = current_node
                    self.size -= 1
                    return item

                previous_node = current_node
                current_node = current_node.next
        return None

    def replace(self,new_item, old_item):
        new_node = Node(new_item)

        current_node = self.head
        previous_node = current_node

        while current_node is not None:
            if current_node.data == old_item:
                current_node.data = new_item
                return
                # current_node = current_node.next
                # previous_node.next = new_node
                # new_node.next = current_node
                # return new_item
            previous_node = current_node
            current_node = current_node.next
        return None

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None
