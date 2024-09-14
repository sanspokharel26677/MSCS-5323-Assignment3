# MSCS-5323-Assignment3

1. As a part of assignment 3, this repo contains 2 files named, "ramdomized_quicksort.py" and "hashing.py" for part 1 and part 2. 
2. Source code should be run by python3. 
3. Example: To run 'hashing.py' in the terminal we should go to the directory where the file is saved and enter "python3 hashing.py". Similarly other python file can be run. 
4. I have also added one of the output file generated from running the program which has been used in report also just in case of need for validation. 
5. I have also included the pdf version of report so that mathematical equations could be stable.


Summary
Randomized Quicksort provides more consistent performance across different input types and sizes, avoiding worst-case scenarios by selecting random pivots.
Deterministic Quicksort can outperform Randomized Quicksort on random arrays due to lower overhead, but it suffers significantly on already sorted and reverse-sorted arrays due to poor pivot choices, confirming the expected O(n^2) behaviour
Repeated Elements present a unique challenge where Randomized Quicksort may show increased times, though still generally within O(nlogn) bounds. 


Summary 

The measured times for insert, search, and delete operations in this hash table implementation reflect the effectiveness of chaining with a well-chosen hash function and dynamic resizing. By maintaining a low load factor through resizing, the hash table minimizes collisions and ensures efficient performance across operations. The use of chaining for collision resolution further ensures that even in the presence of collisions, operations remain quick. 
