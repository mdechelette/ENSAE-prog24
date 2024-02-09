from grid import Grid
from matplotlib import pyplot as plt


class Solver():
    """
    A solver class, to be implemented.
    """
    @staticmethod
    def get_naive_solution(grid: Grid) -> list:
        retour = []
        while not grid.is_sorted():
            # on commence par chercher les coordonnées du minimum qui n'est pas à sa place.
            minimum = grid.state[-1][-1]  # on parcourt à l'envers afin de ne pas être bloqué au n°1
            i_min = grid.m-1
            j_min = grid.n-1
            for i in range(grid.m):  # on parcourt les lignes
                for j in range(grid.n):  # on parcourt les colonnes
                    if grid.state[i][j] < minimum and grid.state[i][j] != i*grid.n+j+1:  # si la case est plus petite que le minimum et n'est pas à sa place 
                        minimum = grid.state[i][j]
                        i_min = i 
                        j_min = j

            ligne_visee = (minimum-1)//grid.n  # coordonnée de la ligne dans laquelle la case doit être 
            colonne_visee = (minimum-1) % grid.n  # coordonnée de la colonne dans laquelle la case doit être 
            if i_min != ligne_visee:  # si la case ne se situe pas sur la bonne ligne
                if i_min > ligne_visee:  # si la case est située trop bas par rapport à celle visée
                    grid.swap((i_min, j_min), (i_min-1, j_min))
                    retour.append((i_min, j_min), (i_min-1, j_min))
                else:  # si la case se situe trop haut par rapport à celle visée. 
                    grid.swap((i_min, j_min), (i_min+1, j_min))
                    retour.append((i_min, j_min), (i_min+1, j_min))
            else:  # si on est sur la bonne ligne
                if j_min > colonne_visee:  # si la case doit être déplacée vers la gauche 
                    grid.swap((i_min, j_min), (i_min, j_min-1))
                    retour.append((i_min, j_min), (i_min, j_min-1))
                else:  # si la case doit être déplacée vers la droite 
                    grid.swap((i_min, j_min), (i_min, j_min+1))
                    retour.append((i_min, j_min), (i_min, j_min+1))
        return retour
  
    """
    QUESTION 3 :
        La complexité est de (n*m)^2. 
    """

    """
            Solves the grid and returns the sequence of swaps at the format
            [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
            """
    # TODO: implement this function (and remove the line "raise NotImplementedError").
    # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.

    """QUESTION 4:
    En utilisant la librairie matplotlib, on définit graph_solver qui représente la grille : """

    def graph_solver(self):
        _, ax = plt.subplots()
        ax.mathshow(self.state, cmap='viridis')  # aide pour matplotlib : https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html
        for i in range(self.n):
            for j in range(self.m):
                ax.text(j, i, str(self.state[i][j], va='center', ha='center'))
        plt.show()
