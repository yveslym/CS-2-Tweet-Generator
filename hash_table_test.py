from double_linked_list import DoubleLinkedList
import unittest

def add_tuplegram(histogram, word):
    if word not in histogram:
        count = 1
        histogram[1] += count
    else:
        histogram[1] += 1
    return (word:histogram[1])
def create_histogram(text_file):
    histogram = []
    list_of_words = open(text_file).read().split()
    for word in list_of_words:
        histogram.append(add_tuplegram(histogram, word))
    return histogram


class HashTableTest(unittest.TestCase):
    def test_init_hash_table(self):
        size = 5
        bucket = DoubleLinkedList()
        ash_table = []

        x = 0
        while x<size:
            ash_table.append(bucket)
            x += 1

        assert ash_table != None
        assert ash_table[0] != None
        assert ash_table[1] != None
        assert ash_table[2] != None
        assert ash_table[3] != None
        assert ash_table[4] != None

    def test_insert(self):
        
