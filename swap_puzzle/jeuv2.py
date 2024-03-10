import pygame
import random

pygame.init()

# Initialisation de la fenêtre et de la grille
fenetre = pygame.display.set_mode((550,550))
pygame.display.set_caption('Jeu de tri de grille')
background_color = (202, 228, 241)
fenetre.fill(background_color)

# Dessin de la grille
for i in range(0,10):
    if(i%3 == 0):
        pygame.draw.line(fenetre, (255, 255, 255), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
        pygame.draw.line(fenetre, (255, 255, 255), (50, 50 + 50*i), (500, 50 + 50*i), 4 )
        pygame.draw.line(fenetre, (166, 166, 166), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        pygame.draw.line(fenetre, (166, 166, 166), (50, 50 + 50*i), (500, 50 + 50*i), 2 )

# Génération des nombres uniques de 1 à 9 dans un ordre aléatoire
numbers = list(range(1, 10))
random.shuffle(numbers)

# Remplissage de la grille avec un nombre unique dans chaque case
grid = [[0]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        num = numbers[i * 3 + j]
        grid[i][j] = num
        font = pygame.font.Font(None, 50)
        text = font.render(str(num), True, (0, 0, 0))
        text_rect = text.get_rect(center=(75 + j*50, 75 + i*50))
        fenetre.blit(text, text_rect)

pygame.display.update()

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

pygame.quit()
