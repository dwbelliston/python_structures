#!/usr/bin/env python3

FILENAMES = [
    [ '1 Nephi',         '01-1 Nephi.txt' ],
    [ '2 Nephi',         '02-2 Nephi.txt' ],
    [ 'Jacob',           '03-Jacob.txt' ],
    [ 'Enos',            '04-Enos.txt' ],
    [ 'Jarom',           '05-Jarom.txt' ],
    [ 'Omni',            '06-Omni.txt' ],
    [ 'Words of Mormon', '07-Words of Mormon.txt' ],
    [ 'Mosiah',          '08-Mosiah.txt' ],
    [ 'Alma',            '09-Alma.txt' ],
    [ 'Helaman',         '10-Helaman.txt' ],
    [ '3 Nephi',         '11-3 Nephi.txt' ],
    [ '4 Nephi',         '12-4 Nephi.txt' ],
    [ 'Mormon',          '13-Mormon.txt' ],
    [ 'Ether',           '14-Ether.txt' ],
    [ 'Moroni',          '15-Moroni.txt' ],
]


###################################
###   Analyze a string of words

def analyze_text(book, text):
    '''Performs a very naive analysis of the words in the text, returning the SORTED list of WordData items'''
    # lowercase the entire text

    # split the text by whitespace to get a list of words

    # convert each word to the longest run of characters
    # eliminate any words that are empty after conversion to characters

    # count up the occurance of each word into a dictionary of: word -> count

    # create a WordData item for each word in our list of words

    # sort the WordData list using Bubble Sort, Insertion Sort, or Selection Sort:
    # 1. highest percentage [descending]
    # 2. highest count (if percentages are equal) [descending]
    # 3. lowest alpha order (if percentages and count are equal) [ascending]

    # return


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
    print('MAIN')
    master = []
    # loop through the filenames and analyze each one
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
