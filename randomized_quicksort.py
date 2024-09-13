"""
This Python program implements the Randomized Quicksort algorithm, which is a variation
of the traditional Quicksort. The key difference is that the pivot element is chosen 
randomly for each partitioning step, rather than using a fixed position (like the first 
or last element). This randomization helps to avoid worst-case scenarios in cases where 
the input data may be already sorted or structured in an unfavorable way for traditional 
Quicksort.

The program consists of three main functions:
1. randomized_partition: Chooses a random pivot and rearranges the array such that all 
   elements smaller than or equal to the pivot are on its left, and all greater elements 
   are on its right.
   
2. partition: Standard partition logic used in Quicksort, where the last element is 
   chosen as the pivot and the array is partitioned around it.
   
3. randomized_quicksort: The recursive function that repeatedly applies the 
   randomized_partition to sort the array. It sorts the subarrays to the left and right 
   of the pivot until the entire array is sorted.
   
This randomized approach improves the average-case performance to O(n log n) and ensures 
better results on inputs that might cause deterministic Quicksort to degrade to O(n^2).
"""



import random 

# Function to partition the array around a randomly selected pivot
def randomized_partition(arr, low, high):
    # Selecting a random index between low and high to use as the pivot
    pivot_index = random.randint(low, high)
    # Swapping the randomly selected pivot with the last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    # Calling the partition function to place the pivot in its correct position
    return partition(arr, low, high)

# Standard partition function used in Quicksort
def partition(arr, low, high):
    pivot = arr[high]  # Using the last element as the pivot
    i = low - 1  # Index for smaller element
    # Traversing through the array and place elements smaller than the pivot on the left
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swapping if the current element is smaller than or equal to the pivot
    # Placing the pivot in its correct position
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1  # Returning the index of the pivot

# Function to implement Randomized Quicksort
def randomized_quicksort(arr, low, high):
    if low < high:
        # Getting the pivot index using the randomized partition function
        pi = randomized_partition(arr, low, high)
        # Recursively applying Quicksort to the left and right of the pivot
        randomized_quicksort(arr, low, pi - 1)  # Sorting elements before the pivot
        randomized_quicksort(arr, pi + 1, high)  # Sorting elements after the pivot

