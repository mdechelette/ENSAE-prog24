# This will work if ran from the root folder ensae-prog24
import sys 
import unittest 
from grid import Grid
from graph import Graph
sys.path.append("swap_puzzle/")


class Test_GridLoading(unittest.TestCase):
    def test_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
        self.assertEqual(g.m, 4)
        self.assertEqual(g.n, 2)
        self.assertEqual(g.state, [[1, 2], [3, 4], [5, 6], [8, 7]])


if __name__ == '__main__':
    unittest.main()

