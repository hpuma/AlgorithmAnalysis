from algorithm_implementations import swap
from random import randrange
# QUICK SORT
def Partition(A,p,r):
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
    return Partition(A,p,r)
def QuickSort(A,p,r):
    if(p < r):
        q = Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,p+1,r)

def QuickSortPivot(A,p,r):
    if(p < r):
        q = PartitionPivot(A,p,r)
        QuickSortPivot(A,p,q-1)
        QuickSortPivot(A,q+1,r)
testArr = [6,3,4,2,1]
print("Before:\t",testArr)
QuickSortPivot(testArr,0,4)
print("After:\t",testArr)

