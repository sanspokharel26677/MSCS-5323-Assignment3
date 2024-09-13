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

