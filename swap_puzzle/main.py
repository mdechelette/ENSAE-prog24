from grid import Grid
from graph import Graph

#g = Grid(2, 3)
#print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

g = Grid.grid_from_file("../input/grid4.in")
print(g.cheminPlusCourt(g.state))