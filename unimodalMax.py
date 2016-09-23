import numpy as np

def split(leftArr, rightArr):

	if leftArr.shape[0] <= 2:
		leftMax = np.max(leftArr)
	elif leftArr[leftArr.shape[0]-1] > leftArr[leftArr.shape[0] -2]:
		leftMax = leftArr[leftArr.shape[0]-1]
	else:
		mid = leftArr.shape[0]/2
		leftMax = split(leftArr[:mid],leftArr[mid:])

	if rightArr.shape[0] <= 2:
		rightMax = np.max(rightArr)
	elif rightArr[rightArr.shape[0]-1] > rightArr[rightArr.shape[0]-2]:
		rightMax = rightArr[rightArr.shape[0]-1]
	else:
		mid = rightArr.shape[0]/2
		rightMax = split(rightArr[:mid],rightArr[mid:])		

	return max(rightMax,leftMax)

if __name__ == "__main__":
	inArr = np.array([1,2,3,4,5,6,4,3,2,1])
	mid = inArr.shape[0]/2
	print split(inArr[:mid],inArr[mid:])