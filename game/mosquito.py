import pygame
import random

class Moustique(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/moustique.png')
        self.image = pygame.transform.scale(self.image, (55, 55))  # Redimensionnez l'image ici
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1100)
        self.rect.y = random.randint(0, 500)
        self.velocity = random.randint(-3, 3), random.randint(-3, 3)

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        self.rect.x = max(0, min(self.rect.x, 1100))
        self.rect.y = max(0, min(self.rect.y, 500))
