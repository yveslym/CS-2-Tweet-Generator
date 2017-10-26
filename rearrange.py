import random
import sys

def rearrange(lists):
    rearranged_list = []

    index = 0
    while index != len(lists):
        random_index = random.randint(0, len(lists)-1)
        rearranged_list.append(lists.pop(random_index))
    return rearranged_list

def print_new_list(rearranged_list):
    new_list = " ".join(rearranged_list)
    print(new_list)

if __name__=="__main__":
    current_input = sys.argv[1:]
    
    print_new_list(rearrange(current_input))
