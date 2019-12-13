from algorithm_implementations import InsertionSort,MergeSort,HeapSort,QuickSort,QuickSortPivot
from random import randrange
import timeit
import sys
# ALGORITHM TEST TOOLS

# Creates a random_list of size "list_size" where the range of list values is from 1 to list_size-1
def BuildList(list_size):
    input_values = dict() # Creating an empty dictionary to generate distinct random values
    last_val = list_size + 1 # Last possible range for the randomly generated array
    while (len(input_values) < list_size): # Generating a random int value for each index in the empty list
        rand_key = False # Set a generated random key to false
        while(not rand_key):# Keep generating a random value until we find a value that is not in the dictionary meaning it's unique
            rand_val = randrange(1,last_val)
            if input_values.get(rand_val) == None:# When we have generated a unique int 
                input_values[rand_val] = True
                rand_key = True
    return list(input_values.keys())

# Wraps a function with arguments and returns the same function as a function with no arguments
# This is used alongised timeit.timeit
def fwrap(func,*args,**kwargs):
        def fwrapper():
            return func(*args,**kwargs)
        return fwrapper
# Tests a single algorithm function and Printing it's results
def algorithm_test(algorithm,test_list,p=0,r=0):
    if(p == 0 and r!=0):
        wrapped_algorithm = fwrap(algorithm,test_list,p,r)
    else: 
        wrapped_algorithm = fwrap(algorithm,test_list)
    print("Testing:\t", algorithm.__name__)
    print("Time:\t",round(timeit.timeit(wrapped_algorithm,number=1)*1000.0,6),"ms")
    print("Output:",test_list,end="\n\n")

# Tests all the algorithms
def test_all_algorithms(list_size):
    print("Generating Random List:\tn =",list_size)
    random_list = BuildList(list_size)
    last_index = list_size-1
    if len(random_list) > 0 and len(random_list) <= 100:
        print("Test List:\t",random_list)
    elif len(random_list) > 100 and len(random_list) > 0:
        print("Non-Empty List Length=",len(random_list))
    print("")
    algorithm_test(InsertionSort,list.copy(random_list))
    algorithm_test(MergeSort,list.copy(random_list),0,last_index)
    algorithm_test(HeapSort,list.copy(random_list))
    algorithm_test(QuickSort,list.copy(random_list),0,last_index)
    algorithm_test(QuickSortPivot,list.copy(random_list),0,last_index)