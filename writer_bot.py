"""
    File: writer_bot.py
    Author: Jake Kravas
    Purpose: display randomly
    generated text to user based
    on prefixes and suffixes of
    user-inputted .txt file, with
    length of prefix and # of
    words to print out up to the
    user
"""

from random import *
SEED = 8
seed(SEED)
NONWORD = ' '

def get_data_from_file():
    """
        gets file input from
        user and returns words
        of file, prefix length (n)
        and display_length
    """

    # txt file
    sfile = input()

    # prefix size
    n = int(input())

    # number of words to print
    display_length = int(input())

    # words in file
    words = []
    # words = ['NONWORD' for i in range(n)]

    sfile_data = open(sfile, 'r')
    sfile_lines = sfile_data.readlines()

    # add words from file to words list
    for line in sfile_lines:

        # remove excess whitespace from line and convert it to a list
        line = line.strip().split()

        # add each word in line to list
        for word in line:
            words.append(word)
    

    sfile_data.close()

    return words, n, display_length

def create_prefix_dict(words, n):
    """
        returns dictionary of prefixes
        based on words argument
    """

    if n == 1:
        prefix_dict = {(NONWORD): [words[0]]}


    elif n == 2:
        prefix_dict = {(NONWORD, NONWORD): [words[0]], (NONWORD, words[0]): [words[1]]}


    elif n == 3:
        prefix_dict = {
            (NONWORD, NONWORD, NONWORD): [words[0]],
            (NONWORD, NONWORD, words[0]): [words[1]],
            (NONWORD, words[0], words[1]): [words[2]]
        }


    for i in range(len(words)):
        if i + n < len(words):

            # set prefix to tuple of length n
            prefix = tuple(words[i:i + n])

            # add word after prefix to prefix_dict
            if prefix in prefix_dict:
                prefix_dict[prefix].append(words[i + n])
            else:
                prefix_dict[prefix] = [words[i + n]]
    
    return prefix_dict


def get_words_to_display(words, prefix_dict, n, display_length):
    """
        returns list of words to display
    """

    # list of words to be printed to user
    words_to_display = words[:n]

    # tuple of current prefix
    cur_prefix_tup = tuple(words_to_display)

    while cur_prefix_tup in prefix_dict and len(words_to_display) < display_length:

        # list of suffixes of current prefix
        cur_suffix_list = prefix_dict[cur_prefix_tup]

        # if cur_suffix_list length is 0, set word_pos to 0
        # otherwise set word_pos to randomly generated #
        # from 0 to length of current_suffix_list
        if len(cur_suffix_list) == 1:
            word_pos = 0
        else:
            word_pos = randint(0, len(cur_suffix_list)-1)

        # set new_word to 
        new_word = cur_suffix_list[word_pos]

        # add new_word to words_to_display
        words_to_display.append(new_word)

        # update variable since words_to_display has changed
        cur_prefix_tup = tuple(words_to_display[-n:])
    
    return words_to_display


def display_words(words_to_display):
    """
        prints words in words_to_display
        with a new line after every
        ten words
    """

    # list of lists that will hold words to display
    words_to_display_lines = []

    for i in range(len(words_to_display)):

        # append new empty list if i divisible by 10
        if i % 10 == 0:
            words_to_display_lines.append([])

        # add word to most recently appended list in words_to_display_lines
        words_to_display_lines[-1].append(words_to_display[i])


    for line in words_to_display_lines:

        # convert line to string
        line = ' '.join(line)

        print(line)


def main():
    words, n, display_length = get_data_from_file()
    prefix_dict = create_prefix_dict(words, n)
    words_to_display = get_words_to_display(words, prefix_dict, n, display_length)
    display_words(words_to_display)

main()