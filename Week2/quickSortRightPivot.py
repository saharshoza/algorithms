import numpy as np
compareCount = 0

def partition(inputArr,left,right):
	pivotElement = inputArr[right]
	i = right - 1
	iterStart = i
	rangeList = range(left,iterStart+1)
	rangeList.reverse()
	for j in rangeList:
		global compareCount
		compareCount += 1
		if inputArr[j] < pivotElement:
			temp = inputArr[i]
			inputArr[i] = inputArr[j]
			inputArr[j] = temp
			i = i - 1
	temp = inputArr[right]
	inputArr[right] = inputArr[i+1]
	inputArr[i+1] = temp
	pivot = i+1
	return inputArr, pivot


def quickSort(inputArr,left, right):

	#print inputArr
	#print left
	#print right 

	if left > right:
		return inputArr
	elif right - left <= 1:
		if inputArr[left] < inputArr[right]:
			temp = inputArr[left]
			inputArr[left] = inputArr[right]
			inputArr[right] = temp
		return inputArr
	else:
		inputArr, pivot = partition(inputArr,left,right)
		inputArr = quickSort(inputArr,left,pivot-1)
		inputArr = quickSort(inputArr,pivot+1,right)
		return inputArr


if __name__ == "__main__":
	inputArr = np.array([3,8,2,4,1,6,7,5])
	outArr = quickSort(inputArr,0,inputArr.shape[0]-1)
	print compareCount