""" This version of merge sort doesn't create a new merged array, every time
    sorted arrays are merged into array(arr). hence the space complexity of this version is less"""
# This method merges two sorted arrays arrA and arrB. arr is the merged array. 
def merge_sorted_arrays(arrA, arrB, arr):
    # compute the length of arrA and arrB
    lenA = len(arrA)    
    lenB = len(arrB)
    # i is used for indexing into arrA, j is used for indexing into arrB
    # k is used for indexing into arr

    i = j = k= 0     
         
    while i < lenA and j < lenB:
	# if ith element of arrA is less than jth element of arrB, then add the element of arrA into arr.
        if arrA[i] < arrB[j]:
            arr[k] = arrA[i]
            i += 1 
            k += 1
        else: # else add jth element of arrB into arr. 
            arr[k]=arrB[j]
            j += 1
            k += 1 
    # If arraA still has elements, then Add the remaining elements of arrA in arr 
    while i < lenA:
        arr[k] = arrA[i]
        i += 1
        k += 1 
    # If arraB still has elements, then Add the remaining elements of arrB in arr      
    while j < lenB:
        arr[k] = arrB[j]
        j += 1 
        k += 1 
    #print(arr) 
    
def mergeSort(arr):
    # base case of the recursive mergeSort function, if len of array is one then return the array
    # else divide the array in two halves and recursively apply merge sort on left half and right half arrays
    # and then merge the sorted left and right arrays 
    if len(arr) <= 1: 
        return arr
    mid = len(arr)//2
    left = arr[: mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    merge_sorted_arrays(left, right, arr)
    return arr

if __name__ == "__main__":
    # calling the mergeSort function
    print(mergeSort([90, 89, 78]))
