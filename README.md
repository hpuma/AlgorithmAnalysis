# Algorithm Analysis
A program that tests widely known algorithms with any n size input.
<br  /> The algorithms implemented are: 
<br  /> **-InsertionSort
<br  /> -MergeSort
<br  /> -HeapSort
<br  /> -QuickSort
<br  /> -QuickSort** (Adjustable Pivot)

### File Overview:

```bash
  algorithm_implementations.py     # Algorithm implementations that undergo testing
  algorithm_test_data.txt 		     # Program output for exponentially increasing input sizes
  algorithm_testing_functions.py 	 # Program tool implementations that test the algorithms
  main.py                          # Driver program that tests all the algorithms
 ```
 
 ----------
 
### Useful Functions in main.py (Driver File)

Supplementary functions that can also be used

```Python
#  1. Creates and returns a random list of list_size size.
def BuildList(list_size):
```
list_size: the size of the randomly generated list.

-----------

```Python
#  2. Checks to see if the input list is currently sorted.
def isSorted(A):
```
A: the input array that gets checked whether it is sorted or not.
It starts by beginning from the second element and checking whether the previous
element is smaller than the current element.

-----------

```Python
#  3. Prints the contents of any given list and prints its context when printed.
def print_list(A, before):
```
A: the input array that gets checked.
before: boolean value that represents the context of the printed list.

-----------

### Algorithm Analysis functions in main.py (Driver File)
       
-----------

```Python
#  4.Tests an algorithms individual run time with a given list input. 
def algorithm_test(algorithm,test_list,p=0,r=0):
```
    algorithm: Algorithm that will have its run time tested. The algorithm names are the options above with no quotation marks.
    test_list: Unsorted list that will be sorted by the input algorithm.
    OPTIONAL PARAMETERS: Parameters that are needed for QuickSort and QuickSort (Pivot)
    p: The index of the first element
    r: The index of the last element
    
-----------

```Python
#  5. Tests all algorithms on a random array with a specific size
def test_all_algorithms(list_size):
```
    list_size: The size of the input list that will be used on the algorithms
    
-----------
