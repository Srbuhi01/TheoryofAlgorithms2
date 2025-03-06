import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk


G = nx.DiGraph()
G.add_edges_from([(1,2),(1,3),(2,4),(3,4),(3,5),(4,5), (4,6), (5,6)])
nx.draw(G, with_labels = True, arrows = True, node_size = 500, node_color = "green", font_size = 20 )
plt.show()

root = tk.Tk()
root.title("Graph display title")
button = tk.Button(root, text = "show graph", command = showgraph)
button.pack (padx = 20, pady = 20)
root.mainloop()
