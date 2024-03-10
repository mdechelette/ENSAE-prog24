from grid import Grid
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import graph


class Solver():
    """
    A solver class, to be implemented.
    """
    def __init__(self, grid):
        self.grid = grid

    # QUESTION 3 : 
    @staticmethod
    def get_naive_solution(grid: Grid) -> list:
        retour = []  # On commence par définir une liste vide qui va stocker les étapes de résolution de la grille afin de les renvoyer sous forme de liste
        while not grid.is_sorted():  # La boucle ne s'arrête pas tant que la grille n'est pas triée
            # on commence par chercher les coordonnées du minimum qui n'est pas à sa place.
            minimum = grid.state[-1][-1]  # on parcourt à l'envers afin de ne pas être bloqué au n°1
            i_min = grid.m-1  # On enregistre les coordonnées du minimum trouvé
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
                    grid.swap((i_min, j_min), (i_min-1, j_min))  # on utilise la méthode swap pour échanger les deux cellules
                    retour.append(((i_min, j_min), (i_min-1, j_min)))  # on ajoute le swap dans la liste "retour" afin d'obtenir la séquence de swap
                else:  # si la case se situe trop haut par rapport à celle visée. 
                    grid.swap((i_min, j_min), (i_min+1, j_min))
                    retour.append(((i_min, j_min), (i_min+1, j_min)))
            else:  # si on est sur la bonne ligne
                if j_min > colonne_visee:  # si la case doit être déplacée vers la gauche 
                    grid.swap((i_min, j_min), (i_min, j_min-1))
                    retour.append(((i_min, j_min), (i_min, j_min-1)))
                else:  # si la case doit être déplacée vers la droite 
                    grid.swap((i_min, j_min), (i_min, j_min+1))
                    retour.append(((i_min, j_min), (i_min, j_min+1)))
        return retour  # On retourne la liste de séquence des swaps.
  
    """
    QUESTION 3 :
        La complexité est de o(n*m)^2. La solution naïve semble peu optimale car elle nécessite de nombreux swaps. 
    """

    """
            Solves the grid and returns the sequence of swaps at the format
            [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
            """
    

    """QUESTION 4:
    En utilisant la librairie matplotlib, on définit graph_solver qui représente la grille : """

    def graph_solver(self):
        _, ax = plt.subplots() # aide pour matplotlib : https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html
        ax.mathshow(self.state, cmap='viridis')  # Afficher la grille en utilisant une carte de couleurs bleue
        for i in range(self.n):
            for j in range(self.m):
                ax.text(j, i, str(self.state[i][j], va='center', ha='center'))  # Pour chaque case, on y inscrit la valeur de la cellule au centre
        plt.show()  # Cela permet d'afficher la figure avec la grille.


    # QUESTION 7 - PARTIE 2 :
    # On veut que la fonction get_bfs_solution résolve la grille et donne la séquence des swaps effectués avec un format de complexité o(n*m)
    """ Paramètres : 
        * La grille à résoudre. 

        Retourne : 
        * Une liste de swaps, chaque swap étant un tuple de 2 cellules. 
        Format : [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')),...]
        
        La fonction nouvellement définie est plus efficace et plus rapide que l'algorithme 
        glouton défini précédemment. """

    def get_bfs_solution(grid: Grid) -> list:  # On veut que la fonction prenne en entrée une grille et renvoie une solution sous forme de liste
        possible_graph = grid.generates_all_possible_grid()  # On obtient un graphe contenant toutes les grilles possibles
        src = grid.to_hashable()  # On transforme la grille de départ en une grille hachée 
        dst = Grid(grid.m, grid.n).to_hashable()  # On crée une grille de destination vide de même taille que la grille de départ aussi hachée
        path = possible_graph.bfs(src, dst)  # On utilise BFS pour trouver un chemin du noeud de départ (src) au noeud d'arrivée (dst)
        solution = Solver.path_to_swap(path)  # On va définir une nouvelle méthode path_to_swap pour transformer le chemin obtenu en une séquence de swaps
        grid.swap_seq(solution)  # Finalement, on applique la séquence de swap à la grille d'origine pour trouver la solution
        return solution  # On retourne la solution d

    """ Pour compléter la fonction ci-dessus, il faut en définir une nouvelle qui transforme un chemin obtenu avec la méthode BFS en une séquence de swaps. 
    Paramètres : une liste de noeuds obtenus avec la méthode bfs. 
    Retourne : une liste de swaps """

    def path_to_swap(path: list) -> list:
        solution = []
        for i in range(1, len(path)):  # Pour chaque élément du chemin obtenu, en partant du deuxième (car on cherche à comparer chaque noeud avec son prédécesseur). 
            for line in range(len(path[i])):  # On itère pour chaque ligne du noeud 
                for column in range(len(path[i][0])):  # Pour chaque colonne
                    if path[i][line][column] != path[i-1][line][column]:  # Si la case a changé
                        #  On cherche alors la case qui a changé
                        for dest_line in range(len(path[i])):  # Pour chaque ligne
                            for dest_column in range(len(path[i][0])):  # Pour chaque colonne
                                if path[i][line][column] == path[i-1][dest_line][dest_column]:  # On a trouvé la case qui a changé
                                    if not ((dest_line, dest_column), (line, column)) in solution:  # Si le swap n'est pas déjà dans la solution
                                        solution.append(((line, column), (dest_line, dest_column)))  # On sauvegarde le swap
        return solution


    # QUESTION 8 PARTIE 3

    def get_bfs_optimized_solution(grid: Grid) -> list:
        src = grid.to_hashable()
        dst = Grid(grid.m, grid.n).to_hashable()
        search_graph = graph.Graph([src, dst])
        path = search_graph.bfs_optimized(src, dst, True)
        solution = Solver.path_to_swap(path)
        grid.swap_seq(solution)
        return solution 


        