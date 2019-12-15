from tools import test_all_algorithms
import sys
import time
# Allowing the computer to process n > 10000
# This is done by hopefully modifying the recursion limit
print("OLD R LIMIT:\t",sys.getrecursionlimit())
sys.setrecursionlimit(1000002)
print("NEW R LIMIT:\t",sys.getrecursionlimit())
print("Test_Start_Time:\t",time.ctime(time.time()),end="\n\n")
test_all_algorithms(10)
# test_all_algorithms(100)
test_all_algorithms(1000)
# test_all_algorithms(100000)
# test_all_algorithms(1000000)
print("Test_End_Time:\t",time.ctime(time.time()),end="\n\n")