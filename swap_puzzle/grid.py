"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
from graph import Graph
from itertools import permutations


class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"
        
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
   
    def is_sorted(self):
        L = []
        for i in range(self.m):
            L = L + self.state[i]
        for k in range(len(L)-1):
            if L[k] > L[k+1]:
                return (False)
        return True

        # [1,2,3,4]
    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        if cell1[0] == cell2[0]:
            if cell1[1] == cell2[1] or cell1[1] == cell2[1]+1 or cell1[1] == cell2[1]-1:
                self.state[cell1[0]][cell1[1]],self.state[cell2[0]][cell2[1]] = self.state[cell2[0]][cell2[1]],self.state[cell1[0]][cell1[1]]
        elif cell1[1] == cell2[1]:
            if cell1[0] == cell2[0] or cell1[0] == cell2[0]+1 or cell1[0] == cell2[0]-1:
                self.state[cell1[0]][cell1[1]],self.state[cell2[0]][cell2[1]] = self.state[cell2[0]][cell2[1]],self.state[cell1[0]][cell1[1]]
        else:
            raise Exception(f"Les cases {cell1} et {cell2} ne peuvent être échangées.")
       
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
       
    def swap_seq(self, cell_pair_list):
        for k in cell_pair_list:
            self.swap(k[0], k[1])

    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid

    # QUESTION 6:

    def to_hashable(self):  # Retourne une représentation hashable de la grille -> conversion en tuple car c'est hashable
        return (tuple(tuple(line) for line in self.state))

    @staticmethod
    def from_hashable(hashable_state: tuple):  
        content = [list(row) for row in hashable_state]
        m = len(content)
        n = len(content[0])
        return Grid(m, n, content)

    # QUESTION 7 - PARTIE 1

    def generates_all_possible_grid(self) -> Graph:  # Construit le graphe de tous les états possible de la grille
        # Le code ci-dessous génère toutes les grilles possibles avec le contenu 1,2,3,4,5,6...
        grids = []
        items = list(range(1, self.m*self.n+1))
        for p in permutations(items):
            grids.append(Grid(self.m, self.n, [list(p[i*self.n:(i+1)*self.n]) for i in range(self.m)]))

        # On crée un graphe avec toutes les grilles possibles
        graph = Graph([grid.to_hashable() for grid in grids])

    # QUESTION 7 - PARTIE 3 
        # Calcul du nombre de noeuds et d'arête du graphe créé
        for i in range(len(grids)):  # pour toutes les grilles 
            for line in range(self.m):  # pour toutes les lignes 
                for column in range(self.n):  # pour toutes les colonnes
                    for line_add, column_add in [(0, 1), (1, 0), (-1, 0), (0, -1)]:  # pour toutes les opérations possibles
                        if 0 <= line+line_add < self.m and 0 <= column+column_add < self.n:  # si la case est dans la grille 
                            hashable = grids[i].to_hashable()
                            grids[i].swap((line, column), (line+line_add, column+column_add))
                            graph.add_edge(hashable, grids[i].to_hashable())
        return graph

    # QUESTION 8 - PARTIE 1 :
    # On redéfinit une nouvelle fonction qui génère le voisin de la grille

    def generate_neighbours(self):
        result = []
        for line in range(self.m): 
            for column in range(self.n):
                for line_add, column_add in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if 0 <= line+line_add < self.m and 0 <= column+column_add < self.n:
                        new_grid = Grid(self.m, self.n, [list(row) for row in self.state])
                        new_grid.swap((line, column), (line+line_add, column+column_add))
                        new_grid_hashable = new_grid.to_hashable()
                        if new_grid_hashable not in result:
                            result.append(new_grid_hashable)
        return (result)
