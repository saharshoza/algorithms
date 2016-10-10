import numpy as np

def bruteForce(inputX):
	leastDistance = 1000000000000
	for i in range(0,inputX.shape[0]):
		for j in range(i+1,inputX.shape[0]):
			diff = inputX[i] - inputX[j]
			leastDistance = min(leastDistance,np.sqrt(np.power(diff[0],2) + np.power(diff[1],2)))
	return leastDistance

def closest(inputX,inputY):

	if inputX.shape[0] <= 3:
		#This is constant time as not dependent on n
		return bruteForce(inputX)

	mid = inputX.shape[0]/2

	# Recursion
	leftLeast = closest(inputX[0:mid],inputY[0:mid])
	rightLeast = closest(inputX[mid:],inputY[mid:])

	delta = min(leftLeast,rightLeast)

	# For any 2 points on different sides of left/right to be closer, they must have distance less than delta
	stripPoints = inputY[np.where(abs(inputY[:,0] - inputX[mid,0]) < delta)]

	# Brute force to find distance between these points. (Always linear time and capped at 7)
	iterLoop = 0
	for i in range(0,stripPoints.shape[0]):
		for j in range(i+1,stripPoints.shape[0]):
			diff = stripPoints[i] - stripPoints[j]
			dist = np.sqrt(np.power(diff[0],2) + np.power(diff[1],2))
			leastDistance = min(delta,dist)
			iterLoop += 1 

	#print iterLoop
	return leastDistance

if __name__ == "__main__":
	inputPoints = np.array([[2,3],[12,30],[40,50],[5,1],[12,10],[3,4]])
	#Sort the inputs by x and y first in O(nlogn)
	inputX = inputPoints[np.argsort(inputPoints[:,0])]
	inputY = inputPoints[np.argsort(inputPoints[:,1])]
	print closest(inputX,inputY)