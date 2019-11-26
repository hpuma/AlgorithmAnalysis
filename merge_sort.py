import math
import sys
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
testArr = [1,3,5,2,6]
print("Before:\t",testArr)
MergeSort(testArr,0,4)
print("After:\t",testArr)