import random
import sys


def generate_word(number):
    path = "/usr/share/dict/words"
    index = 0
    list_of_word = []
    while index < number:
        open_file = open(path).read().split()
        random_word = open_file[random.randint(0, len(open_file)-1)]
        list_of_word.append(random_word)
        index += 1
    return list_of_word

def print_list(list_of_word):
    new_list = " ".join(list_of_word)
    print(new_list)

if __name__=="__main__":
    number = int(sys.argv[1])
    print_list(generate_word(number))
