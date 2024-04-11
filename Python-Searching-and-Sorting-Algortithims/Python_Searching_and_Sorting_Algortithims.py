''' 
Basic sorting and searching alogrithims in Python
Made by Nathan Webb
April 11 2024
'''

def binarySearch(sortedArr, target, leftBound, rightBound):
   midpoint = (leftBound + rightBound) >> 1
   while(rightBound - leftBound > 1):
      if(sortedArr[midpoint] < target):
         leftBound = midpoint
         if(rightBound - leftBound < 1): return rightBound
         midpoint = (leftBound + rightBound) >> 1
      elif(sortedArr[midpoint] > target):
         rightBound = midpoint
         midpoint = (rightBound + leftBound) >> 1
         if(rightBound - leftBound < 1): return leftBound
      else:
         return midpoint
   return -1 

def quickSortParition(arr, i, k):
   pass

def quickSort(arr, i, k):
   pass

   
    
