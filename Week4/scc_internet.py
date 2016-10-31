import resource, sys

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

def strongly_connected_components_iterative(vertices, edges):
    """
    This is a non-recursive version of strongly_connected_components_path.
    See the docstring of that function for more details.

    Examples
    --------
    Example from Gabow's paper [1]_.

    >>> vertices = [1, 2, 3, 4, 5, 6]
    >>> edges = {1: [2, 3], 2: [3, 4], 3: [], 4: [3, 5], 5: [2, 6], 6: [3, 4]}
    >>> for scc in strongly_connected_components_iterative(vertices, edges):
    ...     print(scc)
    ...
    set([3])
    set([2, 4, 5, 6])
    set([1])

    Example from Tarjan's paper [2]_.

    >>> vertices = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> edges = {1: [2], 2: [3, 8], 3: [4, 7], 4: [5],
    ...          5: [3, 6], 6: [], 7: [4, 6], 8: [1, 7]}
    >>> for scc in  strongly_connected_components_iterative(vertices, edges):
    ...     print(scc)
    ...
    set([6])
    set([3, 4, 5, 7])
    set([8, 1, 2])

    """
    identified = set()
    stack = []
    index = {}
    boundaries = []

    for v in vertices:
        if v not in index:
            to_do = [('VISIT', v)]
            while to_do:
                operation_type, v = to_do.pop()
                if operation_type == 'VISIT':
                    index[v] = len(stack)
                    stack.append(v)
                    boundaries.append(index[v])
                    to_do.append(('POSTVISIT', v))
                    # We reverse to keep the search order identical to that of
                    # the recursive code;  the reversal is not necessary for
                    # correctness, and can be omitted.
                    to_do.extend(
                        reversed([('VISITEDGE', w) for w in edges[v]]))
                elif operation_type == 'VISITEDGE':
                    if v not in index:
                        to_do.append(('VISIT', v))
                    elif v not in identified:
                        while index[v] < boundaries[-1]:
                            boundaries.pop()
                else:
                    # operation_type == 'POSTVISIT'
                    if boundaries[-1] == index[v]:
                        boundaries.pop()
                        scc = set(stack[index[v]:])
                        del stack[index[v]:]
                        identified.update(scc)
                        yield scc

if __name__ == "__main__":
    resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
    sys.setrecursionlimit(10**6)
    graphDict = build_graph(sys.argv[1])
    maxVal = 0
    for key in graphDict:
        maxVal = max(maxVal,max(graphDict[key]))
    print maxVal
    keyList = [k for (k,v) in graphDict.items()]
    if 416780 in keyList:
        print 'hi'
    vertices = range(1,maxVal+1)
    print (set(keyList) - set(vertices))
    print graphDict[416780]
    #vertices = [k for (k,v) in graphDict.items()]
    for scc in strongly_connected_components_iterative(vertices, graphDict):
        print(scc)