import sys

def reverse_sentences(sentences):
    index = len(sentences)-1
    reverse = []
    while index >= 0:
        reverse.append(sentences[index])
        index -= 1
    return reverse

def print_reverse(reverse):
    sentence = " ".join(reverse)
    print(sentence)

if __name__=="__main__":
    sentence = sys.argv[1:]
    print_reverse(reverse_sentences(sentence))
