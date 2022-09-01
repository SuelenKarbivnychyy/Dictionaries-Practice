"""Dictionaries Practice

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""
from collections import Counter

# def without_duplicates(words):
#     """Given a list of words, return list with duplicates removed.

#     For example:

#         >>> no_dupes = without_duplicates(
#         ...     ["rose", "is", "a", "rose", "is", "a", "rose"])

#         >>> isinstance(no_dupes, list)
#         True

#         >>> sorted(without_duplicates(
#         ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
#         ['a', 'is', 'rose']

#     You should treat differently-capitalized words as different:

#         >>> sorted(without_duplicates(
#         ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
#         ['Rose', 'a', 'is', 'rose']

#         An empty list should return an empty list:

#         >>> sorted(without_duplicates(
#         ...     []))
#         []

#     The function should work for a list containing integers:

#         >>> sorted(without_duplicates([111111, 2, 33333, 2]))
#         [2, 33333, 111111]

#     The function should return a variable of type list:
#         >>> type(without_duplicates([111111, 2, 33333, 2]))
#         <class 'list'>
#     """


#     #Pseudocode : create an empty list
#     # iterate through the given list
#     # check if word is not in the list and append it
#     #return new list
    

#     no_duplicate = []

#     for word in words:
        
#         if not word in no_duplicate:

#             no_duplicate.append(word)                

#     return no_duplicate
 

# # remove_duplicates = without_duplicates(["Rose", "is", "a", "rose", "is", "a", "rose"]) 
# remove_duplicates = without_duplicates([111111, 2, 33333, 2])
# check_instance = isinstance(remove_duplicates, list) 
# print(check_instance)
# print(type(remove_duplicates))
# print(sorted(remove_duplicates))



# def find_unique_common_items(items1, items2):
#     """Produce the set of *unique* common items in two lists.

#     Given two lists, return a set of the *unique* common items
#     shared between the lists.

#     **IMPORTANT**: you may not use `'if ___ in ___``
#     or the method `list.index()`.

#     This should return a set:

#         >>> unique_common_items = find_unique_common_items([1, 2, 3, 4], [2, 1])
#         >>> isinstance(unique_common_items, set)
#         True

#     This should find [1, 2]:

#         >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
#         [1, 2]

#     However, now we only want unique items, so for these lists,
#     don't show more than 1 or 2 once:

#         >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
#         [1, 2]

#     The elements should not be treated as duplicates if they are
#     different data types:

#         >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
#         [2]
#     """


#     #Pseudocode:
#     #created an empty set
#     #iterate trough the list 1
#     #check if each element has in list2
#     #return set

#     common_items = set()  #empty set

#     common_items =set(items1).intersection(items2)
#     # print(common_items) #testintg       
#     return common_items

# unique_common_items = find_unique_common_items(["2", "1", 2], [2, 1])
# isinstance(unique_common_items, set)
# sorted(unique_common_items)
# print(unique_common_items)    


# def get_sum_zero_pairs(numbers):
#     """Given list of numbers, return list of pairs summing to 0.

#     Given a list of numbers, add up each individual pair of numbers.
#     Return a list of each pair of numbers that adds up to 0.

#     For example:

#         >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
#         [[-2, 2], [-1, 1]]

#         >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
#         [[-3, 3], [-2, 2], [-1, 1]]

#     This should always be a unique list, even if there are
#     duplicates in the input list:

#         >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
#         [[-2, 2], [-1, 1]]

#     Of course, if there are one or more zeros to pair together,
#     that's fine, too (even a single zero can pair with itself):

#         >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
#         [[-1, 1], [0, 0]]
#     """

#     return []


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most in the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    #pseudocode:
    #create an empty list
    #set counter equals to 0
    #check for each iteration if letter in the list
    #append letter and count 1 if letter in the list
    #increase with 0 if letter no in the list

    common_chars = {}
    letter_count_result = []
    max_value = 0
    
    phrase = phrase.replace(" ", "")

    for char in phrase:  

        common_chars[char] = common_chars.get(char, 0) + 1

    for key in common_chars:

        if common_chars[key] > max_value:
            max_value = common_chars[key]
    # print(max_value)  #test

    for key in common_chars:

        if common_chars[key] == max_value:

            letter_count_result.append(key)

    return letter_count_result    

character_count = top_chars("The rain in spain stays mainly in the plain.")
print(character_count)
          

#####################################################################
# You can ignore everything below this.


def sort_pairs(l):
    """ Print sorted list of pairs where the pairs are sorted."""
    # NOTE: This is used only for documentation tests. You can ignore it.

    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print()
    import doctest
    if doctest.testmod().failed == 0:
        print("*** ALL TESTS PASSED ***")
    print()
