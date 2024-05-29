"""
Author: Loi Chai Lam
Date: 29 May 2024

Red Light Camera Detector using Dijkstra Algorithm
Assignment 4

Problem:

The program aims to develop a red - light camera detection application for Alice, 
which helps her avoid intersections with red - light cameras. 
The app identifies the k closest cameras from a given starting vertex, 
ensuring the paths avoid both toll roads and intersections with cameras.




Requirement:
- Let V and E denote the number of vertices and edges, respectively. 
The solution must have O(V log V + E log V ) time complexity (in the worst-case) to determine the k closest cameras.
The total time complexity required to print the shortest paths to these k cameras must be
O(V log V + E log V + P) where P is the total number of edges printed in the output, i.e., the
total number of edges on the shortest paths to these k cameras. 




Input:
There are two input files, vertexes and edges files. Vertexes input file contains number of vertexes 
that have the red-light camera and edges input file contains edges between the vertexs.
The total number of vertices are 6105 and you can assume that their IDs are in the range 0 to 6104.

Below are the first 5 lines from vertices input file denoting that the vertices 1, 5, 12, 16 and 20
have red-light cameras.

1
5
12
16
20

Below are some lines from edges input file. The first two values in each row correspond to the
vertices that the edge connects and the third value corresponds to the distance between the
vertices (i.e., the length of the edge). Some rows have four values where the
fourth value is TOLL denoting that this edge is a toll road. 

122 127 526.950012
123 125 228.396591
124 138 544.010193 TOLL
125 126 259.437286

For example, the third line below shows that there is an edge between vertices with IDs 124 and 138. 
The length of this road segment is 544.010193 and this is a toll road.



Output:
The program must ask the user to enter their location (vertex ID) and the value of k. It must
then display k-closest cameras considering only the safe paths. It must also display the safe
path to each of these cameras. 

Below is a sample output:

Enter your location: 1609
Enter k: 3
Camera 1 : 1595 Distance from your location: 89.02904600000001
Shortest path: 1609 --> 1600 --> 1593 --> 1595
Camera 2 : 1624 Distance from your location: 143.87629700000002
Shortest path: 1609 --> 1600 --> 1607 --> 1624
Camera 3 : 1648 Distance from your location: 170.821331
Shortest path: 1609 --> 1622 --> 1616 --> 1625 --> 1627 --> 1636 --> 1648

Note that there is a camera at vertex 1580 with distance 166.19017100000002 but it is not
returned in the above output because the shortest path to this camera passes through another
camera (at intersection 1595), i.e., the path is not a safe path. Below are the details of the
camera (and the shortest path to it) that must be ignored by your algorithm:

Camera : 1580 Distance from your location: 166.19017100000002
Shortest path: 1609 --> 1600 --> 1593 --> 1595 --> 1578 --> 1580


Below is another sample output:

Enter your location: 2011
Enter k: 2
Camera 1 : 1999 Distance from your location: 21.692297
Shortest path: 2011 --> 1999
Camera 2 : 1991 Distance from your location: 302.152092
Shortest path: 2011 --> 2016 --> 4563 --> 2003 --> 1985 --> 1976 --> 1991

There is a path to camera at intersection 4529 with distance 238.061092 but it is ignored
because the path contains a toll road. Below is a path to this camera which is invalid (i.e., not
safe) because it contains a toll road:

Camera : 4529 Distance from your location: 238.061092
Shortest path: 2011 --> 2016 --> 4563 --> 4556 --> 4549 --> 4543 --> 4541
--> 4529

For the above camera, the road segment 4543 --> 4541 is a toll road so this path must NOT
be considered by your algorithm. 


The shortest path to 4529 that does not pass through any
toll road or any other camera is shown below:

Camera : 4529 Distance from your location: 474.407198
Shortest path: 2011 --> 2016 --> 4563 --> 4556 --> 3433 --> 3446 --> 4557
--> 4545 --> 4542 --> 4529

This camera is not among the 2-closest cameras because its safe distance is 474.407198 which
is greater than the safe distances of the top-2 cameras (1999 and 1991).


If the user is already on an intersection with red-light camera (i.e., the entered location is
a vertex with camera), then the algorithm prints a message stating that it is not possible to
avoid the red-light cameras. 
Below is a sample output:

Enter your location: 2010
Enter k: 5
Oops! Cannot help, Alice!!! Smile for the camera!


In some cases, it is possible that the k-closest cameras cannot be found (e.g., there may be
less than k cameras that can be reached without passing through any toll road or any other
camera). In this case, your algorithm must return only the cameras that can be reached. For
example, assume that you are on a vertex v that has only two adjacent vertices u and x and
both u and x have red-light cameras. If k > 2, the algorithm will return only u and x because
no other cameras can be reached without passing through an intersection with a camera.
In a case, where no camera can be reached (e.g., Alice is on a vertex for which all adjacent
edges are toll roads), your program must print "Oops! You’re stuck here Alice!"



Thought:
In this assignment, I use Dijkstra’s algorithm to find the shortest safe path. I use min-heap to 
implement the Dijkstra’s algorithm to reduce its complexity. 

I use 3 classes to implement the feature, Min-Heap class, Edge class and Vertex class. 
In Vertex class, I have vertex, camera, and previous  attributes. While in Edge class, 
I have u (from vertex), v (to vertex), and weight attributes. I have a
vertices array in my Min-Heap to keep track of the location of vertices in Min-heap array.

First, I process the vertices input file to get an array of classes of vertices. It includes the information of 
the present of camera (which in the Vertex class). The preprossesing takes O(V) time and space 
complexity as I need to loop through all the Vertices. Second, I process the edges input file. I use adjacency 
list to store the neighbour vertices of a vertex. In the big adjacency list, it has an array of Edge classes, 
which indicates the neighbour of of each Vertex. The time complexity is O(E) as I need to loop through 
all the edges, while the space complexity is O(E+V) as the adjacency list need E+V space to store it. 

In Dijkstra’s algorithm, my discovered array is a Min-heap; I have a cameraResult array to store the 
destination camera vertices. When the length of cameraResult array equal to k, the algorithm will stop 
and return the cameraResult array. I loop through all the vertices and all the edges. When inserting a 
new vertices or changing the weight of the vertices, it needs O(logV) time complexity. When getting 
the minimum weight of the vertex, it needs O(log V) time complexity. Hence, the time complexity of 
Dijkstra’s algorithm is O(ElogV+VlogV) which is O(ElogV) time complexity. The space complexity is 
O(E+V) since I use an adjacency list to store the edges.

When backtracking the path and printing the result, I get the destination camera vertex from the 
cameraResult which returned from the Dijkstra’s algorithm. Since, there is a previous attribute in my 
Vertex class, I can use current = current.previous to loop through the path until current is equal to the 
source vertex. I store the path in the shortPath array, later I print the result from shortPath aray. The 
time and space complexity of backtracking and printing result are O(P), where P is the totalnumber of 
edges printed im the output.

From above, the total time complexity is O(ElogV+P), while the total space complexity is O(E+V+P)

"""
from minheap import MinHeap
from edgesnvertex import *


def arrayCamera(filename, numVertex):
    """
    Create an array of class of vertices from file given
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
        tmp_array[line] = Vertex(line, True)
    file.close()

    for i in range(numVertex):
        if tmp_array[i] is None:
            tmp_array[i] = Vertex(i, False)
    return tmp_array


def adjList(filename, verticesList, numVertex):
    """
    Create an adjacency list using class of vertices and class of edges from file given
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


def dijkstra(numVertex, maps, source, k):
    """
    Dijkstra algorithm which find the shortest safe path
    source = [vertex(class),distance]
    time = O(ElogV + VlogV)
    space = O(E+V)
    arg: numVertex = number of vertices
        maps = array of adjacency list
        source = source vertex with distance 0
        k = k-closest camera
    """
    discovered = MinHeap(numVertex)
    cameraResult = []
    counter = 0

    discovered.add(source)

    if source[0].camera == True:
        print("Oops! Cannot help, Alice!!! Smile for the camera!")
        return cameraResult

    while not (discovered.empty()):
        item = discovered.get_min()
        uvertex = item[0]
        uweight = item[1]
        uedges = maps[int(uvertex.vertex)]
        if len(uedges) == 0:
            print("Oops! Cannot help, Alice!!! Smile for the camera!")
            return cameraResult

        if uvertex.camera == True:
            cameraResult.append([uvertex, uweight])
            counter += 1
        if counter == k:
            return cameraResult

        if uvertex.camera == False:
            for i in uedges:
                if discovered.vertices[int(i.v.vertex)] == -2:  # if v not in Discovered or Finalized
                    discovered.add([i.v, float(uweight + i.weight)])
                    i.v.previous = i.u
                elif discovered.vertices[int(i.v.vertex)] > 0:  # if v is not in Finalized
                    if uweight + i.weight < discovered.array[discovered.vertices[i.v.vertex]][1]:
                        discovered.update_min([i.v, float(uweight + i.weight)])
                        i.v.previous = i.u


def backtrackPath(camera, source):
    """
    time:O(p), p is the path of 1 camera
    space:O(p)
    """
    shortPath = []
    current = camera[0]
    while current.vertex != source[0].vertex:
        shortPath.append(current.vertex)
        current = current.previous
    shortPath.append(source[0].vertex)
    return shortPath


def printResult(cameraList, source):
    """
    time:O(P), P is the total number of edges printed in the output
    space:O(P)
    """
    for i in range(len(cameraList)):
        distance = cameraList[i][1]
        string = "Shortest path: "
        shortPath = backtrackPath(cameraList[i], source)
        print("Camera " + str(i + 1) + " : " + str(cameraList[i][0].vertex) + "   Distance from your location : " + str(distance))
        for j in range(len(shortPath) - 1, 0, -1):
            string += str(shortPath[j]) + " --> "
        string += str(shortPath[0])
        print(string)
        print()


if __name__ == "__main__":
    arrCam = arrayCamera('./Sample Data/cameraDetectorVerticesSampleData.txt', 6105)
    maps = adjList('./Sample Data/cameraDetectorEdgesSampleData.txt', arrCam, 6105)
    sourceLo = int(input("Enter your location: "))
    k = int(input("Enter k: "))
    source = [arrCam[sourceLo], 0]  # 2011 2010
    cameraResult = dijkstra(6105, maps, source, k)
    printResult(cameraResult, source)
