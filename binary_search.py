#Algorithm to find a target in an sorted list.

data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 25

def binary_search_iterative(data, target):
	low = 0
	high = len(data) - 1

	while low <= high:
		mid = (low + high) // 2
		if target == data[mid]:
			return f"{target} is at index {mid} in the list"
		elif target < data[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return f"{target} is not in the list" 

print(binary_search_iterative(data,target))

def binary_search_recursive(data, target, low, high):
	if low > high:
		return f"{target} is not in the list" 
	else:
		mid = (low + high) // 2
		if target == data[mid]:
			return f"{target} is at index {mid} in the list"
		elif target < data[mid]:
			return binary_search_recursive(data, target, low, mid-1)
		else:
			return binary_search_recursive(data, target, mid+1, high)


print(binary_search_recursive(data,19, 0, len(data)-1))
