import pygame
from pygame.locals import *
import sys
from game import Game

# Initialisation
pygame.init()

screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Mosquito-Operation')

game = Game()

clock = pygame.time.Clock()

# La boucle de jeu principale
while True:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Gérer les événements spécifiques au jeu
        game.handle_events(event)

    # Mettre à jour la logique du jeu
    game.update()

    # Mettre à jour et dessiner l'écran
    game.draw(screen)

    # Réguler la vitesse de la boucle
    clock.tick(60)
