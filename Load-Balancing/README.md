Given an array A of length n, where A[i] denotes time a task takes to complete. Your job is to choose two tasks and remove them, such that if you assign continuos range of tasks amongst three workers, then each workers turnaround time should be same. Input a single line of space separated numeric values and return True if it is possible to do so else return False.
  
  Example 1
  
  Input:
  1 3 4 2 2 2 1 1 2
  
  Output: True
  
  Choosing A[2] and A[5], and removing them, we have subarrays: [1, 3], [2, 2], [1, 1, 2]
  
  W1 = 1 + 3
  
  W2 = 2 + 2
  
  W3 = 1 + 1 + 2
    
  Example 2: 

  Input:
  1 1 1 1 1 1
    
  Output: False
