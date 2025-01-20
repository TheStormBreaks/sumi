def swap(arr, i, j):
    # swaps the elements of the array present at index i, j
    arr[i], arr[j] = arr[j], arr[i]

def selectionSort(arr):
    # This algorithm picks the minimum element from the unsorted array and place it in the
    # start of the unsorted array
    length = len(arr)
    # The outer loop executes n-1 times, as we need n-1 passes to sort the array
    for i in range(length-1):
        minIndex = i 
        # the inner loop finds the minimum element index in the unsorted array
        for j in range(i+1,length):
            if arr[minIndex] > arr[j]:
                minIndex = j
        
        if minIndex != i:
            swap(arr, i, minIndex)
        print(arr)    
        
if __name__ == "__main__":
    selectionSort([12, 34, 11, 10, 9, 8])
