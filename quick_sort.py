from tools import swap

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

testArr = [6,3,4,2,1]
print("Before:\t",testArr)
QuickSort(testArr,0,4)
print("After:\t",testArr)