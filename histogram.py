import sys
import pprint
def histogram(source_text):

    histogram_dict = {"":0}

    open_files = ('/Users/yveslym/Documents/CS-2-Tweet-Generator/%s' % source_text)
    list_of_word = open(open_files).read().split()

    return list_of_word


def unique_word(list_of_word):
    unique_list = ['']#list(set(list_of_word))
    count = 0
    print("while looping #%s" % count)
    for word in list_of_word:
        print("for looping #%s" % count)
        count +=1
        index = 0
        uniques = True
        while index < len(unique_list):
            if word == unique_list[index]:
                uniques = False

            index += 1
        if uniques == True:
            unique_list.append(word)

    return len(unique_list)

def list_histogram(list_of_word):

    histogram_list = []
    unique_list = list(set(list_of_word))
    for word in unique_list:
        count = 0
        for next_word in list_of_word:
            if word == next_word:
                count += 1
        new_histogram = [word,count]
        histogram_list.append(new_histogram)

    print("\n\n Histogram list print word repeated more than 200 times: ")
    for word in histogram_list:
        if word[1] > 200:
            print(word[0]+'\t'+str(word[1]))

    print("end of the list")


def tuple_histogram(list_of_word):
    unique_list = list(set(list_of_word))
    histogram_tuple = []
    for word in unique_list:
        count = 0
        for next_word in list_of_word:
            if word == next_word:
                count += 1
        new_histogram = (word,count)
        histogram_tuple.append(new_histogram)

    print("\n\n Histogram tuple print word repeated more than 500 times: ")
    for word in histogram_tuple:
        if word[1] > 1000:
            print(word[0]+'\t'+str(word[1]))



def frequency(search_word, list_of_word):

    unique_list = list(set(list_of_word))
    print('number if element in list_of_word: %s' % len(list_of_word))

    print('number if element in unique_list: %s' % len(unique_list))

    histogram_dict = {"":0}

    #count the frequence of word and add register as dictionary

    for word in unique_list:
        count = 0
        for next_word in list_of_word:
            if word == next_word:
                count += 1
        histogram_dict[word] = count
    for word in histogram_dict:
        if word == search_word:
            print(word+'\t'+str(histogram_dict[word]))
            continue
    print("end of the list")



if __name__ == "__main__":
    param = sys.argv[1:]
    word = param[0]
    text_file = param[1]
    print(param)
    print(word)
    print(text_file)
    frequency(word,histogram(text_file))
    list_histogram(histogram(text_file))
    tuple_histogram(histogram(text_file))
