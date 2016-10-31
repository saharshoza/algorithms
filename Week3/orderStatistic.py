import numpy as np

inArr = np.array([3,4,6,7,8,9,1,-2,7,5,0])

def partition(left,right):
	pivot = left
	iterStart = pivot + 1
	partitionLimit = iterStart
	for i in range(iterStart,right+1):
		if inArr[pivot] > inArr[i]:
			temp = inArr[i]
			inArr[i] = inArr[partitionLimit]
			inArr[partitionLimit] = temp
			partitionLimit += 1
	temp = inArr[pivot]
	inArr[pivot] = inArr[partitionLimit-1]
	inArr[partitionLimit-1] = temp
	return partitionLimit-1

def statSearch(statisticOrder,left,right):
	if left == right:
		return inArr[left]
	pivot = partition(left,right)
	print inArr
	print pivot
	if pivot > statisticOrder-1:
		return statSearch(statisticOrder, left, pivot - 1)
	elif pivot < statisticOrder-1:
		return statSearch(statisticOrder, pivot + 1, right)
	else:
		return inArr[pivot]


if __name__ == "__main__":
	statisticOrder = 3
	print statSearch(statisticOrder,0,inArr.shape[0]-1)
