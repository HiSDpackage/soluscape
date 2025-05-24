# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import math
import warnings
from matplotlib.cm import Pastel1
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import networkx as nx

warnings.filterwarnings("ignore")


def DrawLandscapeConnection(instance, **kwargs):
	"""
	Draw the image of Solution Landscape.
	"""
	kwargs.setdefault("Title", "The Connection of Saddle Points")
	kwargs.setdefault(
		"TrajectorySet",
		{
			"width": 0.4,
			"style": "solid",
			"edge_color": "blue",
			"label": "Search Trajectory",
		},
	)
	cmap = Pastel1
	colors = [mcolors.rgb2hex(cmap(i % cmap.N)) for i in range(instance.MaxIndex + 1)]
	kwargs.setdefault(
		"SaddlePointSet",
		[
			{
				"node_shape": "o",
				"node_color": colors[i],
				"label": f"Index {i} Saddle Point",
			}
			for i in range(instance.MaxIndex + 1)
		],
	)
	kwargs.setdefault("WhetherSave", False)
	kwargs.setdefault("SaveFigurePath", "Landscape_Connection_figure.png")

	# Create graph and add nodes/edges
	G = nx.Graph()
	H = nx.path_graph(len(instance.SaddleList))
	G.add_nodes_from(H)
	edges = []
	for i in range(len(instance.SaddleList)):
		for j in instance.SaddleList[i][4]:
			if j == -1 or (instance.SaddleList[j][2] <= instance.SaddleList[i][2]):
				continue
			edges.append((instance.SaddleList[i][0], instance.SaddleList[j][0]))
	G.add_edges_from(edges)

	# Sort saddle points by their index
	pos = {}
	tempposList = [[] for i in range(instance.MaxIndex + 1)]
	EachSaddle = [[] for i in range(instance.MaxIndex + 1)]
	for i in range(len(instance.SaddleList)):
		saddleindex = instance.SaddleList[i][2]
		EachSaddle[saddleindex].append(instance.SaddleList[i][0])
	maxn = max([len(EachSaddle[i]) for i in range(len(EachSaddle))])

	# Calculate positions for each saddle point
	for i in range(len(EachSaddle)):
		n = len(EachSaddle[i])
		if n != 0:
			tempposList[i] = [-10 + (j + 1 / 2) * 20 / n for j in range(n)]
	for i in range(len(instance.SaddleList)):
		saddleindex = instance.SaddleList[i][2]
		pos[instance.SaddleList[i][0]] = (tempposList[saddleindex].pop(0), 2*saddleindex)
		EachSaddle[saddleindex].append(instance.SaddleList[i][0])

	# Plot the graph
	plt.figure()
	for i in range(instance.MaxIndex, -1, -1):
		if EachSaddle[i]:
			nx.draw_networkx_nodes(
				G,
				pos,
				nodelist=EachSaddle[i],
				node_size=math.ceil(3 * 300 / maxn) + 4,
				**kwargs["SaddlePointSet"][i],
			)
	nx.draw_networkx_edges(G, pos, **kwargs["TrajectorySet"])

	# Draw labels for nodes
	labels = {node: "Z_" + str(node) for node in G.nodes()}
	nx.draw_networkx_labels(
		G,
		pos,
		labels=labels,
		font_size=math.ceil(0.45 * math.sqrt(math.ceil(3 * 300 / maxn) + 4)),
		font_color="black",
	)

	# Final plot adjustments
	plt.title(kwargs["Title"])
	plt.legend()
	plt.tight_layout()
	plt.axis("off")
	if kwargs["WhetherSave"]:
		plt.savefig(kwargs["SaveFigurePath"], format="png")
	plt.show()
