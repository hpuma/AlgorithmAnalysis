from insertion_sort import InsertionSort
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
def algorithm_test(algorithm,test_list):
    wrapped_algorithm = fwrap(algorithm,test_list)
    print("Testing:\t", algorithm.__name__)
    print("Time:\t",timeit.timeit(wrapped_algorithm))
    print("Output:",test_list)
    

# Tests all the algorithms
def test_all_algorithms(list_size):
    print("Generating Random List:\tn =",list_size)
    random_list = BuildList(list_size)
    if len(random_list) <= 100:
        print(random_list)
    algorithm_test(InsertionSort,list.copy(random_list))

# ALGORITHM TOOLS
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