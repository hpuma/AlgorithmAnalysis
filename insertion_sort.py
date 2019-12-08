def InsertionSort(a):
    if(len(a) < 2):
        return
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while(j > -1 and a[j] > key):
            a[j+1] = a[j]
            j-=1
        a[j+1] = key

testArr = [3,7,2,5,8]
print("Before:\t",testArr)
InsertionSort(testArr)
print("After:\t",testArr)