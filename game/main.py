import pygame
from pygame.locals import *
import sys
import random
from game import Game

# Initialisation
pygame.init()

# Paramètres de l'écran
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mosquito-Operation')

#bande sound du game
audio = pygame.mixer.Sound ("assets/musique/DJVI - Back On Track.mp3")

#pour que le son se joue en boucle
audio.play (-1)

#pourle temps de pause du sound
TIMEOUT = 5

game = Game(screen)

clock = pygame.time.Clock()

# Écran d'accueil
# Écran d'accueil
def show_start_screen():
    font = pygame.font.Font(None, 36)
    text_color = (255, 255, 255)
    accueil_image = pygame.image.load('assets/bg.jpg')
    accueil_image = pygame.transform.scale(accueil_image, (screen_width, screen_height))

    button_rect = pygame.Rect(500, 450, 200, 50)  # Définissez button_rect en dehors de la boucle

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    # L'utilisateur a cliqué sur "Start", quitter l'écran d'accueil
                    return

        # Afficher l'écran d'accueil avec le nom du jeu et le bouton "Start"
        screen.blit(accueil_image, (0, 0))
        text = font.render('Mosquito Operation', True, text_color)
        text_rect = text.get_rect(center=(screen_width // 2, 200))
        screen.blit(text, text_rect)
        pygame.draw.rect(screen, (0, 255, 0), button_rect)
        start_text = font.render('Start', True, text_color)
        start_text_rect = start_text.get_rect(center=button_rect.center)
        screen.blit(start_text, start_text_rect)

        pygame.display.flip()

show_start_screen()


# Boucle de jeu principale
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        game.handle_events(event)

    game.update()
    game.draw(screen)

    pygame.display.flip()
    clock.tick(60)
