import numpy as np

def fiveSort(arrayIn):
	arrayIn.sort()
	return arrayIn

def partition(inArr,pivot):
	pivotLoc = 0
	leftArr = np.zeros((0,))
	rightArr = np.zeros((0,))
	for i in range(0,inArr.shape[0]):
		if inArr[i] < pivot:
			pivotLoc += 1
			leftArr = np.hstack((leftArr,inArr[i]))
		elif inArr[i] > pivot:
			rightArr = np.hstack((rightArr,inArr[i]))
	print pivotLoc
	print rightArr
	print leftArr
	return pivotLoc, rightArr, leftArr

def dSelect(inArr,arrayLen,orderStatistic,flag):
	
	if arrayLen <= 5:
		inArr.sort()
		print inArr
		if flag == 0:
			return inArr[orderStatistic]
		else:
			return inArr[(arrayLen-1)/2]

	if arrayLen%5 == 0:
		medianArr = np.zeros((arrayLen/5))
		iterRange = arrayLen/5
	else:
		medianArr = np.zeros((arrayLen/5 + 1))
		iterRange = arrayLen/5 + 1

	for i in range(0,iterRange):
		if i == iterRange - 1:
			tempArr = inArr[i*5:]
		else:
			tempArr = inArr[i*5:(i+1)*5]
		fiveOut = fiveSort(tempArr)
		medianArr[i] = fiveOut[fiveOut.shape[0]/2]
	print medianArr
	pivot = dSelect(medianArr,medianArr.shape[0],orderStatistic,1)
	print pivot
	pivotLoc, rightArr, leftArr = partition(inArr,pivot)

	print orderStatistic
	if pivotLoc == orderStatistic:
		return pivot
	elif pivotLoc > orderStatistic:
		return dSelect(leftArr,leftArr.shape[0],orderStatistic,0)
	elif pivotLoc < orderStatistic:
		return dSelect(rightArr,rightArr.shape[0],orderStatistic - pivotLoc - 1,0)

if __name__ == "__main__":
	inArr = np.random.randn(20)
	print inArr
	orderStatistic = np.random.choice(range(0,20))
	#orderStatistic = 16
	print dSelect(inArr,inArr.shape[0],orderStatistic,0)
	inArr.sort()
	print inArr[orderStatistic]
	print orderStatistic
	print inArr