"""
Author: Loi Chai Lam
Date: 29 May 2024

The Edge class and Vertex class used to represent a weighted graph.

"""


class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def __str__(self):
        string = "u: " + str(self.u.vertex) + " " + str(self.u.camera) + " v: " + str(self.v.vertex) + " " + str(self.v.camera) + " weight: " + str(self.weight)
        return string


class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.previous = ""

    def __str__(self):
        string = str(self.vertex) + " " + str(self.camera)
        return string
