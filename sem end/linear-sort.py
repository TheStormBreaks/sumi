''' 
if data is not sorted, we cannot perform binary search and left with one choice of linear search.
Function linearSearch() searches target key in datalist. 
'''

def linearSearch(dataList, target):
    # dataList is the list of elements in which linearSearch function seaches for target key
    # for loop iterates for each element of datalist
    for ele in dataList:
	#if any element of dataList is equal to target then return True
        if ele == target:
            return True
    # the next statment will be executed only if none of the dataList element is equal to target key, hence return False
    return False


print(linearSearch([10,13, "hello"], 20))