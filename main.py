from algorithm_implementations import InsertionSort, MergeSort, HeapSort, QuickSort, QuickSortPivot
from algorithm_testing_functions import algorithm_test, test_all_algorithms
import sys
import time

# Allowing the computer to process n > 10000
# This is done by hopefully modifying the recursion limit
print("OLD R LIMIT:\t",sys.getrecursionlimit())
sys.setrecursionlimit(1000100)
print("NEW R LIMIT:\t",sys.getrecursionlimit())
print("Test_Start_Time:\t",time.ctime(time.time()),end="\n\n")

# TESTING ALL THE ALGORITHMS
# Format test_all_algorithm(Random_list_size)
test_all_algorithms(10)
test_all_algorithms(100)
test_all_algorithms(1000)
test_all_algorithms(100000)
test_all_algorithms(1000000)

# TESTING EACH INDIVIDUAL ALGORITHM
# Format (ALGORITHM_NAME ,[LIST] , P , R) 
# NOTE : P and R parameters if applicable

# algorithm_test(InsertionSort, [1,4,6,2,1,6,7])
# algorithm_test(MergeSort, [1,4,6,2,1,6,7],0,6)
# algorithm_test(HeapSort, [1,4,6,2,1,6,7])
# algorithm_test(QuickSort, [1,4,6,2,1,6,7],0,6)
# algorithm_test(QuickSortPivot, [1,4,6,2,1,6,7],0,6)
print("Test_End_Time:\t",time.ctime(time.time()),end="\n\n")