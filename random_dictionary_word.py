import random
import sys


def generate_word(number):
    path = "/usr/share/dict/words"
    index = 0
    list_of_word = []
    open_file = open(path)
    all_words = open_file.read().split()
    while index < number:
        random_word = all_words[random.randint(0, len(all_words) - 1)]
        list_of_word.append(random_word)
        index += 1
    open_file.close()
    return list_of_word

def print_list(list_of_word):
    new_list = " ".join(list_of_word)
    print(new_list)

if __name__=="__main__":
    number = int(sys.argv[1])
    print_list(generate_word(number))
