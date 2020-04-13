#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""
import re

__author__ = "Cedric Mulvihill"

"""We need a function that takes a string with missing characters
and a list of all possible words"""
def match_words(string, library):
    #to format the string into individual letters and re
    string_formatter = []
    #list we will return with matching words
    match_list = []
    """Iterate through the string to seperate the letters
    from the missing characters, replacing the missing 
    characters with regex expression for letters in range
    from a to z"""
    for i in string:
        if i == ' ':
            string_formatter.append('[a-z]')
        else:
            string_formatter.append(i)
    #String formatted for regex
    f_string = ''.join(string_formatter)
    """Iterating through the dictionary to find matches for
    the given string"""
    for w in library:
        if re.match(f_string, w):
            match_list.append(w)
    return match_list


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()
    for i in match_words(test_word, words):
        print(i)


if __name__ == '__main__':
    main()
