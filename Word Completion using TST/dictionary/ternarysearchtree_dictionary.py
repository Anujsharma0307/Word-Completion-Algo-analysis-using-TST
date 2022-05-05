from turtle import left
from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
from dictionary.node import Node
import queue



# ------------------------------------------------------------------------
# This class is required to be implemented. Ternary Search Tree implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


class TernarySearchTreeDictionary(BaseDictionary):

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        #Create initial node
        self.tree = Node()
        #Add words to the tree
        for word_frequency in words_frequencies:
            self.add_word_frequency(word_frequency)
    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        #Get topmost node
        iter_node = self.tree
        len_word = len(word) 
        i = 0
        while i < len_word and iter_node != None:
            curr_letter = word[i]            
            #Check for direction to traverse    
            if curr_letter < iter_node.letter:
                iter_node = iter_node.left
            elif curr_letter > iter_node.letter:
                iter_node = iter_node.right
            else:
                i+=1
                if(i<len_word):
                    iter_node = iter_node.middle
            

        # check if word is found
        # return frequency word is found
        # else return 0 
        frequency = -1
        if i < len_word or iter_node == None or not iter_node.end_word:
            frequency = 0
        else:
            frequency = iter_node.frequency
        return frequency

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        #Get topmost node
        iter_node = self.tree
        word = word_frequency.word
        len_word = len(word) 
        i = 0
        ret_flag = False
        while i < len_word:
            curr_letter = word[i]

            #Check if node has a letter
            if iter_node.letter == None:
                iter_node.letter = curr_letter

            #Check for direction to traverse
            if curr_letter < iter_node.letter:
                if iter_node.left == None:
                    iter_node.left = Node()
                iter_node = iter_node.left
            elif curr_letter > iter_node.letter:
                if iter_node.right == None:
                    iter_node.right = Node()
                iter_node = iter_node.right
            else:
                #Check if word is ended
                if i == len_word - 1:
                    #Check if word already exists
                    if iter_node.end_word == False:
                        iter_node.end_word = True
                        iter_node.frequency = word_frequency.frequency
                        ret_flag = True
                else:
                    if iter_node.middle == None:
                        iter_node.middle = Node()
                    iter_node = iter_node.middle
                i+=1
                
        return ret_flag

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        #Get topmost node
        iter_node = self.tree
        len_word = len(word) 
        i = 0
        while i < len_word and iter_node != None:
            curr_letter = word[i]            
            #Check for direction to traverse    
            if curr_letter < iter_node.letter:
                iter_node = iter_node.left
            elif curr_letter > iter_node.letter:
                iter_node = iter_node.right
            else:
                i+=1
                if(i<len_word):
                    iter_node = iter_node.middle
            
        # check if word is found
        if i < len_word or iter_node == None or not iter_node.end_word:
            return False
        else:
            iter_node.end_word = False
            iter_node.frequency = 0
            return True

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        print('----')
        cur_node = self.tree 
        len_word = len(word) 
        #Get topmost node
        iter_node = self.tree
        len_word = len(word) 
        i = 0
        while i < len_word and iter_node != None:
            curr_letter = word[i]   
            #Check for direction to traverse    
            if curr_letter < iter_node.letter:
                iter_node = iter_node.left
            elif curr_letter > iter_node.letter:
                iter_node = iter_node.right
            else:
                i+=1
                if(i<len_word):
                    iter_node = iter_node.middle

        if i < len_word or iter_node == None:
            return []

        iter_list = queue.Queue()
        iter_list.put([iter_node, word])
        all_word = []
        first = True
        while not iter_list.empty():
            temp_node, curr_word = iter_list.get()
            #Check if a word
            if temp_node.end_word:
                all_word.append([temp_node, curr_word])
            
            #Add rest
            if temp_node.left != None:
                if not first:
                    iter_list.put([temp_node.left, curr_word[:-1]+temp_node.left.letter])
            if temp_node.right != None: 
                if not first:
                    iter_list.put([temp_node.right, curr_word[:-1]+temp_node.right.letter])
            if temp_node.middle != None:
                iter_list.put([temp_node.middle, curr_word + temp_node.middle.letter])
            first = False

        ret_words = []
        # If words exist

        if all_word != []:
            all_word.sort(key=lambda x: x[0].frequency, reverse=True) # Sort by frequency (descending order)
            ret_words = [ WordFrequency(c_word,c_node.frequency)  for c_node, c_word in all_word[:min(3,len(all_word))]]
                

        # Return top 3 highest frequency words
        return ret_words