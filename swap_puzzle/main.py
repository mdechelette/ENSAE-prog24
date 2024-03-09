from grid import Grid
from graph import Graph

#g = Grid(2, 3)
#print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

g = Grid.grid_from_file("../input/grid0.in")
gtrie = g.grille_parfaite()
print(gtrie)
print(g.cheminPlusCourt(g.state))
print(g.is_sorted(g.state))
print(g.generate_neighbours(g.state, 'BFS'))
print(Graph.bfs(self = g.state, src = g.state, dst = gtrie))