from random import randrange
import sys
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

# Working Heapsort
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