import unittest
from linked_list import Linked_List
import pdb

class linked_list_test(unittest.TestCase):
    
    def test_init_head_tail(self):
        
        head = Linked_List('a')
        tail = head
        assert(head.data == tail.data)
    
    def test_add_node(self):
        head = Linked_List(1)
        tail = head

        #create new node
        new_node = Linked_List(2)

        #set tail to the new node
        tail = new_node

        #set head next to the tail
        head.next = tail

        assert(head.next.data == tail.data)




if __name__ == '__main__':
    unittest.main()




