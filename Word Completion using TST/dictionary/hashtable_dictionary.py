from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. Hash-table-based dictionary.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class HashTableDictionary(BaseDictionary):

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # Create dictionary data-structure
        self.hash = {}
        for pair in words_frequencies:
            self.add_word_frequency(pair)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        freq = 0
        if word in self.hash:
            freq =self.hash.get(word)
        return freq

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        inserted = False
        if self.search(word_frequency.word) == 0:
            inserted = True
            self.hash[word_frequency.word] = word_frequency.frequency
        return inserted


    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        deleted = False
        if self.search(word) > 0:
            deleted = True
            del self.hash[word]
        return deleted
        

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        allDict = {key:val for key, val in self.hash.items() if key.startswith(prefix_word) and val>0}
        sortedDict = dict(sorted(allDict.items(), key=lambda item: item[1], reverse=True))
        finalList=[WordFrequency(sortedWord, sortedDict[sortedWord]) for sortedWord in list(sortedDict)[:min(3,len(sortedDict))]]
        return finalList
