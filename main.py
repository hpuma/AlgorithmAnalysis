from algorithm_implementations import InsertionSort, MergeSort, HeapSort, QuickSort, QuickSortPivot
from algorithm_testing_functions import algorithm_test, test_all_algorithms
import sys
import time

# PREPARING TO RUN ALGORITHM FUNCTIONS
# Allowing the computer to process input where  n > 10^4
# This is done by modifying your python's recursion limit
print("OLD RECURSION LIMIT:\t",sys.getrecursionlimit())
sys.setrecursionlimit(1000100)
print("NEW RECURSON LIMIT:\t",sys.getrecursionlimit())

 # Timestamping the beginning of the algorithm analysis
print("Test_Start_Time:\t",time.ctime(time.time()),end="\n\n")

# TESTING ALL THE ALGORITHMS WITH DIFFERENT SIZE INPUTS
# FUNCTION FORMAT: test_all_algorithm(Random_list_size)
test_all_algorithms(10)
test_all_algorithms(100)
test_all_algorithms(1000)
test_all_algorithms(100000)  # Running both functions below may take a while because of insertion sort O(n^2), consider commenting these out
test_all_algorithms(1000000)


# TESTING EACH INDIVIDUAL ALGORITHM
# FUNCTION FORMAT:(ALGORITHM_NAME ,[LIST] , P , R) 
# NOTE : P and R parameters if applicable
# P and R are necessary for some algorithms to run recursivly 
# P: Index of the first element
# R: Indes of the last element

# algorithm_test(InsertionSort, [1,4,6,2,1,6,7])
# algorithm_test(MergeSort, [1,4,6,2,1,6,7],0,6)
# algorithm_test(HeapSort, [1,4,6,2,1,6,7])
# algorithm_test(QuickSort, [1,4,6,2,1,6,7],0,6)
# algorithm_test(QuickSortPivot, [1,4,6,2,1,6,7],0,6)


# Timestamping the end of the algorithm analysis
print("Test_End_Time:\t",time.ctime(time.time()),end="\n\n") 