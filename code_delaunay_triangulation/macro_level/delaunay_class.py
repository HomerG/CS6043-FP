import numpy as np

class Triangle:
    def __init__(self, a, b, c):
        self.v = [None,None,None]
        self.v[0] = a
        self.v[1] = b
        self.v[2] = c

        self.edges = [[self.v[0], self.v[1]], [self.v[1], self.v[2]],[self.v[2], self.v[0]]]
        self.neighbour = [None,None,None]

    def Node(self, Node):
        if (self.v[0] == Node) or (self.v[1] == Node) or (self.v[2] == Node):
            return True
        return False


class Delaunay_Triangulation:
    def __init__(self, WIDTH, HEIGHT):
        self.triangulation = []

        self.TempNodeA = Node(-100, -100)
        self.TempNodeB = Node(2 * WIDTH + 100, -100)
        self.TempNodeC = Node(-100, 2 * HEIGHT + 100)

        TempTriangle = Triangle(self.TempNodeA, self.TempNodeB, self.TempNodeC)

        self.triangulation.append(TempTriangle)

    def Insert_Node(self, p):

        bad_triangles = []

        for triangle in self.triangulation:
            if p.IsCircumcircle(triangle):
                bad_triangles.append(triangle)

        polygon = []
        for current_triangle in bad_triangles:
            for this_edge in current_triangle.edges:
                isNeighbour = False
                for other_triangle in bad_triangles:
                    if current_triangle == other_triangle:
                        continue
                    for that_edge in other_triangle.edges:
                        if Common_Edge(this_edge, that_edge):
                            isNeighbour = True
                if not isNeighbour:
                    polygon.append(this_edge)

        for each_triangle in bad_triangles:
            self.triangulation.remove(each_triangle)

        for each_edge in polygon:
            newTriangle = Triangle(each_edge[0], each_edge[1], p)
            self.triangulation.append(newTriangle)

    def Remove_Temporary_Triangle(self):
        onSuper = lambda triangle: triangle.Node(self.TempNodeA) or triangle.Node(self.TempNodeB) or triangle.Node(self.TempNodeC)

        for triangle_new in self.triangulation[:]:
            if onSuper(triangle_new):
                self.triangulation.remove(triangle_new)

    def Get_Values(self):
        ps = [p for t in self.triangulation for p in t.v]
        x_s = [p.x for p in ps]
        y_s = [p.y for p in ps]
        ts = [(ps.index(t.v[0]), ps.index(t.v[1]), ps.index(t.v[2])) for t in self.triangulation]
        return x_s, y_s, ts

    def Find_Neighbours(self):
        for one in self.triangulation:
            edge = 0
            for this_edge in one.edges:
                edge = (edge + 1) % 3
                for other in self.triangulation:
                    if one == other:
                        continue
                    for that_edge in other.edges:
                        if Common_Edge(this_edge, that_edge):
                            one.neighbour[edge] = other

class Node:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, b):
        return Node(self.x + b.x, self.y + b.y)

    def __sub__(self, b):
        return Node(self.x - b.x, self.y - b.y)

    def __mul__(self, b):
        return Node(b * self.x, b * self.y)

    __rmul__ = __mul__

    def IsCircumcircle(self, T):

        a_x = T.v[0].x
        a_y = T.v[0].y
        b_x = T.v[1].x
        b_y = T.v[1].y
        c_x = T.v[2].x
        c_y = T.v[2].y
        d_x = self.x
        d_y = self.y

        incircle = np.array([[a_x - d_x, a_y - d_y, (a_x - d_x) ** 2 + (a_y - d_y) ** 2],[b_x - d_x, b_y - d_y, (b_x - d_x) ** 2 + (b_y - d_y) ** 2],[c_x - d_x, c_y - d_y, (c_x - d_x) ** 2 + (c_y - d_y) ** 2]])

        if np.linalg.det(incircle) > 0:
            return True
        else:
            return False


def Common_Edge(line1, line2):
    if (line1[0] == line2[0] and line1[1] == line2[1]) or (line1[0] == line2[1] and line1[1] == line2[0]):
        return True
    return False