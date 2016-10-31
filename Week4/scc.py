import resource, sys
import numpy as np

#graphDict = {1: [4], 2: [8], 3: [6], 4: [7], 5: [2], 6: [9], 7: [1], 8: [5, 6], 9: [3, 7]}
leaderDict = {}
currTime = 0
exploredSet = set([])
timeDict = {}
currLeader = 0

def dfs_routine(inGraph,vertex):
	global currTime
	if vertex not in exploredSet:
		exploredSet.add(vertex)
		leaderDict[currLeader].append(vertex)
	if vertex in inGraph:
		for slaveIter in inGraph[vertex]:
			if slaveIter not in exploredSet:
				dfs_routine(inGraph,slaveIter)
	currTime = currTime +  1
	timeDict[vertex] = currTime

def build_graph(filename):
	f = open(filename)
	contentList = f.read().split('\n')
	graphDict = {}
	for inIter in range(0,len(contentList)):
		vertex = int(contentList[inIter].split(' ')[0])
		edge = int(contentList[inIter].split(' ')[1])
		if vertex not in graphDict:
			graphDict[vertex] = [edge]
		else:
			graphDict[vertex].append(edge)
	return graphDict

if __name__ == "__main__":

	resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
	sys.setrecursionlimit(10**6)
	graphDict = build_graph(sys.argv[1])
	reverseGraph = {}

	for key in graphDict:
		for value in graphDict[key]:
			if value in reverseGraph:
				reverseGraph[value].append(key)
			else:
				reverseGraph[value] = [key]

	vertexList = range(1,max(max(graphDict.keys()),max(reverseGraph.keys()))+1)
	vertexList.reverse()

	print 'Start first pass'

	for vertexIter in vertexList:
		if vertexIter not in exploredSet:
			currLeader = vertexIter
			leaderDict[currLeader] = []
			exploredSet.add(vertexIter)
			dfs_routine(reverseGraph,vertexIter)

	exploredSet = set([])

	timeGraph = {timeDict[k]:v for (k,v) in graphDict.items()}
	for key in timeGraph:
		timeGraph[key] = [timeDict[i] for i in timeGraph[key]]

	leaderDict = {}
	for vertexIter in vertexList:
		if vertexIter not in exploredSet:
			currLeader = vertexIter
			leaderDict[currLeader] = [currLeader]
			exploredSet.add(vertexIter)
			dfs_routine(timeGraph,vertexIter)

	print len(leaderDict)
	sccLen = np.array([len(v) for (k,v) in leaderDict.items()])
	sccLen.sort()
	sccLen[:] = sccLen[::-1]
	if sccLen.shape[0] <= 5:
		print sccLen[0:]
	else:
		print sccLen[0:5]
