
from double_linked_list import DoubleLinkedList
from node import Node
import unittest
array = [1,2,3,4,5,6]
class doubleLinkedList(unittest.TestCase):
    def test_append_dll(self):
        head = None
        tail = None
        for item in array:
            new_node = Node(item)
            if head is None:
                head = new_node
                tail = head
            else:
                tail.next = new_node
                new_node.prev = tail
                tail = new_node
        assert head.data == 1
        assert tail.data == 6
        assert head == head.next.prev
        assert tail == tail.prev.next
        assert head.prev is None
        assert tail.next is None

    def test_append_implementation(self):
        dll = DoubleLinkedList(array)
        assert dll.head.data == 1
        assert dll.tail.data == 6
        assert dll.head.prev is None
        assert dll.tail.next is None
        assert dll.head == dll.head.next.prev
        assert dll.tail == dll.tail.prev.next
    
    def test_prepend(self):
        head = None
        tail = None

        for item in array:
            new_node = Node(item)
            if head is None:
                head = new_node
                tail = new_node
            else:
                head.prev = new_node
                new_node.next = head
                head = new_node
        assert head.data == 6
        assert tail.data == 1
        assert head.prev is None
        assert tail.next is None
        assert head.next.prev == head
        assert tail.prev.next == tail
    
    def test_prepend_implementation(self):
        dll = DoubleLinkedList()
        assert dll.prepend(1) == 1
        assert dll.prepend(2) == 2
        assert dll.prepend(3) == 3
        assert dll.head.data == 3
        assert dll.tail.data == 1
        assert dll.head.next.prev == dll.head
        assert dll.tail.prev.next == dll.tail
        assert dll.tail.next is None
        assert dll.head.prev is None 
        assert dll.size == 3

    def test_delete(self):
        dll = DoubleLinkedList(array)
        item1 = 1
        item2 = 4
        item3 = 6

        current = dll.head

        #delete first item
        if dll.head.data == item1:
            dll.head = dll.head.next
            dll.head.prev = None

        #delete last item
        if dll.tail.data == item3:
            dll.tail = dll.tail.prev
            dll.tail.next = None

        #delete item in the middle of dll
        while current is not None:
           
            if current.data == item2:
                current.prev.next = current.next
                current.next.prev = current.prev
            current = current.next
                
        assert dll.head.data == 2
        assert dll.tail.data == 5
        assert dll.head.next.next.data == 5
        assert dll.tail.prev.data == 3

    def test_delete_implementation(self):
        dll = DoubleLinkedList(array)
        assert dll.delete(1) == 1
        assert dll.delete(4) == 4
        assert dll.delete(6) == 6
        assert dll.size == 3
        assert dll.head.data == 2
        assert dll.tail.data == 5
        assert dll.tail.prev.data == 3
        assert dll.head.next.data == 3
    
    def test_find(self):
        dll = DoubleLinkedList(array)
        assert dll.find(lambda item: item == 1) == 1
        assert dll.find(lambda item: item > 1) == 2
        assert dll.find(lambda item: item < 1) is None
        assert dll.find(lambda item: item == 10) is None
    
    def test_replace(self):
        dll = DoubleLinkedList(array)
        item1 = 5
        item2 = 10
        item3 = 45
        assert dll.replace(item1,1) == item1
        assert dll.replace(item2,4) == item2
        assert dll.replace(item3,6) == item3
        assert dll.replace(34,90) is None

        
       
                




                
                




