import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
# starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
# the function selection_sort_books will taka a lst of books, and it will sort the books by author in alphabetical order
# the letter index helper function will return the index a given number is at


## finish here, letter index will tell index of the given letter, then use to compar 
def letter_index(letter:str) -> int:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    caps_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
    if letter in letters:
        return letters.index(letter)
    if letter in caps_letters:
        return caps_letters.index(letter)




def selection_sort_books(books):
    # Traverse through all Book objects
    for i in range(len(books)):
        mindex = i
        for j in range(i + 1, len(books)):
            if books[j].title < books[mindex].title:
                mindex = j
                books[i], books[mindex] = books[mindex], books[i]



# Part 2
#######################################################################################################################
# swap case takers a single parameter of type string and returns a similar string, but with the cases of the letters
# swapped

def swap_case(words:str) -> str:
    swapped_chars = ""
    for char in range(len(words)):
        if words[char].isupper():
            swapped_chars += words[char].lower()
        elif words[char].islower():
            swapped_chars += words[char].upper()
        else:
            swapped_chars += words[char]
    return swapped_chars

# Part 3
#######################################################################################################################
# str_translate will take three inputs, an input string, an 'old' string, and a 'new' string. the fucntion will find any
# instances of 'old' in the input string, and replace them with the 'new' string.
# this is done by splitting the input string into each of it's separate words, then replacing the neccessary words, and
# putting the strings back together
# I was not sure what exactly was being asked so I created two functions to do what I think was going to be done

# this funciton will replace words

def str_translate(string: str,old: str,new: str ) -> str:
    if old in string:
        split_old = string.split(f'{old}')
        return f'{split_old[0]}{new}{split_old[1]}'




# Part 4
#######################################################################################################################
# histogram will take a single string and return a dictionary mapping of strings to integers of each word. it will do
# this using the split function to separate all of the words in the string into an iterable list of words. 

def histogram(words:str) -> dict[str,int]:
    word_dict = {}
    for word in words.split():
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    return word_dict