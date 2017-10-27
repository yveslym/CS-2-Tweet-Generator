import sys

def reverse_word(word):
    reversed_word = []
    ''' turn the string into list '''
    array = list(word)

    ''' reverse by getting the index of the last character to the first'''
    index = len(word)-1
    while index >= 0:
        reversed_word.append(array[index])
        index -= 1
    return reversed_word

    ''' join the list into string'''
def print_reversed(reverse_words):
    word = "".join(reverse_words)
    print(word)

if __name__=="__main__":
    word = sys.argv[1]
    print_reversed(reverse_word(word))
