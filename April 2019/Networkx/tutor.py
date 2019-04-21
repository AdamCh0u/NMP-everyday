#%%
import networkx as nx
G=nx.Graph()
# In NetworkX, nodes can be any hashable object e.g.,
# a text string, an image, an XML object, another Graph, a customized node object
#%%
# Nodes generate
G.add_node(1)
G.add_nodes_from([2, 3])
## iterable container of nodes
H = nx.path_graph(10)
G.add_nodes_from(H)
##  the graph H as a node in G.
# G.add_node(H)
#$$The graph G now contains H as a node.

#%%
## edge
G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)
#G.add_edges_from([(1, 2), (1, 3)])

#%%
G.add_nodes_from("spam") # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_node("spam")        # adds node "spam"
G.number_of_nodes()
# 重复运行不添加，nodes 不重复？

#%%
G.number_of_edges()

#%%
list(G.nodes)
list(G.edges)
list(G.adj[1])# or list(G.neighbors(1))
G.degree[1]# the number of edges incident to 1


#%%
G.edges([2,"m"])# 返回指定点的边界
#G.nodes()
#G.remove_edge(1, 3)

#%%
#$$https://networkx.github.io/documentation/stable/tutorial.html#what-to-use-as-nodes-and-edges
G.add_edge(1, 3)
G[1][3]['color'] = "blue"
G.edges[1, 2]['color'] = "red"

#%%
#Each graph, node, and edge can hold key/value attribute pairs in an associated attribute dictionary

G = nx.Graph(day="Friday")
G.graph['day'] = "Monday"
G.add_node(1, time='5pm')

#%%
# Directed Graph
nx.draw(G)

#%%
lollipop = nx.lollipop_graph(10, 20)
nx.draw(lollipop)

#%%
ba = nx.barabasi_albert_graph(100, 5)
nx.draw(ba)

#%%
petersen = nx.petersen_graph()
nx.draw(petersen)

#%%
red = nx.random_lobster(100, 0.9, 0.9)
nx.draw(red)


#%%
# analysis graph
sp = dict(nx.all_pairs_shortest_path(G))
sp[3]

#%%
G = nx.petersen_graph()
plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], 
              with_labels=True, font_weight='bold')

#%%
G = nx.dodecahedral_graph()
shells = [[2, 3, 4, 5, 6], [8, 1, 0, 19, 18, 17, 16, 15, 14, 7], [9, 10, 11, 12, 13]]
options = {'node_color': 'green','node_size': 100,'width': 3,}
nx.draw_shell(G, nlist=shells, **options)