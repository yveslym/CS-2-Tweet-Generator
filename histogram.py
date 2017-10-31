import sys
import pprint
def histogram(source_text):

    histogram_dict = {"":0}

    open_files = ('/Users/yveslym/Documents/CS-2-Tweet-Generator/%s' % source_text)
    list_of_word = open(open_files).read().split()

    unique_list = list(set(list_of_word))
    print('number if element in list_of_word: %s' % len(list_of_word))

    print('number if element in unique_list: %s' % len(unique_list))

    for word in unique_list:
        count = 0
        for next_word in list_of_word:
            if word == next_word:
                count += 1
        histogram_dict[word] = count
    for word in histogram_dict:
        if histogram_dict[word] > 10:
            print(word+'\t'+str(histogram_dict[word]))


if __name__ == "__main__":
    histogram('Letter-That-Have-Helped-Me-by-Various.txt')
