
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




