"""
This Python program implements the Randomized Quicksort algorithm, which is a variation
of the traditional Quicksort. The key difference is that the pivot element is chosen 
randomly for each partitioning step, rather than using a fixed position (like the first 
or last element). This randomization helps to avoid worst-case scenarios in cases where 
the input data may be already sorted or structured in an unfavorable way for traditional 
Quicksort.

The program consists of these main functions:
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
import time  # Import time module to measure execution time

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
        
# Function to measure and print the time taken to sort the array
def measure_sorting_time(arr, description):
    # Create a copy of the array to avoid modifying the original
    arr_copy = arr.copy()
    # Record the start time
    start_time = time.time()
    # Perform the sorting
    randomized_quicksort(arr_copy, 0, len(arr_copy) - 1)
    # Record the end time
    end_time = time.time()
    # Calculate and print the time taken
    time_taken = end_time - start_time
    print(f"Time taken to sort {description}: {time_taken:.6f} seconds")



# List of test arrays for various edge cases
test_arrays = {
    "Empty Array": [],
    "Repeated Elements": [5, 3, 8, 3, 9, 5, 3, 3, 8, 1],
    "Already Sorted": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Reverse Sorted": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    "Single Element": [42],
    "All Elements Same": [7, 7, 7, 7, 7, 7, 7, 7]
}

# Run randomized_quicksort on each test array
for description, arr in test_arrays.items():
    randomized_quicksort(arr, 0, len(arr) - 1)
    print(f"Sorted {description}: {arr}")

# Run randomized_quicksort on each test array and measure time
for description, arr in test_arrays.items():
    measure_sorting_time(arr, description)

