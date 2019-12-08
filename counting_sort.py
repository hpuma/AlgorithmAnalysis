from tools import findMax
def CountingSort(A):
    k = findMax(A)
    C = [None] * (k+1)
    B = [None] * len(A)
    for i in range(0,k+1):
        C[i] = 0
    for j in range(0,len(A)):
        C[A[j]] +=1
    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]
    for j in range(0,len(A)):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    for i in range(0,len(A)):
        A[i] = B[i] 

testArr = [1,3,5,2,6]
print("Before:\t",testArr)
CountingSort(testArr)
print("After:\t",testArr)