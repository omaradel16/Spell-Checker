from difflib import SequenceMatcher
#########################################################################
FONT1 = ('Times', 13)
FONT2 = ('Times', 13, 'underline')
MSG_FONT = ('Times', 14, 'bold')
#########################################################################


def get_dictionary(path="Dictionary.txt"):
    """
        Reads the dictionary file ==> returns a list of its words
    """
    with open(path, "r") as file:
        dictionary = file.read().split()

    return dictionary


def binary_search(alist, item):
    """
        searches for an item in a list ==> returns True (if item exists)
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
    """
        Returns the item of maximum ratio
        param alist = [[item, ratio], [item, ratio],.....]
    """

    if len(alist) == 0:
        return ""

    max_value = alist[0][1]
    max_position = 0

    for i in range(1, len(alist)):
        if alist[i][1] > max_value:
            max_value = alist[i][1]
            max_position = i

    alist[0], alist[max_position] = alist[max_position], alist[0]

    return alist[0][0]


def get_suggestions(dictionary, misspelled_words):
    """
        Gets suggestions for each misspelled word ==> returns a
        dictionary of each misspelled word as a key and suggestion word as a value:
        {
            misspelled_word: [suggestion]
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


def print_suggestions(text, words, misspelled_words, suggestions):
    """
        Prints the input text again with the correct word of misspelled words
        param text: the name of the textbox
        param words: the input text required to check
        param misspelled_words: list of misspelled_words in the input text
        param suggestions: dictionary of each misspelled word as a key and suggestion word as a value
    """
    text.delete(1.0, 'end')
# ########################################################################################
    msg = '                     ######### Correct misspelled words #########\n'
    msg1 = "Enter some words to check spelling !"
    msg2 = "Great! the program hasn't detect any misspelled words"
# ########################################################################################
    color_text(text, 'msg', msg, fg_color='blue', bg_color='white', my_font=MSG_FONT)

    if not words:
        color_text(text, 'msg1', msg1, fg_color='green', bg_color='white', my_font=MSG_FONT)

    elif not misspelled_words:
        color_text(text, 'msg2', msg2, fg_color='green', bg_color='white', my_font=MSG_FONT)

    else:
        for word in words:

            if word in misspelled_words:
                if not suggestions[word]:
                    color_text(text, word, word, fg_color='red', bg_color='white', my_font=FONT1)

                else:
                    color_text(text, word, suggestions[word], fg_color='green', bg_color='white', my_font=FONT2)

            else:
                color_text(text, word, word, fg_color='black', bg_color='white', my_font=FONT1)


def color_text(edit, tag, word, fg_color='black', bg_color='white', my_font=FONT1):
    # add a space to the end of the word
    word = word + " "
    edit.insert('end', word)
    end_index = edit.index('end')
    begin_index = "%s-%sc" % (end_index, len(word) + 1)
    edit.tag_add(tag, begin_index, end_index)
    edit.tag_config(tag, foreground=fg_color, background=bg_color, font=my_font)


def reprint_text(text, words, misspelled_words):
    """
        Prints the input text again with underlined misspelled words
    """
    text.delete(1.0, 'end')
    for word in words:
        if rem_punct(word) in misspelled_words:
            color_text(text, word, word, fg_color='red', bg_color='white', my_font=FONT2)

        else:
            color_text(text, word, word, fg_color='black', bg_color='white', my_font=FONT1)
