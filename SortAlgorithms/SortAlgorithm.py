#
# This program is a collection of Sorting Algorithms implemented.
#

#
# Swap function: It takes two indexes and the dataset and swap the values of the two indexs of the dataset.
#                Swap function is the key function in most of the sorting algorithms.
#
def swap(dataset, idx1, idx2):
    if idx1 != idx2:
        dataset[idx1], dataset[idx2] = dataset[idx2], dataset[idx1]

###############################################################################################
# Bubble Sort - Complexity: O(n*n)
def bubbleSort(dataset):
    for idx1 in range(len(dataset) - 1, 0, -1):
        for idx2 in range(idx1):
            if dataset[idx2] > dataset[idx2 + 1]:
                swap(dataset, idx2, idx2 + 1)
        
        # Print the iteration.
        print('Iteration: ', dataset)

###############################################################################################
# Insertion Sort - Complexity:: Best Case - O(n), Worst Case - O(n*n)
def insertionSort(dataset):
    for idx1 in range(1, len(dataset)):
        # Get the current item.
        currItem = dataset[idx1]
        
        idx2 = idx1 - 1
        
        while idx2 >= 0 and dataset[idx2] > currItem:
            dataset[idx2 + 1] = dataset[idx2]
            idx2 -= 1
        
        dataset[idx2 + 1] = currItem
        
        # Print the iteration.
        print('Iteration: ', dataset)

###############################################################################################
# Selection Sort - Complexity: O(n*n)
def selectionSort(dataset):
    for idx1 in range(len(dataset) - 1):
        # Set the minimum element position, initially 0.
        minPos = idx1

        # Get the minimum element index in the rest of the dataset.
        for idx2 in range(idx1 + 1, len(dataset)):
            if dataset[idx2] < dataset[minPos]:
                minPos = idx2

        # Swap the minimum value with the current value to make the minimum element at the first.
        swap(dataset, minPos, idx1)

        # Print the iteration.
        print('Iteration: ', dataset)

###############################################################################################
# Merge Sort - Complexity: O(n log n)
def mergeSort(dataset):
    # Get the size of the dataset.
    size = len(dataset)

    # Exit condition of merge sort divide recursion.
    if size == 1:
        return dataset
    
    # Calculate the middle index.
    midIdx = size // 2

    # Divide/Slice the dataset at the middle index.
    leftData = dataset[:midIdx]
    rightData = dataset[midIdx:]

    # Recursive Calls of Merge Sort function to divide the left and right data.
    leftDataSet = mergeSort(leftData)
    rightDataSet = mergeSort(rightData)

    # Merge the two sorted datasets.
    return mergeData(leftDataSet, rightDataSet)

#
# This function merges two sorted datasets.
#
def mergeData(leftArr, rightArr):
    # Initialize the left and right indexes.
    leftIdx = rightIdx = 0

    # Get the legth of left and right datasets.
    leftLenght = len(leftArr)
    rightLenght = len(rightArr)

    # Merge the two sorted datasets into third dataset in sorted order.
    mergedArr = []

    while leftIdx < leftLenght and rightIdx < rightLenght:
        if leftArr[leftIdx] <= rightArr[rightIdx]:
            mergedArr.append(leftArr[leftIdx])
            leftIdx += 1
        else:
            mergedArr.append(rightArr[rightIdx])
            rightIdx += 1
        
    # Append any remaining items of any of the datasets.
    while leftIdx < leftLenght:
        mergedArr.append(leftArr[leftIdx])
        leftIdx += 1

    while rightIdx < rightLenght:
        mergedArr.append(rightArr[rightIdx])
        rightIdx += 1

    # Return the merged dataset.
    return mergedArr

###############################################################################################
#
# Quick Partition: This fuction is used in Quick Sort algorithm to divide the dataset into two sub-datasets
#                  based on the pivot element in the dataset.
#
def qPartition(dataset, start, end):
    # Set the pivot index at the start index of the dataset and get the pivot element from the dataset.
    pivotIdx = start
    pivotElement = dataset[pivotIdx]
    
    # Traverse the process until start and end pointers cross each other.
    while start <= end:
        # Increment the start pointer while start pointer value is less than the length of the dataset and
        # element in start position is less (or equal to) than the pivot element.
        while start < len(dataset) and dataset[start] <= pivotElement:
            start += 1
        
        # Decrement the end pointer while element in the end position is greter (or equal to) 
        # than the pivot element.
        while dataset[end] >= pivotElement:
            end -= 1

        # When the start position finds the element less than pivot and the end position finds the element
        # greater than pivot, then swap the two elements. The only condition of this swap is the start 
        # and end pointers did not crossed.
        if start < end:
            swap(dataset, start, end)
        
    # When the start and end pointers crossed, then swap the pivot element with the end element.
    swap(dataset, pivotIdx, end)

    # Retrun the end postion as pivot position.
    return end

#
# This is main recursive logic of quick sort.
#
def qsortRecursion(dataset, start, end):
    # Exit criteria of the recursion.
    # if the start position is less than end position i.e. there is more than one element in the dataset.
    if start < end:
        pivotIndex = qPartition(dataset, start, end)
        qsortRecursion(dataset, start, pivotIndex - 1)
        qsortRecursion(dataset, pivotIndex + 1, end)

# Quick Sort (Using Hoare partition scheme) - Complexity:: Average Case - O(n log n), Worst Case - O(n * n).
def quickSort(dataset):
    # Initialize start and end positions.
    start = 0
    end = len(dataset) - 1
    
    # Call the quick sort recursion processs.
    qsortRecursion(dataset, start, end)

###############################################################################################
# Shell Sort - using gap = n/2 : Complexity: Best Case - O(n log n), Worst Case - O(n * n).
def shellSort(dataset):
    # Get the size of the ddataset and set the Gap value.
    size = len(dataset)
    gap = size // 2

    # Process until the Gap is not zero.
    while gap > 0:
        for idx1 in range(gap, size):
            # Get the anchor element.
            anchor = dataset[idx1]

            # Initialize index2
            idx2 = idx1

            # When the index2 is greater than or equal to gap and previous element in gap distance is greater than the anchor element,
            # move the previous gap element to the position of anchor element and decrement the index2 by gap step.
            while idx2 >= gap and dataset[idx2 - gap] > anchor:
                dataset[idx2] = dataset[idx2 - gap]
                idx2 -= gap
            
            # Place the anchor element in the sorted place so that all elements at the left side of it are less than it and all the elements
            # at the right side of it are greater than it.
            dataset[idx2] = anchor   

        # Print the iterations.
        print('Gap: ', gap, 'Iteration: ', dataset) 

        # Get the new gap value.
        gap = gap // 2
            

