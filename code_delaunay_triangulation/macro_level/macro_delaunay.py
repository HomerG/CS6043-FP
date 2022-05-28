import math
import random
import delaunay_class as d

import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np
import copy 
from math import sqrt

enable_circ = True

regular_color = [0.1,0.23,0.8]
new_color = [0,0.51,0]
bg_color = [0,0,0]
line_color = [1,1,1]
circ_color = [0.3,0.3,0.3]

def cercle_circonscrit(T):
    (x1, y1), (x2, y2), (x3, y3) = T
    A = np.array([[x3-x1,y3-y1],[x3-x2,y3-y2]])
    Y = np.array([(x3**2 + y3**2 - x1**2 - y1**2),(x3**2+y3**2 - x2**2-y2**2)])
    if np.linalg.det(A) == 0:
        return False
    Ainv = np.linalg.inv(A)
    X = 0.5*np.dot(Ainv,Y)
    x,y = X[0],X[1]
    r = sqrt((x-x1)**2+(y-y1)**2)
    return (x,y),r


def draw_circles(triangle_array, xs, ys, ax):
    print("DRAW CIRCLES ")
    for triangle in triangle_array: 
        print(triangle)
        #get nodes
        vertex1 = triangle[0]
        vertex2 = triangle[1]
        vertex3 = triangle[2]

        v1_c = (xs[vertex1], ys[vertex1])
        v2_c = (xs[vertex2], ys[vertex2])
        v3_c = (xs[vertex3], ys[vertex3])
        T = (v1_c,v2_c, v3_c )
        my_circ = cercle_circonscrit(T)
        Drawing_uncolored_circle = plt.Circle( my_circ[0], my_circ[1] , fill = False, color=circ_color, linestyle = "dashed",linewidth=1,zorder=0)
        ax.add_artist( Drawing_uncolored_circle )
        plt.pause(pause_time)


        print(v1_c)
        print(v2_c)
        print(v3_c)


old_triangle_list = []

# ---------------------------------------------------------------------------------



WIDTH = int(100)
HEIGHT = int(100)
n = 5  # n should be greater than 2
length_vertices = 7

pause_time = 1.2

init_x = [60,80,56,82,65,42,29,31,3]
init_y = [60,95,78,20,30,40,3,31,29]
init_z = [0,0,0,0,0,0,0]


xs = [ init_x.pop() for x in range(2)]
ys = [ init_y.pop() for y in range(2)]
zs = [0 for z in range(2)]

print(xs)
print(ys)

col = [regular_color,regular_color]


fig = plt.figure()
ax = fig.add_subplot(111)

fig.set_size_inches(18.5, 10.5)
fig.set_dpi(100)



for loop in range(length_vertices):
    plt.cla()

    ax.set_xlim([-20,120])
    ax.set_ylim([-20,120])
    ax.set_aspect( 1 )

    new_Node_x = init_x.pop()
    new_Node_y = init_y.pop()
    new_Node_z = 0 

    xs.append(new_Node_x)
    ys.append(new_Node_y)
    zs.append(new_Node_z)

    col[-1] = regular_color
    col.append(new_color)

    DT = d.Delaunay_Triangulation(WIDTH, HEIGHT)
    for x, y in zip(xs, ys):
        DT.Insert_Node(d.Node(x, y))

    XS, YS, TS = DT.Get_Values()
    ax.triplot(tri.Triangulation(XS, YS), 'bo--')

    triang = tri.Triangulation(xs, ys)
    nothing_masked = triang.edges
    print("edges")
    print(nothing_masked)

    the_neighbors = triang.neighbors
    triangle_list = triang.get_masked_triangles()
    if loop != 0:
        print("TRIANGLE LISTS")
        print(old_triangle_list)
        print(triangle_list)
    print("neighbors:")
    print(the_neighbors)
    print(" ")
    print("mask: ")
    print(triangle_list)
    print(" ")

    new_xs = []
    new_ys = []
    new_zs = []
    for x in range(len(nothing_masked)):
        for y in range(len(nothing_masked[x])):

            if nothing_masked[x][y] == len(xs)-1:
                new_xs.append(xs[nothing_masked[x][1]])
                new_ys.append(ys[nothing_masked[x][1]])
                new_zs.append(zs[nothing_masked[x][1]])


    print("new node connected to:")
    for i in range(len(new_xs)):
        print("Node ", i+1, ": ", new_xs[i], ",", new_ys[i])


    ax.set_facecolor(bg_color) 

    ax.margins(0.1)
    ax.set_aspect('equal')

    print("x is: ", loop)
    if loop == 0:
        plt.plot(xs[0], ys[0], marker="o", markersize=9, markeredgecolor= line_color, markerfacecolor=new_color, zorder = 10)
        plt.pause(pause_time)

        plt.plot(xs[0], ys[0], marker="o", markersize=9, markeredgecolor= line_color, markerfacecolor=regular_color, zorder = 20)
        plt.plot(xs[1], ys[1], marker="o", markersize=9, markeredgecolor= line_color, markerfacecolor=new_color,zorder = 10)
        plt.pause(pause_time)

        plt.plot(xs[1], ys[1], marker="o", markersize=9, markeredgecolor= line_color, markerfacecolor=regular_color, zorder = 20)
        plt.plot(xs[2], ys[2], marker="o", markersize=9, markeredgecolor= line_color, markerfacecolor=new_color,)
        plt.pause(pause_time)

    #Triangulation
    ax.triplot(triang, color = line_color, mfc="black")

    #Nodes
    plt.scatter(xs,ys, s=80, c=col, edgecolor=line_color, zorder = 1000)




    #Hidden
    if loop != 0:
        for i in range(len(new_xs)):
            plt.plot([xs[-1],new_xs[i]],[ys[-1],new_ys[i]], c=bg_color, linewidth=3)

    plt.pause(pause_time)

    #New edges 
    if loop != 0:
        for i in range(len(new_xs)):
            plt.plot([xs[-1],new_xs[i]],[ys[-1],new_ys[i]], c='white', linestyle = "dashed", linewidth = 1.3)
            plt.pause(pause_time)


    T = ((0, 30), (15, 0), (50, 30))
    my_circ = cercle_circonscrit(T)
    print(my_circ)
    Drawing_uncolored_circle = plt.Circle( my_circ[0], my_circ[1] , fill = False, color='white')
    

    fig.canvas.draw()
    plt.pause(pause_time)


    #Phase 2 - draw new Node and dashed lines and circle 
    if len(init_x) != 0:
        plt.plot(xs[-1], ys[-1], marker="o", markersize=9, markeredgecolor= line_color, markerfacecolor=regular_color, zorder = 1200)

        for i in range(len(new_xs)):
            plt.plot([xs[-1],new_xs[i]],[ys[-1],new_ys[i]], c=line_color, linewidth=1.5)
        plt.pause(pause_time)


    # Phase 3 - finalize step - regular lines regular color
    #New Node
    if len(init_x) != 0:
        plt.plot(init_x[-1], init_y[-1], marker="o", markersize=9, markeredgecolor= line_color, markerfacecolor=new_color)
        plt.pause(pause_time)


    # Closing Phase
    if len(init_x) == 0:
        plt.plot(xs[-1], ys[-1], marker="o", markersize=9, markeredgecolor= line_color, markerfacecolor=regular_color, zorder = 1200)

        for i in range(len(new_xs)):
            plt.plot([xs[-1],new_xs[i]],[ys[-1],new_ys[i]], c=line_color, linewidth=1.5)
        plt.pause(pause_time)



        plt.cla()
        ax.set_xlim([-20,120])
        ax.set_ylim([-20,120])
        ax.set_aspect( 1 )
        DT.Remove_Temporary_Triangle()
        ax.triplot(triang, color = line_color, mfc="black")
        plt.scatter(xs,ys, s=80, c=col, edgecolor=line_color, zorder = 1000)
        plt.plot(xs[-1], ys[-1], marker="o", markersize=9, markeredgecolor= line_color, markerfacecolor=regular_color, zorder = 1200)
        
        plt.pause(pause_time)


    old_triangle_list = triangle_list

plt.show()




