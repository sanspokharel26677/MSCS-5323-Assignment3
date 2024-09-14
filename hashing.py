"""
This Python program implements a hash table using chaining for collision resolution. 
It supports the following operations efficiently:
    1. Insert: Adds a key-value pair to the hash table.
    2. Search: Retrieves the value associated with a given key.
    3. Delete: Removes a key-value pair from the hash table.
    4. Display: Shows the current state of the hash table.

Key Features:
    - **Hash Function**: Uses a simple hash function that distributes keys uniformly
      across the hash table to minimize collisions. It uses a prime number (31) to generate
      hash values.
    - **Chaining**: Resolves collisions by storing colliding elements in a linked list (chain)
      at each slot of the hash table.
    - **Dynamic Resizing**: The hash table resizes (doubles its size) when the load factor exceeds
      a specified threshold (0.7) to maintain efficient performance. This process involves rehashing 
      all existing elements into the new table.
    - **Performance Measurement**: Includes functionality to measure the time taken for insert, 
      search, and delete operations to analyze the hash table's performance.

Sections of the Code:
    1. **HashTable Class**: Defines the core hash table functionalities including:
        - `_hash_function`: Computes the hash value for a given key.
        - `insert`: Adds a key-value pair to the hash table.
        - `search`: Finds and returns the value for a given key.
        - `delete`: Removes the key-value pair for a given key.
        - `display`: Prints the current state of the hash table.
        - `_resize`: Dynamically resizes the hash table when the load factor is too high.
    2. **measure_time Function**: Measures and returns the time taken for performing an 
       insert, search, or delete operation.
    3. **Example Usage**: Demonstrates the hash table operations with a few sample key-value pairs.
    4. **Performance Testing**: Tests the hash table's performance with 1000 key-value pairs, 
       measuring and printing the average time taken for insert, search, and delete operations.

This program provides a comprehensive implementation of a hash table that effectively handles 
collisions and maintains efficient performance, making it a useful data structure for scenarios 
where fast insertion, deletion, and search operations are needed.
"""




import time

class HashTable:
    def __init__(self, size=10):
        # Initialize the hash table with a fixed initial size.
        # The hash table is a list of lists (chains) to handle collisions using chaining.
        self.size = size
        self.table = [[] for _ in range(self.size)]  # Initialize the table with empty chains.
        self.num_elements = 0  # Keep track of the number of elements in the hash table.

    def _hash_function(self, key):
        # Simple hash function to compute the index for a given key.
        # Uses a prime number (31) to distribute keys uniformly across the table.
        prime = 31
        # Generate a hash value based on the characters in the key.
        return sum((ord(char) * prime ** i) for i, char in enumerate(str(key))) % self.size

    def _resize(self):
        # Resize the hash table when the load factor exceeds a threshold.
        # Create a new table with double the current size.
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]

        # Rehash all existing elements into the new table to maintain uniform distribution.
        for chain in self.table:
            for key, value in chain:
                index = self._hash_function(key) % new_size
                new_table[index].append((key, value))
        
        # Update the table and its size.
        self.size = new_size
        self.table = new_table

    def insert(self, key, value):
        # Insert a key-value pair into the hash table.
        # If the load factor exceeds 0.7, resize the table to maintain efficiency.
        if self.num_elements / self.size > 0.7:
            self._resize()

        # Compute the hash index for the key.
        index = self._hash_function(key)
        
        # Check if the key already exists in the chain.
        for i, kv in enumerate(self.table[index]):
            k, v = kv
            if k == key:
                # If key exists, update the value and return.
                self.table[index][i] = (key, value)
                return
        
        # If the key does not exist, append the key-value pair to the chain.
        self.table[index].append((key, value))
        self.num_elements += 1  # Increase the number of elements.

    def search(self, key):
        # Search for a value associated with the given key.
        # Compute the hash index for the key.
        index = self._hash_function(key)

        # Traverse the chain at the computed index to find the key.
        for k, v in self.table[index]:
            if k == key:
                return v  # Return the value if the key is found.
        
        # Return None if the key is not found in the chain.
        return None

    def delete(self, key):
        # Delete a key-value pair from the hash table.
        # Compute the hash index for the key.
        index = self._hash_function(key)

        # Traverse the chain to find and remove the key-value pair.
        for i, kv in enumerate(self.table[index]):
            k, v = kv
            if k == key:
                # Remove the key-value pair if found and return True.
                del self.table[index][i]
                return True
        
        # Return False if the key is not found in the chain.
        return False

    def display(self):
        # Display the current state of the hash table for debugging purposes.
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")

# Function to measure time for each operation.
def measure_time(hash_table, operation, key=None, value=None):
    # Record the start time before the operation.
    start_time = time.time()

    # Perform the specified operation on the hash table.
    if operation == 'insert':
        hash_table.insert(key, value)
    elif operation == 'search':
        result = hash_table.search(key)
    elif operation == 'delete':
        hash_table.delete(key)
    
    # Record the end time after the operation.
    end_time = time.time()
    
    # Return the time taken for the operation.
    return end_time - start_time

# Example usage section to demonstrate basic hash table operations.
print("=== Example Usage ===")
hash_table = HashTable()

# Insert some key-value pairs into the hash table.
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)

# Search for keys in the hash table and print the results.
print(hash_table.search("apple"))   # Output: 1
print(hash_table.search("banana"))  # Output: 2
print(hash_table.search("grape"))   # Output: None (key not found)

# Delete a key from the hash table.
hash_table.delete("banana")
print(hash_table.search("banana"))  # Output: None (key has been deleted)

# Display the current state of the hash table.
hash_table.display()

# Performance testing section to measure average times for hash table operations.
print("\n=== Performance Testing ===")
hash_table = HashTable()  # Create a new hash table for performance testing.

# Data for testing with 1000 key-value pairs.
keys = [f"key{i}" for i in range(1000)]
values = [i for i in range(1000)]

# Measure and record time for insert operations.
insert_times = [measure_time(hash_table, 'insert', key, value) for key, value in zip(keys, values)]

# Measure and record time for search operations.
search_times = [measure_time(hash_table, 'search', key) for key in keys]

# Measure and record time for delete operations.
delete_times = [measure_time(hash_table, 'delete', key) for key in keys]

# Calculate and display the average time taken for each operation.
print(f"Average Insert Time: {sum(insert_times) / len(insert_times)} seconds")
print(f"Average Search Time: {sum(search_times) / len(search_times)} seconds")
print(f"Average Delete Time: {sum(delete_times) / len(delete_times)} seconds")

# Display the final state of the hash table after all operations for verification.
print("\nFinal state of the hash table after performance testing:")
hash_table.display()

