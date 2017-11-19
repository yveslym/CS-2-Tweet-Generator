# import sys
# import pprint
# import time
# from operator import itemgetter
# def histogram(source_text):
#
#     histogram_dict = {"":0}
#
#     open_files = ('/Users/yveslym/Documents/CS-2-Tweet-Generator/%s' % source_text)
#     list_of_word = open(open_files).read().split()
#
#     return list_of_word
#
#
# def unique_word(list_of_word):
#     # unique_list = ['']#list(set(list_of_word))
#     # count = 0
#     # print("while looping #%s" % count)
#     # for word in list_of_word:
#     #     print("for looping #%s" % count)
#     #     count +=1
#     #     index = 0
#     #     uniques = True
#     #     while index < len(unique_list):
#     #         if word == unique_list[index]:
#     #             uniques = False
#     #
#     #         index += 1
#     #     if uniques == True:
#     #         unique_list.append(word)
#     #
#     # return len(unique_list)
#     return list(set(list_of_word))
#
# def get_index_of_item(item, list_hist):
#     for index, item in enumerate(list_hist):
#         if list_hist[0] == item:
#             return index + 1
#     return -1
#
# def list_histogram(list_of_word):
#     histogram_list = []
#     types = []
#     # unique_list = list(set(list_of_word))
#
#     start = time.time()
#
#     for word in list_of_word:
#         if word not in types:
#             histogram_list.append([word, 1])
#             types.append(word)
#
#         else:
#             # all_words = list(map(itemgetter(0), histogram_list))
#             # i = all_words.index(word)
#             # print("word " + word)
#             i = get_index_of_item(word, histogram_list)
#             histogram_list[i][1] += 1
#
#     print(histogram_list)
#     return histogram_list
#
#     # finish = time.time()
#     # print("List of List histogram after looping takes: %s seconds" % (finish - start))
#     #
#     #
#     # print("\n\n Histogram list print word repeated more than 200 times: ")
#     # for word in histogram_list:
#     #     if word[1] > 200:
#     #         print(word[0]+'\t'+str(word[1]))
#     #
#     # print("end of the list")
#
#
# def tuple_histogram(list_of_word):
#     unique_list = list(set(list_of_word))
#     histogram_tuple = []
#     for word in unique_list:
#         count = 0
#         for next_word in list_of_word:
#             if word == next_word:
#                 count += 1
#         new_histogram = (word,count)
#         histogram_tuple.append(new_histogram)
#
#     print("\n\n Histogram tuple print word repeated more than 500 times: ")
#     for word in histogram_tuple:
#         if word[1] > 1000:
#             print(word[0]+'\t'+str(word[1]))
#
#
# def counts_list(histo):
#
#     count_list = []
#     tempList = []
#     frequence = []
#     index = 0
#     for word in histo:
#         frequence.append(word[1])
#
#     while index < len(frequence):
#
#         for word in histo:
#             if word[1] == frequence[index]:
#                 tempList.append(word[0])
#         new_count = [frequence[index],tempList]
#         count_list.append(new_count)
#         index += 1
#
#     for count in count_list:
#         if count[0] > 5000:
#             print("frequence %s: %s " % (count[0], count[1]))
#
#
#             #     if word[1] == count:
#             #         tempList.append(word[0])
#             #         index += 1
#             # count_list.append[count,tempList]
#             # tempList = []
#             # count += 1
#     # finish = time.time()
#     # print("List of List histogram after looping takes: %s seconds" % (finish - start))
#
#
#     # print("\n\n Histogram list print word repeated more than 200 times: ")
#     # for word in histogram_list:
#     #     if word[0] > 1000:
#     #         print(word[0]+'\t'+str(word[1]))
#
#
#
#
# def frequency(search_word, list_of_word):
#
#     unique_list = list(set(list_of_word))
#     print('number if element in list_of_word: %s' % len(list_of_word))
#
#     print('number if element in unique_list: %s' % len(unique_list))
#
#     histogram_dict = {"":0}
#
#     #count the frequence of word and add register as dictionary
#
#     for word in unique_list:
#         count = 0
#         for next_word in list_of_word:
#             if word == next_word:
#                 count += 1
#         histogram_dict[word] = count
#     for word in histogram_dict:
#         if word == search_word:
#             print(word+'\t'+str(histogram_dict[word]))
#             continue
#     print("end of the list")
#
#
#
# if __name__ == "__main__":
#     param = sys.argv[1:]
#     word = param[0]
#     text_file = param[1]
#
#
#     start = time.time()
#     list_of_words = histogram(text_file)
#     finish = time.time()
#     print("reading takes: %s " % (finish - start))
#
#     # start = time.time()
#     # frequency(word,list_of_words)
#     # finish = time.time()
#     # print("dictionnary histogram takes: %s seconds" % (finish - start))
#
#     start = time.time()
#     histo = list_histogram(list_of_words)
#     finish = time.time()
#     print("List of List histogram takes: %s seconds" % (finish - start))
#
#     # start = time.time()
#     # tuple_histogram(list_of_words)
#     # finish = time.time()
#     # print("List of tuple histogram takes: %s seconds" % (finish - start))
#
#     #counts_list(histo)

from __future__ import division, print_function
import pdb

class Histogram(dict):
    def __init__(self, text_file = None):
        self.types = 0
        self.tokkens = 0
        self.words_list = None
        if text_file is not None:
            self.words_list = self._get_list_of_words(text_file)
        if self.words_list is not None:
            #pdb.set_trace()
            for word in self.words_list:
                self.add(word)

    ''' function to add word in the dictogram following a certain condition
        if the word already exist in the dictogram increment is frequence
        by one each time we count it
        if it's the first time increment the self.types'''
    def add(self,word, count = 1):

        if word not in self:
            self[word] = count
            self.types += 1
        else:
            self[word] += 1
        self.tokkens += 1
        #pdb.set_trace()
        return {word:self[word]}

    ''' Function to return the list of word from file'''
    def _get_list_of_words(self, text_file):
        return open(text_file).read().split()

    def get_histogram(self, word):
        #pdb.set_trace()
        return {word:self[word]}

    def frequency(self,word):
        if word in self:
            return self[word]
        else:
            return 0
