# Assignment: Book of Mormon Words

Create a new project and program three sorting algorithms:

1. Bubble Sort
1. Insertion Sort
1. Selection Sort

Write a tester program to ensure each sorting algorithm sorts correctly.  You cannot, of course, use the built-in sorting functions of your language, but you **can** use built-in list functionality of your language.  You are not required to use the Array or LinkedList classes you programmed earlier in the course.  Your sorting functions should modify the list in-place rather than create a new list.


## File Analysis

Your assignment is to count the frequencies of each word used in the Book of Mormon.  The overall program should:

1. Analyze each individual book and print the results (> 2 percent).  Merge `master` and each list as you go.
1. Print the `master` list items (> 2 percent).
1. Print the `master` list items (word == 'christ').
1. Analyze the full text of the Book of Mormon and print the results (> 2 percent).

On Step 1 above, you'll analyze all 15 books, starting with `01-1 Nephi.txt`.  

When analyzing an individual file (Step 1 and 4 above), follow this process:

1. Read the text file into a string.  The first file to analyze is `01-1 Nephi.txt`.
1. Convert the string to lowercase so all words are lower. This allows the words `Behold` and `behold` to be counted together.
1. Split the string by any white space character.  Regular expressions are your friend here.  You should now have a list of individual words.
1. Convert each word to the longest run of alpha characters within that word.  If the word is empty after this step (i.e. doesn't contain any alpha), remove it from the list.  Words like `2` are skipped, and words like `pass,` are converted to `pass`.
1. Count the frequency of each word in the list.  This results in a list of WordData objects containing the book, word, count, and percent. Round all percentages to one decimal place: `3.1415 percent => 3.1 percent`.  You can use a library to count the frequencies, or you can roll your own code to do it.  The percent for a given word is calculated as `count / num words in list`, rounded to one decimal place.
1. Sort the words by highest percent, highest count, alpha order.  For each file, choose one of your sorting algorithms (Bubble Sort, Insertion Sort, Selection Sort).  Be sure each algorithm is used at least once.
1. Print the sorted WordData object data (one line per WordData) for all words with a percentage over 2%.  Follow each book printout with a blank line.  See `example_output.txt` for the exact format.

Do not modify the input files.  Your program should be written to deal with them as they are.


## Merging Lists

Throughout Step 1 of the assignment, keep a running `master` list of all WordData objects analyzed thus far.  The `master` list starts empty.  After analyzing an individual book, merge the current `master` list with the results from that book.  This should result in a new `master` list and the garbage collection of the old `master` list.  DO NOT just insert the items into the master list and then sort.  The sorting should occur as you insert the next item from one list or the other.  Order using highest percent, highest count, alpha order.

In other words, go through both lists at the same time.  At each item, insert the next WordData object from either list A or list B, depending on the their percent values.  If their percent values are the same, insert based on the count value.  If percent and count values are the same, insert based on the alpha order.

Merging two, sorted lists (or transaction sets) is a common problem done in data mining and business processing.  This part of the assignment is to give you experience coding the process.  It can be tricky to get right.

An iterator on each list is one way to code this algorithm.  Another hint is to `sleep` your code and print debug statements as it runs in human time.


## Submitting the Assignment

Zip the following files and submit on Learning Suite (again, using Python extensions here):

```
main.py
worddata.py
merge.py
bubblesort.py
insersionsort.py
selectionsort.py
output.txt
(add any additional files needed to run your program)
```
