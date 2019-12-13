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