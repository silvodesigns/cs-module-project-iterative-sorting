# TO-DO: Complete the selection_sort() function below
#-----0-1--2--3--4
#arr [1-10-22-50-20]
def selection_sort(arr):
    # loop through n-1 elements
    n = len(arr)
    for i in range(0, len(arr) - 1):
        cur_index = i 
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i + 1,  n):
          if(arr[j] < arr[smallest_index]):
            #update if smaller is found
            smallest_index = j
                 
        # TO-DO: swap
        # Your code here
        temp = arr[i]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
# 10, 5, 14, 99, 3 ,2
def bubble_sort(arr):
    # Your code here
    #loop thru the array
    sorting = True
    while sorting:
      sorting = False
      for i in range(0, len(arr) - 1 ):
        #each time I loop thru it compare pointer to value next to it
        if arr[i] > arr[i+1]:
        #if the value is biggger than the value to my right, swap position
          temp = arr[i + 1]
          arr[i + 1] = arr[i]
          arr[i] = temp
          sorting = True
        #keep looping until no more swaps are done
    
    return arr
    

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
