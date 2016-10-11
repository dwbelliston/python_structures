# Assignment: Sort Analytics

Create a new project and copy your sorting classes into it (bubble sort, insertion sort, selection sorts).  Add one additional sort algorithm: quicksort. Test your new sorting algorithm with a few lists to ensure it works correctly.  Try lists of one item, already-sorted lists, fully-unsorted lists, etc.

Next, determine how your language sorts lists natively.  For example, if we have a Python list called `mylist` that holds integers, we'd call `mylist.sort()` to have Python sort the list for us.  Internally, Python uses a variation of quicksort to do the work.  What is the code to sort in your language?

Now that you have five sorting algorithms (four of your own making and one in your language), evaluate their relative speed.  Sort each list of numbers included with this assignment, and print the results.  If you want to go the extra mile and are using Python, try compiling your algorithms to machine code using the Cython library.  This should dramatically improve speed.

Finally, I will give 10 extra credit points (not to exceed 100 overall points on this assignment) to any student who can determine the name of every list of numbers in this assignment.  Each is a list of numbers in the real world or in mathematics.

## Analytics Process

Loop through the number files in this assignment.  For each list of numbers, do the following:
 
1. Print the name of the list, or the filename if you don't know the name of the list.
1. For each of the six sorting algorithms, do the following:
    1. Read the list into a list/array.  Use the native data types in your language (not your array or linked list from earlier assignments).  Read the list fresh with each sorting algorithm so each has the same input sequence.
    1. Copy the list of numbers 1,000 times so you can sort more than once. 
    1. Save the current time in millis.
    1. In a for loop, sort each of the lists using the specific algorithm.  You should only sort each copy once (you have 1,000 copies).
    1. Calculate the current time in millis minus the start time.  Create a `Result` object for this result.
1. You should now have five result objects: one for each algorithm.  Determine which was the fastest, and calculate the relative increase in time of each algorithm.  The formula is: `100.0 * (algorithm time - fastest time) / fastest time`.  
1. Sort the five results from fastest to slowest.
1. Print the times to the console as shown in `example_output.txt`.  Please try to match this file exactly with your output.  The relative time is rounded to the nearest integer.  Note that the first 10 and last 10 numbers of each set are included in the printout.

Note that the portion we are timing above is as minimal as possible.  We are reading the list of numbers, generating the thousand copies, and printing outside of the timed part.  This is to make the time as reliable as possible.

## Submitting the Assignment

Zip all your assignment files and submit on Learning Suite.
