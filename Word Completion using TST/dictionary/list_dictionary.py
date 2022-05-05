from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. List-based dictionary implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ListDictionary(BaseDictionary):

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # create list data structure 
        self.dictList = []  
        for i in words_frequencies:
            self.dictList.append([i.word, i.frequency])


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
         # For each word in dictList
        for i in self.dictList:
            # Remove leading and trailing whitespaces from word, and compare to each entry in dictList @ index 0. When found, return frequency
            if i[0] == word:
                return i[1]
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        foundFlag = True
        
        for i in self.dictList:
            if i[0] == word_frequency.word:
                foundFlag = False
        
        if foundFlag: 
            self.dictList.append([word_frequency.word, word_frequency.frequency]) 
        return foundFlag
        

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        deleteFlag = True
        for i in self.dictList:
            if i[0] == word.strip():
                self.dictList.remove(i)
                return True

        # If not found, return False
        return False

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        allList = [i for i in self.dictList if i[0].startswith(prefix_word)]
        sortedList = sorted(allList, key=lambda item: item[1], reverse=True)[:min(3,len(allList))]
        
        

        # Convert list items from shortList to WordFrequency object, and append to finalList
        
        return [WordFrequency(item[0], item[1]) for item in sortedList]
         
