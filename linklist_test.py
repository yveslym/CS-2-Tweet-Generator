import unittest
from linked_list import Linked_list
from node import Node
import pdb

array = [1, 2, 3, 4, 5, 6]
class linked_list_test(unittest.TestCase):
    def test_init_array(self):
        ll = Linked_list(array)
        assert(ll.head.data == 1)
        assert(ll.head.next.data == 2)
        assert(ll.tail.data == 6)
    def test_init_head_tail(self):
        
        head = Node(1)
        tail = head
        assert(head.data == tail.data)
    
    def test_add_new_node(self):
        head = Node(1)
        tail = head

        #create new node
        new_node = Node(2)

        #set tail to the new node
        tail = new_node

        #set head next to the tail
        head.next = tail
        assert(head.next.data == tail.data)
    
    def test_append_to_the_end(self, node = None):
        
        head = Node(1)
        tail = head
        new_node = Node(2)
        new_node2 = Node(3)

        #append first node
        tail.next = new_node
        tail = new_node

        #append second node
        tail.next = new_node2
        tail = new_node2


        assert(head.next.data == new_node.data)
        assert(head.next.next.data == new_node2.data == tail.data)

    def test_append_to_the_front(self):
        head = Node(1)
        new_node =  Node(2)

        new_node.next = head
        head = new_node

        assert(head.data == 2)
        assert(head.next.data == 1)

    def test_linked_listlength(self):
        
        #init node
        head = Node(1)
        tail = head
        node = Node(2)
        node2 = Node(3)
        
       
       #append first node
        tail.next = node
        tail = node

        #append second node
        tail.next = node2
        tail = node2

        
        #count list
        count = 0
        current = head
       
        while current:
            count += 1
            #pdb.set_trace()
            current = current.next
        
        assert(count == 3)

    def test_find(self):
       
        ll = Linked_list(array)
        #pdb.set_trace() 
        assert ll.find(lambda item: item == 1) == 1
        assert ll.find(lambda item: item < 2 ) == 1
        assert ll.find(lambda item: item > 3) == 4
        assert ll.find(lambda item: item == 7) is None

    def test_delete_node_in_middle(self):
        ll = Linked_list(array)
        item = 4
        current_node = ll.head
        previous_node = current_node
        while current_node is not None:
            
            if current_node.data == item:
                current_node = current_node.next
                previous_node.next = current_node
                
            previous_node = current_node
            current_node = current_node.next

        assert ll.find(lambda item: item == 4) is None

    def test_delete_last_node(self):
        ll = Linked_list(array)
        item = 6
        current_node = ll.head
        previous_node = current_node

        while current_node is not None:
            
            if current_node is not None and current_node.next is None:
                ll.tail = previous_node
            previous_node = current_node
            current_node = current_node.next
        assert (ll.tail.data == 5)

    def test_delete_first_item(sef):
        ll = Linked_list(array)
        item = 1

        if item == ll.head.data:
            ll.head = ll.head.next
        assert (ll.head.data == 2)

    def test_delete_none_existing_item(sef):
        ll = Linked_list(array)
        current_node = ll.head
        previous_node = current_node
        item = 9
        find = False
        while current_node is not None:

            if current_node.data == item:
                current_node = current_node.next
                previous_node.next = current_node
                find = True

            previous_node = current_node
            current_node = current_node.next

        assert(find == False)

    def test_delete_implementation(self):
        
        ll = Linked_list(array)

        assert ll.delete(1) == 1
        assert (ll.delete(4)) == 4
        assert (ll.delete(6)) == 6
        assert (ll.delete(9)) == None
        assert(ll.size == 3)

    def test_replace(self):
        
        ll = Linked_list(array)
        newItem = Node(8)
        replaceItem = 6

        current = ll.head
        previous = current

        while current:
            if current.data == replaceItem:
                current = current.next
                previous.next = newItem
                newItem.next = current
                break
            previous = current
            current = current.next
        assert (ll.find(lambda item: item == 8)) == 8
        assert (ll.find(lambda item: item == 6)) == None

    def test_replace_implementation(self):
        ll = Linked_list(array)
        assert ll.replace(8,1) == 8 #replace first element
        assert ll.replace(9,3) == 9 #replace item in the middle
        assert ll.replace(10,6) == 10 #replace last item
        assert ll.replace(0,45) == None #replace item that doesn't exist
        assert ll.size == 6 #size doesn't change
    
    def test_prepend_implementation(self):
        ll = Linked_list()
        assert ll.prepend(1) == 1
        assert ll.prepend(2) == 2
        assert ll.head.data == 2
        assert ll.tail.data == 1
        assert ll.size == 2

        
                


        

        

        
            
        
       
        

if __name__ == '__main__':
    unittest.main()
    




