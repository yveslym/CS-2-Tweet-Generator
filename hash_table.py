from double_linked_list import DoubleLinkedList

class HashTable(object):
    def __init__(self):
        number_of_bucket = 5
        self.bucket = DoubleLinkedList()
        self.hash_table = []

        index = 0

        while index < number_of_bucket:
            self.hash_table.append(self.bucket)
            index += 1
            
