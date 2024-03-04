"""
This is the graph module. It contains a minimalistic Graph class.
"""
from collections import deque
import grid


class Graph:
    """
    A class representing undirected graphs as adjacency lists. 

    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [neighbor1, neighbor2, ...]
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    edges: list[tuple[NodeType, NodeType]]
        The list of all edges
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 

        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes 
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.edges = []

    def __str__(self):
        """
        Prints the graph as a list of neighbors for each node (one per line)
        """
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the graph with number of nodes and edges.
        """
        return f"<graph.Graph: nb_nodes={self.nb_nodes}, nb_edges={self.nb_edges}>"

    def add_edge(self, node1, node2):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 
        When adding an edge between two nodes, if one of the ones does not exist it is added to the list of nodes.

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
        self.nb_edges += 1
        self.edges.append((node1, node2))

    # QUESTION 5 
    def bfs(self, src, dst): 
        # Le site de wikipedia nous permet de voir la structure attendue de la fonction BFS
        # La fonction BFS permet de trouver le chemin le plus court de la source à la destination
        if src == dst:
            return [src]
        f = deque()
        f.append([src])
        visited = []
        while f:
            path = f.popleft()
            node = path[-1]
            if node not in visited:
                for t in self.graph[node]:
                    new_path = list(path)
                    new_path.append(t)
                    f.append(new_path)
                    if t == dst: 
                        return new_path
                visited.append(node)
        return
        """
        Finds a shortest path from src to dst by BFS.  

        Parameters: 
        -----------
        src: NodeType
            The source node.
        dst: NodeType
            The destination node.

        Output: 
        -------
        path: list[NodeType] | None
            The shortest path from src to dst. Returns None if dst is not reachable from src
        """ 

    @classmethod
    def graph_from_file(cls, file_name):
        """
        Reads a text file and returns the graph as an object of the Graph class.

        The file should have the following format: 
            The first line of the file is 'n m'
            The next m lines have 'node1 node2'
        The nodes (node1, node2) should be named 1..n

        Parameters: 
        -----------
        file_name: str
            The name of the file

        Outputs: 
        -----------
        graph: Graph
            An object of the class Graph with the graph from file_name.
        """
        with open(file_name, "r") as file:
            n, m = map(int, file.readline().split())
            graph = Graph(range(1, n+1))
            for _ in range(m):
                edge = list(map(int, file.readline().split()))
                if len(edge) == 2:
                    node1, node2 = edge
                    graph.add_edge(node1, node2) # will add dist=1 by default
                else:
                    raise Exception("Format incorrect")
        return graph

    # QUESTION 8 - PARTIE 2 
    # REDÉFINITION DE LA FONCTION BFS

    def bfs_optimized(self, src, dst, generate=False): 
        if src == dst:
            return [src]
        f = deque()
        f.append([src])
        visited = []
        while f:
            path = f.popleft()
            node = path[-1]
            if node not in visited:
                neighbours = self.graph.get(node, None)
                if generate:
                    neighbours = grid.Grid.from_hashable(node).generate_neighbours()
                    self.add_children(node, neighbours)
                for t in neighbours:
                    new_path = list(path)
                    new_path.append(t)
                    f.append(new_path)
                    if t == dst:
                        return new_path
                visited.append(node)
        return

    # Compléter la fonction bfs nécessite de définir une nouvelle fonction qui génère le graphe de la grille obtenue en swappant 2 cellules adjacentes.

    def add_children(self, parent, list: list):
        for i in list: 
            self.add_edge(parent, i)


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

import heapq


def filePrioVide():
    file = []
    heapq.heapify(file)  # La fonction heapify permet d'accéder rapidement à l'élément le plus petit (ou le plus grand)
    return file 


def InsererFile(x, f):  #  Cette nouvelle fonction a pour objectif d'insérer l'élément x dans la file de priorité f 
    heapq.heappush(f,x)  # La fonction heappush permet d'ajouter l'élément x à la file f


def PopminFile(f):
    if len(f) == 0:
        return None
    else:
        return heapq.heappop(f)  # La fonction heappop extrait et renvoie l'élément de priorité minimale de la file de priorité "f". 


#   Définition de l'heuristique :
#   On cherche à définir la distance entre une matrice (noeud) et la matrice d'arrivée qui est triée en évaluant leurs différences : pour chaque coordonnées, on code 0 si c'est identique et 1 si c'est différent puis on additionne. 

def heuristique(grid):
    k = 0 # on note k la distance entre la matrice étudiée et la matrice triée
    for i in range(grid.m):
        for j in range(grid.n):
            if grid.state[i][j] != i*n+j+1 :
                k = k+1 # on ajoute 1 si le coef étudié est différent de celui du noeud d'arrivée
    return k


# Comparer les heuristiques :
# On compare la distance à la matrice triée de deux matrices quelconques
def compare_heuristique(grid1, grid2):
    if heuristique(grid1) < heuristique(grid2):
        return 1 # Si la matrice 1 est plus proche de la matrice tricée que la 2, on obtient 1
    elif heuristique(grid1) == heuristique(grid2): 
        return 0
    else:
        return -1

# Définition du chemin le plus court :

def cheminPlusCourt(grid):
       closedList = File()
       openList = FilePrioritaire(comparateur = compareParHeuristique)
       openList.ajouter(depart)
       while openList != []
           u = openList.defiler()
           if u.x == objectif.x and u.y == objectif.y
               reconstituerChemin(u)
               terminer le programme
           for v voisin de u dans g
               if non(   v existe dans closedList
                            ou v existe dans openList avec un coût inférieur)
                    v.cout = u.cout +1 
                    v.heuristique = v.cout + distance([v.x, v.y], [objectif.x, objectif.y])
                    openList.ajouter(v)
           closedList.ajouter(u)