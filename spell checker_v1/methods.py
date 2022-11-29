# from difflib import SequenceMatcher
# 
# 
# def get_dictionary(path="Dictionary.txt"):
#     """
#         Reads the dictionary file ==> returns a list of its words
#     """      
# 
#     f = open(path)
#     dictionary = f.read().split()
#     f.close
# 
#     return dictionary
# 
# 
# def binary_search(alist, item):
#     """
#         searchs for an item in a list ==> returns True (if item exists)
#         or False (if item doesn't exist)
#     """
# 
#     first = 0
#     last = len(alist) - 1
# 
#     while first <= last:
#         mid = (first + last) // 2
# 
#         if alist[mid] == item:
#             return True
#         elif item < alist[mid]:
#             last = mid - 1
#         else:
#             first = mid + 1
# 
#     return False
# 
# 
# def rem_punct(word):
#     """
#         Removes punctuation from english words if exists
#     """
#     if word[0] in "&-":
#         word = word[1:]
# 
#     if word[-1] in ".,?!":
#         word = word[:-1]
# 
#     return word
# 
# 
# def is_misspelled(dictionary, word):
#     """
#         Checks spelling of a word ==> returns True (if the word is misspelled)
#         or False (if the word is correct)
#     """
# 
#     if len(word) == 0 or word.isdigit():
#         return False
#     else:
#         return not binary_search(dictionary, word)
# 
# 
# def get_misspelled(dictionary, words):
#     """
#         Returns a list of misspelled words from user words
#     """
# 
#     misspelled_words = []
# 
#     for word in words:
#         word = rem_punct(word)
# 
#         if word not in misspelled_words and \
#            is_misspelled(dictionary, word):
#             misspelled_words.append(word)   
# 
#     return misspelled_words
# 
# 
# def custom_max(alist, n2):
# 
#     n = len(alist)
# 
#     if n2 > n:
#         n2 = n
# 
#     for i in range(n2):
#         max_value = alist[i][1] 
#         max_position = i 
# 
#         for j in range(i + 1, n):
#             if alist[j][1] > max_value:
#                 max_value = alist[j][1]
#                 max_position = j
# 
#         alist[i], alist[max_position] = alist[max_position], alist[i]
#     
#     return alist[:n2]
# 
# 
# def get_suggestions(dictionary, misspelled_words, n=3):
#     """
#         Gets suggestions for each misspelled word ==> returns a 
#         dictionary of each misspelled word as a key and a list of suggestions for this word as a value:
#         {
#             misspelled_word: [list of its suggestions]
#         }
#     """
# 
#     suggestions = {}
# 
#     for word in misspelled_words:
# 
#         temp = []
#         s = SequenceMatcher()
#         s.set_seq2(word)
#        
#         for item in dictionary:
#             s.set_seq1(item)
# 
#             if s.real_quick_ratio() >= 0.65 and \
#                s.quick_ratio() >= 0.65 and \
#                s.ratio() >= 0.65:
#                 temp.append([item, s.ratio()])
# 
#         suggestions[word] = custom_max(temp, n)
# 
#     return suggestions
# 
# 
# def print_suggestions(misspelled_words, suggestions):
# 
#     print("\033[1;32m######### misspelled words & Suggestions #########\033[0m\n")
#     
#     if misspelled_words == []:
#         print("\033[38;5;45mNo misspelled words...\033[0m")
#     else:
#         for word in misspelled_words:
#             if suggestions[word] == []:
#                 print(f"\033[38;5;231m{word}:\033[0m\033[38;5;45m No suggestions!\033[0m")
#             else:
#                 print(f"\033[38;5;231m{word}:\033[0m ", end='')
# 
#                 sugges = ""
#                 for w in suggestions[word]:
#                     sugges += (w[0] + ", ")
#                 sugges = sugges.strip(", ")
# 
#                 print(f"\033[38;5;45m{sugges}.\033[0;0m")
# 
# 
# def print_underlined(words, misspelled_words):
#     
#     print("\033c\033[38;5;231mType words to check its spelling: \033[0m")
#     
#     for word in words:
#         if rem_punct(word) in misspelled_words:
#             print(f"\033[4;31m{word}\033[0m", end=' ')
#         else:
#             print(word, end=' ')
#     print("\n")
# 
# 
# if __name__ == '__main__':
#    
#     sentence = input("\033[38;5;231mType words to check its spelling:\033[0m\n")
#     words_list = sentence.lower().split()
# 
#     dictionary = get_dictionary()
# 
#     mispelled_words = get_misspelled(dictionary, words_list)
# 
#     print_underlined(words_list, mispelled_words)
# 
#     suggestions = get_suggestions(dictionary, mispelled_words)
# 
#     print_suggestions(mispelled_words, suggestions)

from difflib import SequenceMatcher


def get_dictionary(path="Dictionary.txt"):
    """
        Reads the dictionary file ==> returns a list of its words
    """

    f = open(path)
    dictionary = f.read().split()
    f.close

    return dictionary


def binary_search(alist, item):
    """
        searchs for an item in a list ==> returns True (if item exists)
        or False (if item doesn't exist)
    """

    first = 0
    last = len(alist) - 1

    while first <= last:
        mid = (first + last) // 2

        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return False


def rem_punct(word):
    """
        Removes punctuation from english words if exists
    """
    if word[0] in "&-":
        word = word[1:]

    if word[-1] in ".,?!":
        word = word[:-1]

    return word


def is_misspelled(dictionary, word):
    """
        Checks spelling of a word ==> returns True (if the word is misspelled)
        or False (if the word is correct)
    """

    if len(word) == 0 or word.isdigit():
        return False
    else:
        return not binary_search(dictionary, word)


def get_misspelled(dictionary, words):
    """
        Returns a list of misspelled words from user words
    """

    misspelled_words = []

    for word in words:
        word = rem_punct(word)

        if word not in misspelled_words and \
                is_misspelled(dictionary, word):
            misspelled_words.append(word)

    return misspelled_words


def custom_max(alist):

    if len(alist) == 0:
        return ""
    
    max_value = alist[0][1]
    max_position = 0

    for j in range(1, len(alist)):
        if alist[j][1] > max_value:
            max_value = alist[j][1]
            max_position = j

    alist[0], alist[max_position] = alist[max_position], alist[0]

    return alist[0][0]


def get_suggestions(dictionary, misspelled_words):
    """
        Gets suggestions for each misspelled word ==> returns a 
        dictionary of each misspelled word as a key and a list of suggestions for this word as a value:
        {
            misspelled_word: [A suggestion]
        }
    """

    suggestions = {}

    for word in misspelled_words:

        temp = []
        s = SequenceMatcher()
        s.set_seq2(word)

        for item in dictionary:
            s.set_seq1(item)

            if s.real_quick_ratio() >= 0.65 and \
                    s.quick_ratio() >= 0.65 and \
                    s.ratio() >= 0.65:
                temp.append([item, s.ratio()])

        suggestions[word] = custom_max(temp)

    return suggestions


def print_suggestions(misspelled_words, suggestions):
    print("\033[1;32m######### misspelled words & Suggestions #########\033[0m\n")

    if misspelled_words == []:
        print("\033[38;5;45mNo misspelled words...\033[0m")
    else:
        for word in misspelled_words:
            if suggestions[word] == "":
                print(f"\033[38;5;231m{word}:\033[0m\033[38;5;45m No suggestions!\033[0m")
            else:
                print(f"\033[38;5;231m{word}: {suggestions[word]}\033[0m ", end='')

                # sugges = ""
                # for w in suggestions[word]:
                #     sugges += (w[0] + ", ")
                # sugges = sugges.strip(", ")

                #print(f"\033[38;5;45m{sugges}.\033[0;0m")


def print_underlined(words, misspelled_words):
    print("\033c\033[38;5;231mType words to check its spelling: \033[0m")

    for word in words:
        if rem_punct(word) in misspelled_words:
            print(f"\033[4;31m{word}\033[0m", end=' ')
        else:
            print(word, end=' ')
    print("\n")


if __name__ == '__main__':
    sentence = input("\033[38;5;231mType words to check its spelling:\033[0m\n")
    words_list = sentence.lower().split()

    dictionary = get_dictionary()

    mispelled_words = get_misspelled(dictionary, words_list)

    print_underlined(words_list, mispelled_words)

    suggestions = get_suggestions(dictionary, mispelled_words)

    print_suggestions(mispelled_words, suggestions)
