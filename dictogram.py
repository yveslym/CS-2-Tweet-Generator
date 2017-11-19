# from __future__ import division, print_function
# import pdb
#
# class Dictogram(dict):
#     def __init__(self, text_file = None):
#         self.types = 0
#         self.tokkens = 0
#         self.words_list = None
#         if text_file is not None:
#             self.words_list = self._get_list_of_words(text_file)
#         if self.words_list is not None:
#             #pdb.set_trace()
#             for word in self.words_list:
#                 self._check_word(word)
#
#     ''' function to add word in the dictogram following a certain condition
#         if the word already exist in the dictogram increment is frequence
#         by one each time we count it
#         if it's the first time increment the self.types'''
#     def _check_word(self,word, count = 1):
#         if word not in self:
#             self[word] = count
#             self.types += 1
#         else:
#             self[word] += 1
#         self.tokkens += 1
#
#     ''' Function to return the list of word from file'''
#     def _get_list_of_words(self, text_file):
#         return open(text_file).read().split()
#
#     def frequency(self,word):
#         if word in self:
#             return self[word]
#         else:
#             return 0
#
#
# if __name__ == "__main__":
#     hictogram = Dictogram("project-guthemberg.txt")
#     print("tokkens: "+str(hictogram.tokkens))
#     # for word in dictogram:
#     #     if dictogram[word] > 500:
#     #         print(word+' '+str(dictogram[word]))
#     print("types: "+str(hictogram.types))
#     print("frequency of word 'spirit': "+str(hictogram.frequency('spirit')))


from histogram import Histogram
import pdb
from pprint import pprint

class Dictogram(dict):
    def __init__(self, text_file = None):


        self.histogram = None
        if text_file is not None:
            self.histogram = Histogram(text_file)
            self.create_dictogram()

    def create_dictogram(self):
        if self.histogram is not None:
            for index,word in enumerate(self.histogram.words_list):
                if index + 1 > len(self.histogram.words_list)-1:
                     return
                next_word = self.histogram.words_list[index+1]

                if word not in self:
                    self[word] = {}
                    histogram = Histogram()
                    #pdb.set_trace()
                    #histogram = {next_word:0}

                    self[word] = histogram.add(next_word)
                else:
                    self.histogram = self[word]
                    self[word] = self.histogram.add(next_word)





                #
                # if index + 1 > len(self.histogram.words_list)-1:
                #     return
                # next_word = self.histogram.words_list[index+1]
                # next_histogram = self.histogram.get_histogram(next_word)
                #
                # if word in self and next_histogram not in self[word]:
                #     self[word].append(next_histogram)
                # else:
                #     self[word] = []
                #     self[word].append(self.histogram.get_histogram(next_word))
                #


if __name__ == "__main__":
     dictogram = Dictogram("fish.txt")
     # pprint('histogram: %s' % dictogram.histogram)
     # print('\n\n')
     pprint('dictogram: %s' % dictogram)


     # print("tokkens: "+str(hictogram.tokkens))
     # print("types: "+str(hictogram.types))
     # print("frequency of word 'spirit': "+str(hictogram.frequency('spirit')))
