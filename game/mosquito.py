#import random
#import pygame

# Votre code ici


#class Moustique(pygame.sprite.Sprite):
    #def __init__(self, image_path, position):
        #super().__init__()
        #self.image = pygame.image.load(image_path)
        #self.rect = self.image.get_rect(topleft=position)
        #self.velocity = random.randint(1, 5)

    #def deplacer(self):
        # Déplacer le moustique aléatoirement en ajoutant ou soustrayant une petite quantité à ses coordonnées x et y
        #self.rect.x += random.randint(-3, 3)
        #self.rect.y += random.randint(-3, 3)

        # Assurez-vous que le moustique ne sort pas de l'écran
        #self.rect.x = max(0, min(self.rect.x, 1100))
        #self.rect.y = max(0, min(self.rect.y, 500))

import pygame
import random

class Moustique:
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/moustique.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = random.randint(-3, 3), random.randint(-3, 3)

    def update(self):
        # Déplacer le moustique aléatoirement
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Assurez-vous que le moustique ne sort pas de l'écran
        self.rect.x = max(0, min(self.rect.x, 1100))
        self.rect.y = max(0, min(self.rect.y, 500))

    def draw(self, screen):
        # Dessiner le moustique à sa position actuelle
        screen.blit(self.image, self.rect.topleft)

