
def insertion_sort_ascending(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        # Move elements of lst[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

# Define a function for insertion sort in descending order
def insertion_sort_descending(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        # Move elements of lst[0..i-1] that are less than key
        # to one position ahead of their current position
        while j >= 0 and key > lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

# Initial list of numbers
numbers = [1, 72, 81, 25, 65, 91, 11]

# Sort the list in ascending order
ascending_sorted = insertion_sort_ascending(numbers[:])  # Use a copy of the list to preserve the original order

# Sort the list in descending order
descending_sorted = insertion_sort_descending(numbers[:])  # Use a copy of the list to preserve the original order

# Print the results
print("Original list:", numbers)
print("Sorted in ascending order:", ascending_sorted)
print("Sorted in descending order:", descending_sorted)
