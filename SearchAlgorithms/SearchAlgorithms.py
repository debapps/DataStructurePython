#
# This program implements two popular search algorithms for array: Linear Search and Binary Serch.
# Time Complexity: Linear Search - O(n), Binary Search - O(log n)
#

# Linear Search - This search method traverses all the elements of the dataset to find the desired element. It works 
# on Sorted or Unsorted dataset. Time Complexity: Linear Search - O(n).
def linearSearch(dataset, item):
    index = -1
    isFound = False

    for element in dataset:
        index += 1
        if element == item:
            isFound = True
            break
    
    if isFound:
        return index
    else:
        return -1

# This Method determines if a given dataset is sorted or not.
def isSorted(dataset):
    if len(dataset) == 1:
        return True
    for idx in range(0, len(dataset) - 1):
        if dataset[idx] > dataset[idx + 1]:
            return False
    return True

# Binary Search - This method implements Binary search. Time Complexity: Binary Search - O(log n).
# The characteristic of Binary Search is as follows.
# 1. It takes sorted dataset as input.
# 2. It calculates the mid point of the sorted dataset.
# 3. It compares the item with the mid element, if item found then return the mid position.
# 4. If the item is less than the mid position, then it search in the left portion of the mid position.
# 5. If the item is greter than the mid position, then it search in the right portion of the mid position.
# 6. If the item is not found it returns -1.

def binarySearch(dataset, item):
    # Initialize the start and end positions.
    start = 0
    end = len(dataset) - 1

    # Perform the operations until start crosses the end.
    while start <= end:
        # Calculate the mid position.
        midPos = (start + end) // 2

        if dataset[midPos] > item:
            end = midPos - 1
        elif dataset[midPos] < item:
            start = midPos + 1
        else:
            return midPos
    
    if start > end:
        return -1

# This method searches the given item into the given dataset. It determines search algorithm based on whether 
# the dataset is sorted or not.
def indexOfItem(dataset, item):
    if isSorted(dataset):
        print('Binary Search ..')
        index = binarySearch(dataset, item)
    else:
        print('Linear Search ..')
        index = linearSearch(dataset, item)

    return index
     
