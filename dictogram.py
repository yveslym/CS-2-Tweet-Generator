from __future__ import division, print_function
import pdb

class Dictogram(dict):
    def __init__(self, text_file = None):
        self.types = 0
        self.tokkens = 0
        self.words_list = None
        if text_file is not None:
            self.words_list = self._get_list_of_words(text_file)
        if self.words_list is not None:
            #pdb.set_trace()
            for word in self.words_list:
                self._check_word(word)

    ''' function to add word in the dictogram following a certain condition
        if the word already exist in the dictogram increment is frequence
        by one each time we count it
        if it's the first time increment the self.types'''
    def _check_word(self,word, count = 1):
        if word not in self:
            self[word] = count
            self.types += 1
        else:
            self[word] += 1
        self.tokkens += 1

    ''' Function to return the list of word from file'''
    def _get_list_of_words(self, text_file):
        return open(text_file).read().split()

if __name__ == "__main__":
    dictogram = Dictogram("word.txt")
    print("tokkens: "+str(dictogram.tokkens))
    print("types: "+str(dictogram.types))
