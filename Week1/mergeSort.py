import numpy as np

inArray = np.array([4,5,6,7,3,8,1])

def mergeRoutine(rightArray,leftArray):

	outArray = np.zeros((rightArray.size+leftArray.size,1))
	rightArrayIter = 0
	leftArrayIter = 0
	for i in range(0,outArray.size):
		if leftArrayIter == leftArray.size:
			outArray[i] = rightArray[rightArrayIter]
			rightArrayIter += 1
		elif rightArrayIter == rightArray.size:
			outArray[i] = leftArray[leftArrayIter]
			leftArrayIter += 1
		elif rightArray[rightArrayIter] > leftArray[leftArrayIter]:
			outArray[i] = rightArray[rightArrayIter]
			rightArrayIter += 1
		else:
			outArray[i] = leftArray[leftArrayIter]
			leftArrayIter += 1
	return outArray


def mergeSort(inArray):

	print inArray

	if inArray.size == 1:
		return inArray
	if inArray.size == 2:
		if inArray[1] > inArray[0]:
			tempVar = inArray[1]
			inArray[1] = inArray[0]
			inArray[0] = tempVar
		return inArray
	else:
		leftArray = mergeSort(inArray[0:inArray.size/2])
		rightArray = mergeSort(inArray[inArray.size/2:inArray.size])
		recurseResult = mergeRoutine(rightArray,leftArray)
		#print recurseResult
		return recurseResult
		
if __name__ == "__main__":
	print mergeSort(inArray)