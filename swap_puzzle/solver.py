from grid import Grid
from matplotlib import pyplot as plt
import graph


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
        La complexité est de o(n*m)^2. 
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

    # QUESTION 7 - PARTIE 2 :
    # On veut que la fonction get_bfs_solution résolve la grille et donne la séquence des swaps effectués avec un format de complexité o(n*m)
    """ Paramètres : 
        * La grille à résoudre. 

        Retourne : 
        * Une liste de swaps, chaque swap étant un tuple de 2 cellules. 
        Format : [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')),...] """

    def get_bfs_solution(grid: Grid) -> list:  # On veut que la fonction prenne en entrée une grille et renvoie une solution sous forme de liste
        possible_graph = grid.generate_all_possible_grid()
        src = grid.to_hashable()
        dst = Grid(grid.m, grid.n).to_hashable()
        path = possible_graph.bfs(src, dst)
        solution = Solver.path_to_swap(path)
        grid.swap_seq(solution)
        return solution

    """ Pour compléter la fonction ci-dessus, il faut en définir une nouvelle qui transforme un chemin obtenu avec la méthode BFS en une séquence de swaps. 
    Paramètres : une liste de noeuds obtenus avec la méthode bfs. 
    Retourne : une liste de swaps """

    def path_to_swap(path: list) -> list:
        solution = []
        for i in range(1, len(path)):  # Pour chaque élément du chemin obtenu, en partant du deuxième
            for line in range(len(path[i])):  # Pour chaque ligne
                for column in range(len(path[i][0])):  # Pour chaque colonne
                    if path[i][line][column] != path[i-1][line][column]:  # Si la case à changé
                        #  On cherche alors la case qui a changé
                        for dest_line in range(len(path[i])):  # Pour chaque ligne
                            for dest_column in range(len(path[i][0])):  # Pour chaque colonne
                                if path[i][line][column] == path[i-1][dest_line][dest_column]:  # On a trouvé la case qui a changé
                                    if not ((dest_line, dest_column), (line, column)) in solution:  # Si le swap n'est pas déjà dans la solution
                                        solution.append(((line, column), (dest_line, dest_column)))  # On sauvegarde le swap
        return solution

    def get_bfs_optimized_solution(grid: Grid) -> list:
        src = grid.to_hashable()
        dst = Grid(grid.m, grid.n).to_hashable()
        search_graph = graph.Graph([src, dst])
        path = search_graph.bfs(src, dst, True)
        solution = Solver.path_to_swap(path)
        grid.swap_seq(solution)
        return solution