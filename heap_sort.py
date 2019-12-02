from math import floor 

def left(index):
    return (2*index)+1
def right(index):
    return (2*index)+2
def swap(A,a,b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp
    return A



def Heapify(A,index):
    largest = index
    if left(index) < len(A)-1 and A[left(index)] > A[index]:
        largest = left(index)
    else:
        largest = index
    if right(index) < len(A)-1 and A[right(index)] > A[largest]:
        largest = right(index)
    
    if(largest != index):
        A = swap(index,largest)
        Heapify(A,largest)
    return A

def buildMaxHeap(A):
    if len(A) <= 1:
        return A
    for i in range(floor((len(A))/2),-1,-1):
        A = Heapify(A,i)
    return A


def HeapSort(A):
    if len(A)<=1:
        return A
    last_index = len(A)-1
    A = buildMaxHeap(A)
    for i in range(last_index,0,-1):
        A = swap(A,last_index,i)
        del A[-1]
        A = Heapify(A,0)
    return A