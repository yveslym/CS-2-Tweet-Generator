import unittest
from linked_list import Linked_List
import pdb

class linked_list_test(unittest.TestCase):
    
    def test_init_head_tail(self):
        
        head = Linked_List('a')
        tail = head
        assert(head.data == tail.data)
    
    def test_add_new_node(self):
        head = Linked_List(1)
        tail = head

        #create new node
        new_node = Linked_List(2)

        #set tail to the new node
        tail = new_node

        #set head next to the tail
        head.next = tail
        assert(head.next.data == tail.data)

    def test_length(self):
        head = Linked_List(1)
        node1 = Linked_List(2)
        node2 = Linked_List(3)
    
    def test_append_to_the_end(self, node = None):
        
        head = Linked_List(1)
        tail = head
        new_node = Linked_List(2)

        tail.next = new_node
        tail = new_node
        insert(head.next.data == tail.data)
         




if __name__ == '__main__':
    unittest.main()
    




