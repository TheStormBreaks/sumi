def bubbleSort(array):
    # Loop to access each array element
    for i in range(len(array)):
        # Loop to compare array elements
        for j in range(0, len(array) - i - 1):
            # Compare two adjacent elements
            # Change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # Swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

data = [-2, 45, 0, 11, -9]
bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)