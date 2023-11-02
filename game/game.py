#import random
#import pygame
#from pygame.locals import *
#from mosquito import Moustique

#class Game:
    #def __init__(self, screen):
        #self.screen = screen
        #self.background = pygame.image.load('assets/bg.jpg')
        #self.moustique_image = pygame.transform.scale(pygame.image.load('assets/moustique.png'), (55, 55))
        #self.sang_image = pygame.transform.scale(pygame.image.load('assets/sang.png'), (55, 55))
        #self.moustique_rects = []
        #self.sang_rects = []
        #self.clock = pygame.time.Clock()

    #def handle_event(self, event):
       #if event.type == MOUSEBUTTONDOWN and event.button == 1:
            #mouse_pos = pygame.mouse.get_pos()
            #for moustique_rect in self.moustique_rects[:]:
                #if moustique_rect.collidepoint(mouse_pos):
                    #self.sang_rects.append((self.sang_image, moustique_rect.topleft, pygame.time.get_ticks()))
                    #self.moustique_rects.remove(moustique_rect)

    #def update(self):
        #if random.randint(1, 400) < 2:
            #moustique_rect = self.moustique_image.get_rect()
            #moustique_rect.x = random.randint(0, 1100)
            #moustique_rect.y = random.randint(0, 500)
            #self.moustique_rects.append(moustique_rect)

        #for sang_rect in self.sang_rects[:]:
            #image, position, start_time = sang_rect
            #current_time = pygame.time.get_ticks()
            #if current_time - start_time >= 3000:
                #self.sang_rects.remove(sang_rect)

    #def draw(self):
        #self.screen.blit(self.background, (0, 0))
        #for moustique_rect in self.moustique_rects:
            #self.screen.blit(self.moustique_image, moustique_rect.topleft)
        #for sang_rect in self.sang_rects:
            #image, position, start_time = sang_rect
            #self.screen.blit(image, position)
import pygame
from pygame.locals import MOUSEBUTTONDOWN
import random
from mosquito import Moustique

class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.background = pygame.image.load('assets/bg.jpg')
        self.moustiques = []

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            # Gérer les clics de souris pour écraser les moustiques
            mouse_pos = pygame.mouse.get_pos()
            for moustique in self.moustiques[:]:
                if moustique.rect.collidepoint(mouse_pos):
                    self.moustiques.remove(moustique)

    def update(self):
        # Ajouter un nouveau moustique à la liste à des intervalles aléatoires
        if random.randint(1, 100) < 2:  
            moustique = Moustique(random.randint(0, 1100), random.randint(0, 500))
            self.moustiques.append(moustique)

        # Mettre à jour la logique des moustiques
        for moustique in self.moustiques:
            moustique.update()

    def draw(self, screen):
        # Dessiner le fond
        screen.blit(self.background, (0, 0))

        # Dessiner les moustiques
        for moustique in self.moustiques:
            moustique.draw(screen)

