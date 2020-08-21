# Given is a list full of anagrams 
# ['mmo', 'omm', 'mom', 'tom', 'omt', 'mot']
# Return all the matching anagrams in seperate lists 
from collections import defaultdict

def sort_anagram(anagram_list):

    dict = defaultdict(list)

    for word in anagram_list:
        sorted_word = sorted(word)
        new_word = "".join(sorted_word)
        dict[new_word].append(word)
    
    return dict

if __name__ == "__main__":
    anagram_list = ['mmo', 'omm', 'tom', 'omt', 'mot','mom']
    print(sort_anagram(anagram_list))