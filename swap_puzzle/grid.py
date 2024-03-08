"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
from graph import *
from itertools import permutations
import heapq


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
   
    def is_sorted(self, grid):
        L = []
        for i in range(len(grid)):
            L = L + grid[i]
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

    def to_hashable(self, grid):  # Retourne une représentation hashable de la grille -> conversion en tuple car c'est hashable
        return (tuple(tuple(line) for line in grid))

    @staticmethod
    def from_hashable(hashable_state: tuple):  
        content = [list(row) for row in hashable_state]
        m = len(content)
        n = len(content[0])
        return Grid(m, n, content)

    # QUESTION 7 - PARTIE 1

    def generates_all_possible_grid(self):  # Construit le graphe de tous les états possible de la grille
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

    def generate_neighbours(self, grid,mode):
        result = []
        for line in range(self.m): 
            for column in range(self.n):
                for line_add, column_add in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if 0 <= line+line_add < self.m and 0 <= column+column_add < self.n:
                        new_grid = Grid(self.m, self.n, [list(row) for row in grid])
                        new_grid.swap((line, column), (line+line_add, column+column_add))
                        new_grid_hashable = self.to_hashable(new_grid.state)
                        if new_grid_hashable not in result:
                            if mode == 'BFS':
                                result.append(new_grid_hashable)
                            else: 
                                result.append(new_grid.state)
        return (result)



        #  QUESTION 9 : A*
    """
        Structure nœud = {
        x, y: Nombre
        cout, heuristique: Nombre
    }
    depart = Nœud(x=_, y=_, cout=0, heuristique=0)
    Fonction compareParHeuristique(n1:Nœud, n2:Nœud)
        si n1.heuristique < n2.heuristique 
            retourner 1
        ou si n1.heuristique == n2.heuristique 
            retourner 0
        sinon
            retourner -1
    Fonction cheminPlusCourt(g:Graphe, objectif:Nœud, depart:Nœud)
        closedList = File()
        openList = FilePrioritaire(comparateur = compareParHeuristique)
        openList.ajouter(depart)
        tant que openList n'est pas vide
            u = openList.defiler()
            si u.x == objectif.x et u.y == objectif.y
                reconstituerChemin(u)
                terminer le programme
            pour chaque voisin v de u dans g
                si non(   v existe dans closedList
                ou v existe dans openList avec un coût inférieur)
                        v.cout = u.cout +1 
                        v.heuristique = v.cout + distance([v.x, v.y], [objectif.x, objectif.y])
                        openList.ajouter(v)
            closedList.ajouter(u)
        terminer le programme (avec erreur)
    """

    #  Définition d'une file de priorité : 
    # c est le cout
    # g est la distance à la source
    # x est la grille observée 
    # f est la file

    def filePrioVide(self):
        file = []
        heapq.heapify(file)  # La fonction heapify permet d'accéder rapidement à l'élément le plus petit (ou le plus grand)
        return file 


    def InsererFile(self, f, c, g, x):  #  Cette nouvelle fonction a pour objectif d'insérer l'élément x dans la file de priorité f 
        heapq.heappush(f,(c, g, x))  # La fonction heappush permet d'ajouter l'élément x à la file f
    #ajouter qqch qui trouve la priorité et met la grille au bon endroit


    def PopminFile(self, f):
        if len(f) == 0:
            return None
        else:
            return heapq.heappop(f)  # La fonction heappop extrait et renvoie l'élément de priorité minimale de la file de priorité "f". On met [1] pour ne selectionner que la grille et pas son heuristique


#On défiinit une fonction qui donne la grille triée
    
    def grille_parfaite(self):
        grid = []
        nblist = [i for i in range(1,self.m*self.n+1)]
        for i in range(0,len(nblist),self.n):
            grid.append(list(nblist[i:i+self.n]))
        return grid

#   Définition de l'heuristique :
    #   On cherche à définir la distance entre une matrice (noeud) et la matrice d'arrivée qui est triée en évaluant leurs différences : pour chaque coordonnées, on code 0 si c'est identique et 1 si c'est différent puis on additionne. 

    def heuristique1(self, grid):
        k = 0 # on note k la distance entre la matrice étudiée et la matrice triée (le but)
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] != i*self.n+j+1 :
                    k = k+1 # on ajoute 1 si le coef étudié est différent de celui du noeud d'arrivée
        return k/2
    # On divise par 2 car on veut que l'heuristique soit inférieure ou égale au nombre de swaps nécessaires 
    #l'heursistique1 n'est pas assez précise (pour la grille4 en particulier) donc on utilise la distance de Manhattan 
    

    # Comparer les heuristiques :
    # On compare la distance à la matrice triée de deux matrices quelconques
    def compare_heuristique(self, grid1, grid2):
        if self.heuristique(grid1) < self.heuristique(grid2):
            return 1 # Si la matrice 1 est plus proche de la matrice triée que la 2, on obtient 1
        elif self.heuristique(grid1) == self.heuristique(grid2): 
            return 0
        else:
            return -1


    #Définition de la fonction reconstituerChemin :
    #On veut que la fonction reconstitue le chemin le plus court

    def reconstituerChemin(self, grid, dictionnaire):
        grille_actuelle = self.to_hashable(grid)
        liste_etapes = []
        while grille_actuelle != None :
            liste_etapes.append(grille_actuelle)
            grille_actuelle = dictionnaire[grille_actuelle]
        return liste_etapes[::-1]


    # Définition du chemin le plus court (A*):

    def cheminPlusCourt(self, src):
        closedList = deque()
        openList = self.filePrioVide() #la file doit être ordonnée en comparant les heuristiques (les plus faibles)
        self.InsererFile(openList, 0, 0, src) #jsp si c'est fait sur insererfile mais il faut peut etre comparer les heuristiques
        src_h = self.to_hashable(src)
        dst = self.grille_parfaite()
        dictionnaire = {src_h: None}
        while openList != []:
            pop = self.PopminFile(openList)
            grille_observe = pop[2]
            closedList.append(grille_observe) #on la met dans la closed liste parce qu'on la visite 
            if grille_observe == dst:
                self.reconstituerChemin(grille_observe, dictionnaire)
                return self.reconstituerChemin(grille_observe, dictionnaire)
            for nv_grille in self.generate_neighbours(grille_observe,'A*') :
                if nv_grille not in closedList and nv_grille not in openList:
                    g = pop[1] + 1 
                    c = g + self.heuristique(nv_grille)
                    self.InsererFile(openList, c, g, nv_grille)
                    grille_h = self.to_hashable(nv_grille)
                    dictionnaire[grille_h] = self.to_hashable(grille_observe)

    #définir une fonction cout : f=h+g
