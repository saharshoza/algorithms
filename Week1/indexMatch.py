import numpy as np

def indexMatch(leftArr,rightArr):

	print leftArr
	print rightArr

	checkRight = 0
	checkLeft = 0

	mid = leftArr.shape[0]/2
	if leftArr[leftArr.shape[0] - 1] == 0:
		return 1
	elif leftArr[leftArr.shape[0] -1] >= 0:
		checkLeft = indexMatch(leftArr[:mid],leftArr[mid:])

	mid = rightArr.shape[0]/2
	if rightArr[rightArr.shape[0] - 1] == 0:
		return 1
	elif rightArr[0] <= 0:
		checkRight = indexMatch(rightArr[:mid],rightArr[mid:])

	return max(checkLeft,checkRight)

if __name__ == "__main__":
	inArr = np.array([-31,-2,0,1,10,25,46,87])
	idxArr = np.linspace(1,inArr.shape[0],inArr.shape[0])
	inArr = inArr - idxArr
	mid = inArr.shape[0]/2
	print indexMatch(inArr[:mid],inArr[mid:])