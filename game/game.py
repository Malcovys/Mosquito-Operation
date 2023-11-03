import random
import pygame
from pygame.locals import MOUSEBUTTONDOWN
from mosquito import Moustique

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('assets/bg.jpg')
        self.moustiques = pygame.sprite.Group()

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for moustique in self.moustiques.sprites():
                if moustique.rect.collidepoint(mouse_pos):
                    moustique.kill()

    def update(self):
        if random.randint(1, 100) < 2:
            moustique = Moustique()
            self.moustiques.add(moustique)

        self.moustiques.update()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.moustiques.draw(screen)
