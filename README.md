# Word-Completion-Algo-analysis-using-TST

## About 

Word auto-complete functionality is very common in text editors and smart phone apps nowadays. In this assignment you will implement a dictionary that store English words and their frequencies and allows operations such as addition, deletion, search, and auto-completion. This repository consists of the python script that will evaluate and compare the running time of each operations for different data structures (list, dictionary, and ternary search tree) in various scenarios. 

## Objectives

There are a number of key objectives for this program:

• Understand how a real-world problem can be implemented by different data structures and/or
algorithms.
• Evaluate and contrast the performance of the data structures and/or algorithms with respect to
different usage scenarios and input data.

In this program, we focus on the word completion problem.

## Background

Word/sentence (auto-)completion is a very handy feature of nowadays text editors and email browsers
(you must have used it in your Outlook). While sentence completion is a much more challenging task
and perhaps requires advanced learning methods, word completion is much easier to do as long as
you have a dictionary available in the memory. In this assignment, we will focus on implementing a
dictionary comprising of words and their frequencies that allows word completion. We will try several
data structures and compare their performances. One of these data structures is the Ternary Search
Tree, which is described below.

## Ternary Search Trees

Ternary search trees (TST) is a data structure that allows memory-efficient storage of strings and fast
operations such as spell checking and auto-completion.
Each node of the a TST contains the following fields:
• a lower-case letter from the English alphabet (‘a’ to ‘z’),
• a positive integer indicating the word’s frequency (according to some dataset) if the letter is the
last letter of a word in the dictionary,
• a boolean variable that is True if this letter is the last letter of a word in the dictionary and False
otherwise,
• the left pointer points to the left child-node whose letter is smaller (in alphabetical order, i.e.
‘a’ < ‘b’),
• the right pointer points to the right child-node whose letter is larger,
• the middle pointer points to a node that stores the next letter in the word.
As an example, consider Figure 1.

![Figure 1](https://github.com/Anujsharma0307/Word-Completion-Algo-analysis-using-TST/blob/main/Screen%20Shot%202022-05-18%20at%2011.29.19%20am.png?raw=true)

Figure 1: An example of a ternary search tree storing five words and their frequencies. The boolean
value (T)rue indicates that the letter is the end of a word. In that case, a frequency (an integer) is
shown, e.g., 10 for ‘cut’. Note that a word can be a prefix of another, e.g., ‘cut’ is a prefix of ‘cute’.

## 
