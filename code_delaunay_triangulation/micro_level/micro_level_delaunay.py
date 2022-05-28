import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

circ_color = [0.1,1,0.1]
node_color = '#F1F1F4'
border_color = 'white'
edge_color = 'white'
node_size = 200
bg_color = [0,0,0]


pause_time = 1.2


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


def draw_circles(T):
    print("DRAW CIRCLES ")
    # T = (v1_c,v2_c, v3_c )
    my_circ = cercle_circonscrit(T)
    Drawing_uncolored_circle = plt.Circle( my_circ[0], my_circ[1] , fill = False, color=circ_color, linestyle = "dashed",linewidth=1,zorder=0)
    ax.add_artist( Drawing_uncolored_circle )


 
g = nx.Graph()


# fig, ax = plt.subplots()





fig = plt.figure()
ax = fig.add_subplot(111)

fig.set_size_inches(18.5, 10.5)
fig.set_dpi(100)
# plt.rcParams["figure.figsize"] = [7.00, 3.50]
# plt.rcParams["figure.autolayout"] = True
# plt.rcParams['axes.facecolor'] = 'black'
# plt.rcParams['figure.facecolor'] = 'black'


ax.set_xlim([-20,120])
ax.set_ylim([-20,120])
ax.set_aspect( 1 )
# ax.set_facecolor(bg_color) 



pos=nx.get_node_attributes(g,'pos')
nx.draw(g, pos, with_labels = True)
plt.pause(pause_time) 
plt.grid()


# ---------------------         SCENE 1         -----------------------------------------------------------
plt.cla()
g.add_node(1,pos=(20,20))
g.add_node(2,pos=(15,40))
g.add_node(3,pos = (17,60))
g.add_node(4,pos = (38,53))
g.add_node(5,pos = (35,35))
g.add_node(6,pos = (36,20))
g.add_node(7,pos = (60,20))
g.add_node(8,pos = (65,40))
g.add_node(9,pos = (46,64))


circle1 = plt.Circle((0, 0), 0.2, color='r')
g.add_edge(1, 2 , color=edge_color)
g.add_edge(2, 3 , color=edge_color)
g.add_edge(3, 4 , color=edge_color)
g.add_edge(2, 4 , color=edge_color)
g.add_edge(4, 5 , color=edge_color)
g.add_edge(2, 5)
g.add_edge(1, 5)
g.add_edge(1, 6)
g.add_edge(5, 6)
g.add_edge(6, 7)
g.add_edge(5, 7)
g.add_edge(8, 7)
g.add_edge(8, 5)
g.add_edge(8, 4)
g.add_edge(9, 4)
g.add_edge(9, 3)
g.add_edge(9, 8)


pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time) 


# ---------------------         SCENE 2 - new point        -----------------------------------------------------------
plt.cla()
g.add_node(10,pos = (26,43))




pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time) 


# ---------------------         SCENE 3 - new edges        -----------------------------------------------------------
plt.cla()

g.add_edge(10,2)
g.add_edge(10,4)
g.add_edge(10,5)





pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time) 

# ---------------------         SCENE 4  test triangle 1      -----------------------------------------------------------
plt.cla()

T = ((15,40),(38,53),(26,43))
draw_circles(T)




pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time) 

# ---------------------         SCENE 5  remove edge      -----------------------------------------------------------
plt.cla()
g.remove_edge(2,4)



pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time) 

# ---------------------         SCENE 6  add fli[] edge      -----------------------------------------------------------
plt.cla()
g.add_edge(3,10)



pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time)  

# ---------------------         SCENE 7  add fli[] edge      -----------------------------------------------------------
plt.cla()
T = ((26,43),(17,60),(38,53))
draw_circles(T)



pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time) 

# ---------------------         SCENE 8     -----------------------------------------------------------
plt.cla()




pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time)  


# ---------------------         SCENE 9  add fli[] edge      -----------------------------------------------------------
plt.cla()
T = ((26,43),(17,60),(15,40))
draw_circles(T)



pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time) 

# ---------------------         SCENE 10     -----------------------------------------------------------
plt.cla()




pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time) 

# ---------------------         SCENE 11  add fli[] edge      -----------------------------------------------------------
plt.cla()
T = ((26,43),(38,53),(35,35))
draw_circles(T)



pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time) 

# ---------------------         SCENE 12    -----------------------------------------------------------
plt.cla()




pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time)  

# ---------------------         SCENE 13  add fli[] edge      -----------------------------------------------------------
plt.cla()
T = ((26,43),(15,40),(35,35))
draw_circles(T)



pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time) 

# ---------------------         SCENE 14    -----------------------------------------------------------
plt.cla()




pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time)  

# ---------------------         SCENE 15   -----------------------------------------------------------
plt.cla()
g.remove_edge(2,5)



pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time)

# ---------------------         SCENE 16    -----------------------------------------------------------
plt.cla()
g.add_edge(10,1)



pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time)  


# ---------------------         SCENE 17  add fli[] edge      -----------------------------------------------------------
plt.cla()
T = ((26,43),(15,40),(20,20))
draw_circles(T)



pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time) 

# ---------------------         SCENE 18    -----------------------------------------------------------
plt.cla()
g.add_edge(10,1)



pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time)  


# ---------------------         SCENE 19  add fli[] edge      -----------------------------------------------------------
plt.cla()
T = ((26,43),(35,35),(20,20))
draw_circles(T)



pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time) 

# ---------------------         SCENE 18    -----------------------------------------------------------
plt.cla()
g.add_edge(10,1)



pos=nx.get_node_attributes(g,'pos')
colors = nx.get_edge_attributes(g,'color').values()
nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color, edge_color=colors)
fig.set_facecolor(bg_color)
plt.pause(pause_time)  


# # ---------------------         SCENE 2         -----------------------------------------------------------
# g.add_edge(4,3)
# T = ((1,1),(20,20),(1,20))
# draw_circles(T)


# pos=nx.get_node_attributes(g,'pos')
# nx.draw(g, pos, with_labels = True, node_color=node_color, node_size= node_size, edgecolors = border_color)
# plt.pause(pause_time) 





plt.show()