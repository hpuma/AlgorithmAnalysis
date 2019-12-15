import math
import sys
from random import randrange
# Python file containing all of the algorithm implementations

# AUXILARY FUNCTIONS FOR ALGORITHM IMPLEMENTATIONS
def left(index): # Left and right functions for heapsort
    return (2*index+1)
def right(index):
    return (2*index+2)
def swap(A,a,b): # Swap items in index a and b
    temp = A[a]
    A[a] = A[b]
    A[b] = temp
# ALL ALGORITHM IMPLEMENTATIONS
# INSERTION SORT
def InsertionSort(A):
    if(len(A) < 2): # Always check if the input list is big enough to be considered for sorting
        return
    for i in range(1,len(A)): # Start from the second element and traverse the array
        key = A[i] # Store the list value at the current index
        j = i-1 # Store the index before the current index, this will be used to sort the current index
        while(j > -1 and A[j] > key): # From the current index, traverse backwards until you reach an index whose list value is less than the current value "key"
            A[j+1] = A[j] # Move the larger list values to the right as you look back
            j-=1 
        A[j+1] = key # Once you find a list value smaller than the current item, then add the current value "key" in front of it

# MERGE SORT
def MergeSort(A,p,r):
    if(p < r):
        q = math.floor((p+r)/2) # Compute the middle of the array
        MergeSort(A,p,q) # Process/Sort the left subarray.
        MergeSort(A,q+1,r) # Process/Sort the right sub array.
        Merge(A,p,q,r) # Comparing the left and right sub array for sorting/
def Merge(A,p,q,r):
    n1 = q - p+1 # Find the sizes of both sub arrays.
    n2 = r - q
    L = [None] *(n1+1) # Create both sub arrays with the extra space for the sentinel value.
    R = [None] *(n2+1)

    for i in range(0,n1): # Add the values from the entire array to their corresponding sub array.
        L[i] = A[p+i]
    for j in range(0,n2):
        R[j] = A[q+j+1]
    L[n1] = sys.maxsize # Add the sentinal value (MAX VALUE) when one sub array has finished, the other gets added to merged/sorted array.
    R[n2] = sys.maxsize
    i = 0 # Pointers for each subarray comparisons
    j = 0
    for k in range(p,r+1):
        # Check if the Left sub array value is smaller,
        # if so add the value from the left sub array and increment its pointer for the next comparison
        # else, the right subarray is smaller and do likewise
        if L[i] <= R[j]: 
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
# HEAP SORT
def Heapify(A,last_index,index): # Setup the input array as a MaxHeap
    largest = index # Set the highest index value
    if left(index) < last_index and A[left(index)] > A[index]: # Check if left child is greater than the root
        largest = left(index)
    else:
        largest = index
    if right(index) < last_index and A[right(index)] > A[largest]: # Check if the right child is greater than the root
        largest = right(index)
    
    if(largest != index): # If the highest index is not the root, then swap the root with the highest index and recall Heapify
        swap(A,index,largest)
        Heapify(A,last_index,largest)
def buildMaxHeap(A): # Apply MaxHeap from the  bottom to the top, or from back to front in an array
    if len(A) <= 1:
        return A
    for i in range(len(A),-1,-1):
        Heapify(A,len(A),i)
def HeapSort(A): # Main Heap Sort function
    if len(A) <= 1:
        return A
    buildMaxHeap(A) # Make the list into a maxheap
    last_index = len(A) 
    for i in range(last_index-1,0,-1):
        swap(A,0,i)
        Heapify(A,i,0)
# QUICK SORT PIVOT LAST INDEX (REGULAR)
# Sorts the sub array and returns the new
# The pivot is always set to the last index
def Partition(A,p,r): 
    x = A[r] # Pick the value at the last element of the array
    i = p-1
    for j in range(p,r):
        if(A[j] <= x):
            i+=1
            swap(A,i,j)
    swap(A,i+1,r)
    return i+1
def QuickSort(A,p,r):
    if(p < r):
        q = Partition(A,p,r) # Find a pivot point that will be used to sort the left and right sub arrays
        QuickSort(A,p,q-1) # Sort the subarray to the left of the pivot
        QuickSort(A,q+1,r) # Sort the subarray to the right of the pivot
# QUICKSORT WITH RANDOM PIVOT (Lomuto Partitioning)
def PartitionPiv(A,p,r): # Regular partitioning by taking the last index as the pivot
    x = A[r]
    i = p
    for j in range(p,r):
        if(A[j] <= x):
            swap(A,i,j)
            i+=1
    swap(A,i,r)
    return i
def PartitionPivot(A,p,r): # Picks a random pivot and sets it as the last element, then performs normal paritioning
    rand_pivot = randrange(p,r+1) # Random pivot
    swap(A,rand_pivot,r) # Swap Random pivot with the last element
    return PartitionPiv(A,p,r)
def QuickSortPivot(A,p,r): # Quick Sort function with random pivot
    if(p < r):
        q = PartitionPivot(A,p,r) # Partition but with a random pivot
        QuickSortPivot(A,p,q-1) # Sort the subaray to the left of the pivot
        QuickSortPivot(A,q+1,r) # Sort the subarray to the right of the pivot