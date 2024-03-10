from grid import Grid
#from graph import Graph
from solver import Solver

"""#g = Grid(2, 3)
#print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

g = Grid.grid_from_file("../input/grid0.in")
gtrie = g.grille_parfaite()
print(gtrie)
print(g.cheminPlusCourt(g.state))
print(g.is_sorted(g.state))
print(g.generate_neighbours(g.state, 'BFS'))
print(Graph.bfs(self = g.state, src = g.state, dst = gtrie))"""


class Test_Solver(unittest.TestCase):
    def test_solver_grid1(self):
        grid = Grid.grid_from_file("input/grid1.in")
        a = Solver(grid)
        solution = a.get_naive_solution(grid)
        self.assertTrue(grid.is_sorted())

    def test_solver_grid2(self):
        grid = Grid.grid_from_file("input/grid2.in")
        solution = Solver.get_naive_solution(grid)
        self.assertTrue(grid.is_sorted())

    def test_solver_grid3(self):
        grid = Grid.grid_from_file("input/grid3.in")
        solution = Solver.get_naive_solution(grid)
        self.assertTrue(grid.is_sorted())

    def test_solver_grid4(self):
        grid = Grid.grid_from_file("input/grid4.in")
        solution = Solver.get_naive_solution(grid)
        self.assertTrue(grid.is_sorted())

    def test_solver_bfs(self):
        grid = Grid.grid_from_file("input/grid2.in")
        solution = Solver.get_bfs_solution(grid)
        self.assertTrue(grid.is_sorted())
        

    def test_solver_bfs_optimized(self): 
        grid = Grid.grid_from_file("input/grid2.in")
        solution = Solver.get_bfs_optimized_solution(grid)
        self.assertTrue(grid.is_sorted())

if __name__ == '__main__':
    unittest.main()