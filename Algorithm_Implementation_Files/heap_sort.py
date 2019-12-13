from math import floor 
from tools import left, right,swap

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
    
def HeapSort(A):
    if len(A) <= 1:
        return A
    buildMaxHeap(A)
    last_index = len(A) 
    for i in range(last_index-1,0,-1):
        swap(A,0,i)
        Heapify(A,i,0)

testArr = [2,7,5,1,3]
print("Before:\t",testArr)
HeapSort(testArr)
print("After:\t",testArr)