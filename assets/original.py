import pygame
from pygame.locals import *
import sys
import random

# Initialisation
pygame.init()

screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mosquito-Operation')

# Importation du background
background = pygame.image.load('assets/bg.jpg')

# Chargement de l'image du moustique et redimensionnement à la taille souhaitée
original_moustique_image = pygame.image.load('assets/moustique.png')
moustique_image = pygame.transform.scale(original_moustique_image, (55, 55))

# Chargement de l'image du sang et redimensionnement à la taille souhaitée
sang_image = pygame.image.load('assets/sang.png')
sang_image = pygame.transform.scale(sang_image, (55, 55))

#bande sound du game
audio = pygame.mixer.Sound ("assets/musique/DJVI - Back On Track.mp3")

#pour que le son se joue en boucle
audio.play (-1)

#pourle temps de pause du sound
TIMEOUT = 5

# Liste pour stocker les positions de chaque moustique
moustique_rects = []
sang_rects = []  # Liste pour stocker les positions de chaque image de sang

clock = pygame.time.Clock()
def show_start_screen():
    font = pygame.font.Font("assets/fonts/Montserrat-ExtraBold.ttf", 80)
    text_color = (255, 255, 255)
    accueil_image = pygame.image.load('assets/bg.jpg')
    accueil_image = pygame.transform.scale(accueil_image, (screen_width, screen_height))

    button_rect = pygame.Rect(500, 450, 200, 50)  # Définit button_rect en dehors de la boucle

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
        start_text = pygame.image.load("assets/bttn_start.png")
        start_text = pygame.transform.scale(start_text, (500, 150))
        start_text_rect = start_text.get_rect(center=button_rect.center)
        screen.blit(start_text, start_text_rect)

        pygame.display.flip()

show_start_screen()

# La boucle de jeu principale
while True:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Vérifier si le bouton de la souris gauche a été cliqué
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            # Obtenir la position du clic de la souris
            mouse_pos = pygame.mouse.get_pos()
            # Vérifier si le clic a touché un moustique
            for moustique_rect in moustique_rects[:]:  # Utilisez [:] pour créer une copie de la liste
                if moustique_rect.collidepoint(mouse_pos):
                    # Créer une instance de l'image de sang à la position du moustique écrasé
                    sang_rects.append((sang_image, moustique_rect.topleft, pygame.time.get_ticks()))
                    # Supprimer le moustique de la liste
                    moustique_rects.remove(moustique_rect)

    # Appliquer notre background
    screen.blit(background, (0, 0))
    # Ajouter un nouveau moustique à la liste à des intervalles aléatoires
    if random.randint(1, 110) < 2:  # Choisit un nombre aléatoire entre 1 et 100, si c'est 1 ou 2, ajoute un moustique
        moustique_rect = moustique_image.get_rect()
        moustique_rect.x = random.randint(0, 1100)  # Position aléatoire en x
        moustique_rect.y = random.randint(0, 500)  # Position aléatoire en y
        moustique_rects.append(moustique_rect)

    # Déplacer et dessiner tous les moustiques de manière aléatoire
    for moustique_rect in moustique_rects:
        # Déplacer le moustique aléatoirement en ajoutant ou soustrayant une petite quantité à ses coordonnées x et y
        moustique_rect.x += random.randint(-3, 3)
        moustique_rect.y += random.randint(-3, 3)

        # Assurez-vous que le moustique ne sort pas de l'écran
        moustique_rect.x = max(0, min(moustique_rect.x, 1100))
        moustique_rect.y = max(0, min(moustique_rect.y, 500))

        # Dessiner le moustique à sa nouvelle position
        screen.blit(moustique_image, moustique_rect.topleft)

    # Dessiner le sang
    for sang_rect in sang_rects:
        image, position, start_time = sang_rect
        current_time = pygame.time.get_ticks()
        # Afficher l'image de sang pendant 3 secondes (3000 millisecondes)
        if current_time - start_time < 3000:
            screen.blit(image, position)

    # Mettre à jour l'écran
    pygame.display.flip()

    # Réguler la vitesse de la boucle
    clock.tick(60)
