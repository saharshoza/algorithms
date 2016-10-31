f = open('scc.txt')
contentList = f.read().split('\n')
graphDict = {}
print len(contentList)
for inIter in range(0,len(contentList)):
	vertex = int(contentList[inIter].split(' ')[0])
	edge = int(contentList[inIter].split(' ')[1])
	if vertex not in graphDict:
		graphDict[vertex] = [edge]
	else:
		graphDict[vertex].append(edge)
print len(graphDict)#
print graphDict[875707]
#875707