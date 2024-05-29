"""
Author: Loi Chai Lam
Date: 29 May 2024

Dijkstra Algorithm
An algorithm for finding the shortest paths between nodes in a weighted graph, which may represent, 
for example, road networks. It does so by repeatedly selecting the nearest unvisited vertex and 
calculating the distance to all the unvisited neighboring vertices.

"""


def arrayVertex(filename, numVertex):
    """
    Create an array of vertices from file with all vertices listed
    time = O(V)
    space = O(V)
    arg: numVertex = number of vertices
        filename: the file given with data
    """
    tmp_array = [None for i in range(numVertex)]
    file = open(filename, "r", encoding="UTF-8-sig")
    for line in file:
        line = line.strip("\n")
        line = int(line)
        tmp_array[line] = Vertex(line)
    file.close()
    return tmp_array


def adjList(filename, verticesList, numVertex):
    """
    Create an adjacency list using class of vertices and class of edges from file with the vertex and its edge.
    time = O(E)
    space = O(E+V),adjacency list
    arg: numVertex = number of vertices
        filename: the file given with data
        verticesList = an array of of class of vertices created from function arrayCamera
    """
    tmp_array = [[] for i in range(numVertex)]
    file = open(filename, "r", encoding="UTF-8-sig")
    for line in file:
        line = line.strip("\n")
        line = line.split(" ")
        if len(line) == 3:
            tmp_array[int(line[0])].append(Edge(verticesList[int(line[0])], verticesList[int(line[1])], float(line[2])))
            tmp_array[int(line[1])].append(Edge(verticesList[int(line[1])], verticesList[int(line[0])], float(line[2])))
    file.close()
    return tmp_array


def dijkstra(numVertex, maps, source):
    """
    Dijkstra algorithm which find the shortest safe path
    source = [vertex(class),distance]
    time = O(ElogV + VlogV)
    space = O(E+V)
    arg: numVertex = number of vertices
        maps = array of adjacency list
        source = source vertex with distance 0

    """
    discovered = MinHeap(numVertex)
    counter = 0

    discovered.add(source)

    while not (discovered.empty()):
        item = discovered.get_min()
        uvertex = item[0]
        uweight = item[1]
        uedges = maps[int(uvertex.vertex)]
        for i in uedges:
            if discovered.vertices[int(i.v.vertex)] == -2:  # if v not in Discovered or Finalized
                discovered.add([i.v, float(uweight + i.weight)])
                i.v.previous = i.u
            elif discovered.vertices[int(i.v.vertex)] > 0:  # if v is not in Finalized
                if uweight + i.weight < discovered.array[discovered.vertices[i.v.vertex]][1]:
                    discovered.update_min([i.v, float(uweight + i.weight)])
                    i.v.previous = i.u


def backtrackPath(destination, source):
    """
    time:O(p), p is the path of 1 camera
    space:O(p)
    """
    shortPath = []
    current = destination
    while current.vertex != source[0].vertex:
        shortPath.append(current.vertex)
        current = current.previous
    shortPath.append(source[0].vertex)
    return shortPath
