import numpy as np
import sys

def graphCreate(graphIn):
	graphStructure = {}
	graphIn = open(graphIn)
	graphList = graphIn.read().split('\n')
	for i in range(0,len(graphList)):
		vertexList = graphList[i].split('\t')
		singleVertex = int(vertexList[0])
		graphStructure[singleVertex] = [int(x) for x in vertexList[1:len(vertexList)-1]]
	#print graphStructure
	return graphStructure

if __name__ == "__main__":
	graphDict = graphCreate(sys.argv[1])
	print graphDict
	superNodeDict = {}
	superNodeNum = 1
	vertexNum = len(graphDict)
	minCut = vertexNum*vertexNum
	maxIter = 1000
	randIter = 0

	while randIter < maxIter:
		graphDict = graphCreate(sys.argv[1])
		superNodeDict = {}
		superNodeNum = 1
		while len(graphDict) > 2:
			keyList = [k for (k,v) in graphDict.items()]
			vertexOne = np.random.choice(keyList,1)[0]
			vertexTwo = graphDict[vertexOne][np.random.choice(len(graphDict[vertexOne]),1)[0]]
			#print vertexOne, vertexTwo
			superNodeDict[vertexNum+superNodeNum] = [vertexOne,vertexTwo]
			graphDict[vertexOne].remove(vertexTwo)
			#print graphDict
			#print vertexOne
			#print graphDict[vertexTwo]
			graphDict[vertexTwo].remove(vertexOne)
			#print graphDict
			graphDict[vertexOne].extend(graphDict[vertexTwo])
			#print graphDict
			graphDict.pop(vertexTwo,None)
			#print graphDict
			for key in graphDict:
				graphDict[key] = [x if x not in superNodeDict[vertexNum+superNodeNum] else vertexNum+superNodeNum for x in graphDict[key]]
			#print graphDict
			graphDict = {k if k not in superNodeDict[vertexNum+superNodeNum] else vertexNum+superNodeNum:v for (k,v) in graphDict.items()}
			for key in graphDict:
				while key in graphDict[key]:
					graphDict[key].remove(key)
			#print graphDict[vertexNum+superNodeNum]
			superNodeNum += 1
			#print superNodeNum
			#print graphDict
			#print superNodeDict
		for key in graphDict:
			minCutIter = len(graphDict[key])
			break;
		print minCutIter
		randIter += 1
		if minCutIter < minCut:
			minCut = minCutIter
		print randIter
	print minCut
