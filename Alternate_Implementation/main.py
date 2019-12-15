from tools import test_all_algorithms,algo_test_all
import sys
# Allowing the computer to process n > 10000
# This is done by hopefully modifying the recursion limit
print("OLD R LIMIT:\t",sys.getrecursionlimit())
sys.setrecursionlimit(1000002)
print("NEW R LIMIT:\t",sys.getrecursionlimit())
algo_test_all(10)
algo_test_all(100)
algo_test_all(100)
algo_test_all(1000)
algo_test_all(10000)