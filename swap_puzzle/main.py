from grid import Grid
from graph import Graph

#g = Grid(2, 3)
#print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)


gr = Graph.graph_from_file(...)
gr.bfs(src, dst)