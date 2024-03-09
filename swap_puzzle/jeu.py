import pygame 
import requests
from grid import Grid
from numpy import array, blackman
import random


#Création d'un jeu de tri d'une grille aléatoire 
"""Installez la bibliothèque pygame.
Création d’un cadre de fenêtre pour le jeu.
Ajout de la grille  pour les nombres.
Mettre les numéros de départ des grilles de jeu à l’aide de l’API.
Nous allons ajouter une fonctionnalité d’entrée qui est utilisée pour saisir les chiffres dans un espace vide."""

pygame.init()

fenetre = pygame.display.set_mode((550,550))
pygame.display.set_caption('Jeu de tri de grille')

background_color = (202, 228, 241)
fenetre.fill(background_color)
pygame.display.update()

for i in range(0,10):
        if(i%3 == 0):
        #lignes intérieures
            pygame.draw.line(fenetre, (255, 255, 255), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
        #lignes horizontales
            pygame.draw.line(fenetre, (255, 255, 255), (50, 50 + 50*i), (500, 50 + 50*i), 4 )
        #on dessine les lignes verticales
            pygame.draw.line(fenetre, (166, 166, 166), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        #on dessine les lignes horizontales
            pygame.draw.line(fenetre, (166, 166, 166), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
pygame.display.update()


running = True 
        
while running:
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

pygame.quit()

"""import tkinter as tk
 
rows = columns = 10
size = 50
cases = {}            # un dict pour se souvenir des cases.
 
def on_click(event):
    i, j =  event.x // size, event.y // size  # (x, y) => (i, j)
    if (i, j) in cases:  # si la case existe...
        return
    # sinon on crée la case (i, j)
    x0, y0 = i * size, j * size
    x1, y1 = x0 + size, y0 + size
    cases[i,j] = damier.create_rectangle(x0, y0, x1, y1, fill='black')
 
damier = tk.Canvas(width=rows*size, height=columns*size)
damier.bind('<1>', on_click)
damier.pack()
tk.mainloop()"""