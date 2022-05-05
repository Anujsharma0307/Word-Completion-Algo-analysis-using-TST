import sys
from dictionary.node import Node
from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
from dictionary.list_dictionary import ListDictionary
from dictionary.hashtable_dictionary import HashTableDictionary
from dictionary.ternarysearchtree_dictionary import TernarySearchTreeDictionary
import timeit

def read_data():
    # read from data file to populate the initial set of points
    data_filename = "sampleData200k.txt"

    words_frequencies_from_file = []
    
    try:
        data_file = open(data_filename, 'r')
        for line in data_file:
            values = line.split()
            word = values[0]
            frequency = int(values[1])
            word_frequency = WordFrequency(word, frequency)  # each line contains a word and its frequency
            words_frequencies_from_file.append(word_frequency)
        data_file.close()
        return words_frequencies_from_file

    except FileNotFoundError as e:
        print("Data file doesn't exist.")

def create_dict(dict_type: str, word_frequency, sizes):
    # initialise search agent
    all_dicts = []
    agent: BaseDictionary = None
    for i in range(len(sizes)):
        if dict_type == 'list':
            agent = ListDictionary()
        elif dict_type == 'hashtable':
            agent = HashTableDictionary()
        elif dict_type == 'tst':
            agent = TernarySearchTreeDictionary()
        all_dicts.append(agent)    
    for itr in range(len(sizes)):
        all_dicts[itr].build_dictionary(word_frequency[:sizes[itr]])

    return all_dicts
        
def execute_command(line: str, agent):
    command_values = line.split()
    command = command_values[0]
    start_time = timeit.default_timer()
    # search
    if command == 'S':
        word = command_values[1]
        search_result = agent.search(word)
        if search_result > 0:
            print(f"Found '{word}' with frequency {search_result}\n")
        else:
            print(f"NOT Found '{word}'\n")

    # add
    elif command == 'A':
        word = command_values[1]
        frequency = int(command_values[2])
        word_frequency = WordFrequency(word, frequency)
        if not agent.add_word_frequency(word_frequency):
            print(f"Add '{word}' failed\n")
        else:
            print(f"Add '{word}' succeeded\n")

    # delete
    elif command == 'D':
        word = command_values[1]
        if not agent.delete_word(word):
            print(f"Delete '{word}' failed\n")
        else:
            print(f"Delete '{word}' succeeded\n")

    # check
    elif command == 'AC':
        word = command_values[1]
        list_words = agent.autocomplete(word)
        line = "Autocomplete for '" + word + "': [ "
        for item in list_words:
            line = line + item.word + ": " + str(item.frequency) + "  "
        print(line + ']\n')

    else:
        print('Unknown command.')
        print(line)
    execution_time = timeit.default_timer() - start_time
    #print(f"Command: {command}\nTime Taken:{execution_time}\n")
    return execution_time
if __name__ == '__main__':
    sizes = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000]
    analysis_file = open("analysis.txt", 'w')
    # Read Data from file and create word frequency array
    word_frequency = read_data()
    #TEST
    ##LIST
    #Create Dictionaries
    list_dicts = create_dict("list", word_frequency, sizes)
    
    #Tests
    #List Dict
    analysis_file.write("*************************\n")
    analysis_file.write("*****LIST DICTIONARY*****\n")
    analysis_file.write("*************************\n")
    for itr, dic in enumerate(list_dicts):
        analysis_file.write("-------\n")
        analysis_file.write("--ADD--\n")
        analysis_file.write("-------\n")
        add_times = []
        # Addition to structure
        add_times.append(execute_command("A booming1 123456",   dic))
        add_times.append(execute_command("A loblolly1 123456",  dic))
        add_times.append(execute_command("A tvpg1 123456",      dic))
        add_times.append(execute_command("A ohhlacom1 123456",  dic))
        #status
        analysis_file.write(f"Dictionary Length: {sizes[itr]}\nCommand: Add a word\nAverageTime:{sum(add_times)/len(add_times)}\n")

    analysis_file.write("---------- ACP -----------\n")
    for itr, dic in enumerate(list_dicts):
        analysis_file.write("-------\n")
        analysis_file.write("-------\n")
        ser_times = []
        ser_times.append(execute_command("AC boom",  dic))
        ser_times.append(execute_command("AC lobl", dic))
        ser_times.append(execute_command("AC tvp",     dic))
        ser_times.append(execute_command("AC ohh", dic))
        # Status
        analysis_file.write(f"Dictionary Length: {sizes[itr]}\nCommand: AutoCOmplete a word\nAverageTime:{sum(ser_times)/len(ser_times)}\n")
    
    analysis_file.write("---------- SER -----------\n")
    for itr, dic in enumerate(list_dicts):
        analysis_file.write("-------\n")
        analysis_file.write("-------\n")
        acp_times = []
        acp_times.append(execute_command("S booming1",  dic))
        acp_times.append(execute_command("S loblolly1", dic))
        acp_times.append(execute_command("S tvpg1",     dic))
        acp_times.append(execute_command("S ohhlacom1", dic))
        # Status
        analysis_file.write(f"Dictionary Length: {sizes[itr]}\nCommand: AC a word\nAverageTime:{sum(acp_times)/len(acp_times)}\n")
    
    for itr, dic in enumerate(list_dicts):
        analysis_file.write("-------\n")
        analysis_file.write("--DEL--\n")
        analysis_file.write("-------\n")
        del_times = []
        del_times.append(execute_command("D booming1",  dic))
        del_times.append(execute_command("D loblolly1", dic))
        del_times.append(execute_command("D tvpg1",     dic))
        del_times.append(execute_command("D ohhlacom1", dic))
        # Status
        analysis_file.write(f"Dictionary Length: {sizes[itr]}\nCommand: Delete a word\nAverageTime:{sum(del_times)/len(del_times)}\n")
    
            
    analysis_file.write("*************************\n")
    analysis_file.write("*****HASH DICTIONARY*****\n")
    analysis_file.write("*************************\n")
    
    analysis_file.write("---------- ADD -----------\n")
    hash_dicts=create_dict("hashtable", word_frequency, sizes)
    for itr, dic in enumerate(hash_dicts):
        analysis_file.write("-------\n")
        analysis_file.write("-------\n")
        add_times = []
        # Addition to structure
        add_times.append(execute_command("A booming1 123456",   dic))
        add_times.append(execute_command("A loblolly1 123456",  dic))
        add_times.append(execute_command("A tvpg1 123456",      dic))
        add_times.append(execute_command("A ohhlacom1 123456",  dic))
        # Status
        analysis_file.write(f"Dictionary Length: {sizes[itr]}\nCommand: Add a word\nAverageTime:{sum(add_times)/len(add_times)}\n")
    
    analysis_file.write("---------- ACP -----------\n")
    for itr, dic in enumerate(hash_dicts):
        analysis_file.write("-------\n")
        analysis_file.write("-------\n")
        ser_times = []
        ser_times.append(execute_command("ACP boom",  dic))
        ser_times.append(execute_command("ACP lobl", dic))
        ser_times.append(execute_command("ACP tvp",     dic))
        ser_times.append(execute_command("ACP ohh", dic))
        # Status
        analysis_file.write(f"Dictionary Length: {sizes[itr]}\nCommand: Search a word\nAverageTime:{sum(ser_times)/len(ser_times)}\n")
    
    analysis_file.write("---------- SER -----------\n")
    for itr, dic in enumerate(hash_dicts):
        analysis_file.write("-------\n")
        analysis_file.write("-------\n")
        acp_times = []
        acp_times.append(execute_command("S booming1",  dic))
        acp_times.append(execute_command("S loblolly1", dic))
        acp_times.append(execute_command("S tvpg1",     dic))
        acp_times.append(execute_command("S ohhlacom1", dic))
        # Status
        analysis_file.write(f"Dictionary Length: {sizes[itr]}\nCommand: AC a word\nAverageTime:{sum(acp_times)/len(acp_times)}\n")
    
    analysis_file.write("---------- DEL -----------\n")
    for itr, dic in enumerate(hash_dicts):
        analysis_file.write("-------\n")
        analysis_file.write("-------\n")
        del_times = []
        del_times.append(execute_command("D booming1",  dic))
        del_times.append(execute_command("D loblolly1", dic))
        del_times.append(execute_command("D tvpg1",     dic))
        del_times.append(execute_command("D ohhlacom1", dic))
        # Status
        analysis_file.write(f"Dictionary Length: {sizes[itr]}\nCommand: Delete a word\nAverageTime:{sum(del_times)/len(del_times)}\n")
    
    
    
    analysis_file.write("*************************\n")
    analysis_file.write("*****TREE DICTIONARY*****\n")
    analysis_file.write("*************************\n")
    tree_dicts=create_dict("tst",       word_frequency, sizes)
    analysis_file.write("---------- ADD -----------\n")
    for itr, dic in enumerate(tree_dicts):
        analysis_file.write("-------\n")
        
        analysis_file.write("-------\n")
        add_times = []
        # Addition to structure
        add_times.append(execute_command("A booming1 123456",   dic))
        add_times.append(execute_command("A loblolly1 123456",  dic))
        add_times.append(execute_command("A tvpg1 123456",      dic))
        add_times.append(execute_command("A ohhlacom1 123456",  dic))
        # Status
        analysis_file.write(f"Dictionary Length: {sizes[itr]}\nCommand: Add a word\nAverageTime:{sum(add_times)/len(add_times)}\n")    
   
    analysis_file.write("---------- ACP -----------\n")
    for itr, dic in enumerate(tree_dicts):
        analysis_file.write("-------\n")
        analysis_file.write("-------\n")
        ser_times = []
        ser_times.append(execute_command("AC boom",  dic))
        ser_times.append(execute_command("AC lobl", dic))
        ser_times.append(execute_command("AC tvp",     dic))
        ser_times.append(execute_command("AC ohh", dic))
        # Status
        analysis_file.write(f"Dictionary Length: {sizes[itr]}\nCommand: AutoComplete a word\nAverageTime:{sum(ser_times)/len(ser_times)}\n")
    
    analysis_file.write("---------- SER -----------\n")
    for itr, dic in enumerate(tree_dicts):
        analysis_file.write("-------\n")
        analysis_file.write("-------\n")
        acp_times = []
        acp_times.append(execute_command("S booming1",  dic))
        acp_times.append(execute_command("S loblolly1", dic))
        acp_times.append(execute_command("S tvpg1",     dic))
        acp_times.append(execute_command("S ohhlacom1", dic))
        # Status
        analysis_file.write(f"Dictionary Length: {sizes[itr]}\nCommand: AC a word\nAverageTime:{sum(acp_times)/len(acp_times)}\n")
    
    analysis_file.write("---------- DEL -----------\n")
    for itr, dic in enumerate(tree_dicts):
        analysis_file.write("-------\n")
        analysis_file.write("--DEL--\n")
        analysis_file.write("-------\n")
        del_times = []
        del_times.append(execute_command("D booming1",  dic))
        del_times.append(execute_command("D loblolly1", dic))
        del_times.append(execute_command("D tvpg1",     dic))
        del_times.append(execute_command("D ohhlacom1", dic))
        # Status
        analysis_file.write(f"Dictionary Length: {sizes[itr]}\nCommand: Delete a word\nAverageTime:{sum(del_times)/len(del_times)}\n")    
    
    analysis_file.close()