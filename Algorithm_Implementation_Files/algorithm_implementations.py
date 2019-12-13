import math
import sys
from random import randrange
# AUXILARY FUNCTIONS FOR ALGORITHM IMPLEMENTATIONS
def left(index):
    return (2*index+1)
def right(index):
    return (2*index+2)
def swap(A,a,b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp
def findMax(A):
    max = -sys.maxsize
    for i in A:
        if i > max:
            max = i
    return max
# ALL ALGORITHM IMPLEMENTATIONS
# INSERTION SORT
def InsertionSort(a):
    if(len(a) < 2): # Always check if the input list is big enough to be considered for sorting
        return
    for i in range(1,len(a)): # Start from the second element and traverse the array
        key = a[i] # Store the list value at the current index
        j = i-1 # Store the index before the current index, this will be used to sort the current index
        while(j > -1 and a[j] > key): # From the current index, traverse backwards until you reach an index whose list value is less than the current value "key"
            a[j+1] = a[j] # Move the larger list values to the right as you look back
            j-=1 
        a[j+1] = key # Once you find a list value smaller than the current item, then add the current value "key" in front of it

# MERGE SORT
def MergeSort(A,p,r):
    if(p < r):
        q = math.floor((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p,q,r)
def Merge(A,p,q,r):
    n1 = q - p+1
    n2 = r - q
    L = [None] *(n1+1)
    R = [None] *(n2+1)

    for i in range(0,n1):
        L[i] = A[p+i]
    for j in range(0,n2):
        R[j] = A[q+j+1]
    L[n1] = sys.maxsize
    R[n2] = sys.maxsize
    i = 0
    j = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1

# HEAP SORT
def HeapSort(A):
    if len(A)<=1:
        return A
    buildMaxHeap(A)
    last_index = len(A) 
    for i in range(last_index-1,0,-1):
        swap(A,0,i)
        Heapify(A,i,0)
def Heapify(A,last_index,index):
    largest = index
    if left(index) < last_index and A[left(index)] > A[index]:
        largest = left(index)
    else:
        largest = index
    if right(index) < last_index and A[right(index)] > A[largest]:
        largest = right(index)
    
    if(largest != index):
        swap(A,index,largest)
        Heapify(A,last_index,largest)
def buildMaxHeap(A):
    if len(A) <= 1:
        return A
    for i in range(len(A),-1,-1):
        Heapify(A,len(A),i)
    
# QUICK SORT PIVOT LAST INDEX (REGULAR)
def Partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if(A[j] <= x):
            i+=1
            swap(A,i,j)
    swap(A,i+1,r)
    return i+1
def QuickSort(A,p,r):
    if(p < r):
        q = Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)
# QUICKSORT WITH RANDOM PIVOT (Lomuto Partitioning)
def PartitionPiv(A,p,r):
    x = A[r]
    i = p
    for j in range(p,r):
        if(A[j] <= x):
            swap(A,i,j)
            i+=1
    swap(A,i,r)
    return i
def PartitionPivot(A,p,r):
    rand_pivot = randrange(p,r+1)
    swap(A,rand_pivot,r)
    return PartitionPiv(A,p,r)
def QuickSortPivot(A,p,r):
    if(p < r):
        q = PartitionPivot(A,p,r)
        QuickSortPivot(A,p,q-1)
        QuickSortPivot(A,q+1,r)