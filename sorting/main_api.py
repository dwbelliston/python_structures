#!/usr/bin/env python3
import re
from worddata import WordData
from sorts.bubble import bubble_sort
from sorts.insertion import insertion_sort

FILENAMES = [
    # [ '1 Nephi',         '01-1 Nephi.txt' ],
    # [ '2 Nephi',         '02-2 Nephi.txt' ],
    # [ 'Jacob',           '03-Jacob.txt' ],
    # [ 'Enos',            '04-Enos.txt' ],
    # [ 'Jarom',           '05-Jarom.txt' ],
    # [ 'Omni',            '06-Omni.txt' ],
    # [ 'Words of Mormon', '07-Words of Mormon.txt' ],
    # [ 'Mosiah',          '08-Mosiah.txt' ],
    # [ 'Alma',            '09-Alma.txt' ],
    # [ 'Helaman',         '10-Helaman.txt' ],
    # [ '3 Nephi',         '11-3 Nephi.txt' ],
    # [ '4 Nephi',         '12-4 Nephi.txt' ],
    # [ 'Mormon',          '13-Mormon.txt' ],
    # [ 'Ether',           '14-Ether.txt' ],
    # [ 'Moroni',          '15-Moroni.txt' ],
    ['test',          '99-99-test.txt'],
]


###################################
###   Analyze a string of words

def analyze_text(book, text):
    '''Performs a very naive analysis of the words in the text, returning the SORTED list of WordData items'''
    print('Analyzing {} ...'.format(book))
    # lowercase the entire text
    text = text.lower()
    # split the text by whitespace to get a list of words
    # # The str.split() method without an argument splits on whitespace:
    text = text.split()
    # convert each word to the longest run of characters
    for i, word in enumerate(text):
        m = re.match(r'(?P<word>[a-z]+)', word)
        if m:
            text[i] = m.group('word')
        else:
            # eliminate any words that are empty after conversion to characters
            text.remove(word)

    # will be used to calc percentage
    text_total_count = len(text)
    # count up the occurance of each word into a dictionary of: word -> count
    word_counts = dict()
    for w in text:
        # .get allows you to specify a default value if the key does not exist.
        word_counts[w] = word_counts.get(w, 0) + 1

    # create a WordData item for each word in our list of words
    word_data = []
    for k, v in word_counts.items():
        wd = WordData(book, k, v)
        # Set percent based on total text word count
        wd.set_percent(text_total_count)
        word_data.append(wd)

    # sort the WordData list using Bubble Sort, Insertion Sort, or Selection Sort:
    # 1. highest percentage [descending]
    # 2. highest count (if percentages are equal) [descending]
    # 3. lowest alpha order (if percentages and count are equal) [ascending]
    sort_by_order = [
        {'name': 'percent', 'dir': 'asc'},
        {'name': 'count', 'dir': 'desc'},
        {'name': 'word', 'dir': 'desc'}
    ]

    # sorted_data = bubble_sort(word_data, sort_by_order)
    sorted_data = insertion_sort(word_data, sort_by_order)

    print('SORTED::')
    for i in sorted_data:
        print(i)

    return sorted_data


################################
###   Prints a words list

def print_words(words, threshold=None, word=None):
    '''Prints a list of words'''
    # print the words over the threshold_percent or that match the given word

    # print an empty line



#######################
###   Main loop

def main():
    '''Main program'''
    master = []
    # loop through the filenames and analyze each one
    for file_info in FILENAMES:
        with open ('word_bank/{}'.format(file_info[1]), "r") as f:
            file_data=f.read()
            analyze_text(file_info[0], file_data)

    # after analyzing each file, merge the master and words lists into a single, sorted list (which becomes the new master list)
    print('INDIVIDUAL BOOKS > 2%')

    # print each book, word, count, percent in master list with percent over 2
    print('MASTER LIST > 2%')

    # print each book, word, count, percent in master list with word == 'christ'
    print('MASTER LIST == christ')

    # read the full text of the BoM and analyze it
    print('FULL TEXT > 2%')



#######################
###   Runner

if __name__ == '__main__':
    main()
