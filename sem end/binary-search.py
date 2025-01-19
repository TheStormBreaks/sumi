''' Two prerequisites for performing binarySearch are: 
1. Data must be in sorted order(ascending/descending order)
2. Data Structure used to data store must allow access of data elements using index numbers eg. Array

the function binarySearch performs the binarySearch (searchs target key) on dataList (data stored in ascending order)  
The function returns True if target is prsent in dataList, else returns False
'''
def binarySearch(dataList, target, low, high):
    # if low value is greater than high, it means target is not present in dataList, hence return False 
    if (low > high):
        return False
    
    # else compute the mid of the dataList
    mid = (low + high) // 2   
    
    # if mid element of dataList is equal to target key, then return True (target key found) 
    if target == dataList[mid]:
        return True
        
        
    # else if target is smaller than mid element, then perform binary search in the first half(high = mid-1) of the dataList
    elif target < dataList[mid]:
        return binarySearch(dataList, target, low, mid -1)
        
        
    #else target is greater than mid element, then perform binary search in the second half(low = mid+1) of the dataList
    else:
        return binarySearch(dataList, target, mid +1, high)
        
        

print(binarySearch([10, 20, 30, 40, 50], 20, 0, 4))  