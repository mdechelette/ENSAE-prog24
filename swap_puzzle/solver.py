from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """
    @staticmethod
    def get_cell(grid, k):
        for i in range(0, grid.n):
            for j in range(0, grid.m):
                if grid.state[i][j] == k:
                    return (i, j)

    def swap_gauche(grid):
        i0, j0 = Solver.get_cell(grid, k)
        for j in range(0, i0):
            cell1 = grid.state[i][j]
            cell2 = grid.state[i-1][j]
            while j > k-i*n-1:
                swap(grid, cell1, cell2)

    @staticmethod
    def get_solution(grid):
        m = grid.m
        n = grid.n
        # Dans cette partie, on cherche les coordonnées de chaque numéro entre 1 et n*m
        for k in range(1, m*n+1):
            i0, j0 = Solver.get_cell(grid, k)
                return (i0, j0)
            
    @staticmethod
    def go_cell(grid, k):        
        j == k-i*grid.n-1
        i == (1/n)*(k-j-1)

    
            

        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
       

        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        raise NotImplementedError

