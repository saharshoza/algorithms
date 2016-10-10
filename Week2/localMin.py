import numpy as np

MatSize = 100
inMat = np.random.rand(MatSize,MatSize)

def getLocMin(rowNum):
	print rowNum
	if(rowNum == 0 or rowNum == MatSize - 1):
		return inMat[rowNum,np.argmin(inMat[rowNum])]
	else:
		rowMinIdx = np.argmin(inMat[rowNum])
		print rowMinIdx
		minCol = np.argmin(np.array([inMat[rowNum-1,rowMinIdx],inMat[rowNum,rowMinIdx],inMat[rowNum+1,rowMinIdx]]))
		print minCol
		if(minCol == 1):
			return inMat[rowNum,rowMinIdx]
		elif(minCol == 0):
			locMin = getLocMin(rowNum-1)
		elif(minCol == 2):
			locMin = getLocMin(rowNum+1)
	return locMin

if __name__ == "__main__":
	print inMat
	locMin = getLocMin(MatSize/2)
	print locMin