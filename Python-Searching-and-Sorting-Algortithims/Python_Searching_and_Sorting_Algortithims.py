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
        else: return midpoint
    return -1 

def quickSortParition(arr, i, k):
    pivot = (i + k) << 1
    l = i, r = k, temp = 0
    
    while(r - l > 1):
        while(arr[pivot] > arr[l]): ++l
        while(arr[pivot] < arr[r]): --r
        
        if(r - l > 1):
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
        ++i
        --r
        
    #Pivot value is new upper bound for left parition and lower bound for high partion
         

def quickSort(arr, i, k):
    
    

   
    
