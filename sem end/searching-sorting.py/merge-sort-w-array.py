""" This version of merge sort creates a new merged array, every time merge_sorted_arrays 
function is called, hence this version is not efficient in terms of space complexity"""

# This method merges two sorted arrays arrA and arrB. 
def merge_sorted_arrays(arrA, arrB):
    # compute the length of arrA and arrB
    lenA = len(arrA)
    lenB = len(arrB)
    
    
    sortedArray = [] # mered array
    
    i = j = 0  # i is used for indexing into arrA, j is used for indexing into arrB
    
    while i < lenA and j < lenB:
        # if ith element of arrA is less than jth element of arrB
        #then append the element of arrA into sortedArray.
        if arrA[i] < arrB[j]:
            sortedArray.append(arrA[i])
            i += 1 
        else: # else append the jth element of arrB into sortedArray.
            sortedArray.append(arrB[j])
            j += 1
     # If arraA still has elements, then append the remaining elements of arrA in sortedArray     
    while i < lenA:
        sortedArray.append(arrA[i])
        i += 1
    
     # If arraB still has elements, then Append the remaining elements of arrB in sortedArray      
    while j < lenB:
        sortedArray.append(arrB[j])
        j += 1 
    print("Merged Array : ",sortedArray) 
    return sortedArray
def mergeSort(arr):
    # base case of the recursive mergeSort function, if len of array is one then return the array
    # else divide the array in two halves and recursively apply merge sort on left half and right half arrays
    # and then merge the sorted left and right arrays
    if len(arr) <= 1: 
        return arr
    mid = len(arr)//2
    left = arr[: mid]
    right = arr[mid:]
    
    left  = mergeSort(left)
    right = mergeSort(right)
    return merge_sorted_arrays(left, right)
if __name__ == "__main__":
    # calling mergeSort function
    mergeSort([1, 7 , 2, 4, 10, 13])
