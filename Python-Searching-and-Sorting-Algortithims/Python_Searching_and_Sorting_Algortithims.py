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
    midpoint = i + ((k - i) >> 1)
    pivot = arr[midpoint]
    temp = 0
    done = False
    
    while(not done):
        while(pivot > arr[i]): i+=1
        while(pivot < arr[k]): k-=1
        
        if(i >= k): done = True
        else: 
            temp = arr[i]
            arr[i] = arr[k]
            arr[k] = temp
            
            i+=1
            k-=1
    return k
         

def quickSort(arr, i, k):
    
    if(i >= k): return
    
    j = quickSortPartition(arr, i, k)
    
    quickSort(arr, i, j) #left partition call
    quickSort(arr, j + 1, k) #right partition call