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

def quickSortPartition(arr, i, k):
    pivot = (i + k) >> 1
    l = i
    r = k
    temp = 0
    done = False
    
    while(not done):
        while(arr[pivot] > arr[l]): l+=1
        while(arr[pivot] < arr[r]): r-=1
        
        if(l >= r): done = True
        else: 
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            
            l+=1
            r-=1
    return r
         

def quickSort(arr, i, k):
    
    if(i >= k): return
    
    j = quickSortPartition(arr, i, k)
    
    quickSort(arr, i, j) #left partition call
    quickSort(arr, j + 1, k) #right partition call