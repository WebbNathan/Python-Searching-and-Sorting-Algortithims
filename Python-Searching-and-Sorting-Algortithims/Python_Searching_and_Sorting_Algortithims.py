''' 
Basic sorting and searching alogrithims in Python
Made by Nathan Webb
April 11 2024
'''

def binarySearch(sortedArr, target, leftBound, rightBound):
   midpoint = (leftBound + rightBound) // 2
   while(rightBound - leftBound > 1):
      if(sortedArr[midpoint] < target):
         leftBound = midpoint
         midpoint = (leftBound + rightBound) // 2
      elif(sortedArr[midpoint] > target):
         rightBound = midpoint
         midpoint = (rightBound + leftBound) // 2
      else:
         return midpoint
   if(sortedArr[leftBound] == target):
      return leftBound
   elif(sortedArr[rightBound] == target):
      return rightBound
   else:
      return -1 #Not found

def
   
    
