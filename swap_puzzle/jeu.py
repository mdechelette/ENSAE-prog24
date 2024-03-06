import pygame 
from grid import Grid
from numpy import array, blackman
import random

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

