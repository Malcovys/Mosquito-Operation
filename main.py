import pygame
import random

def setRandomPosition(screen_height, screen_width, position, image):
    position.x = random.randint(0, screen_width - image.get_width())
    position.y = random.randint(0, screen_height - image.get_height())

    # Limitateur
    position.x = max(0, min(position.x, screen_width - image.get_width()))
    position.y = max(0, min(position.y, screen_height - image.get_height()))

    return position

def doMosquitoFlyEffect(position):
    position.x += random.randint(-3, 3)
    position.y += random.randint(-3, 3)

    return position

background_image_path = './assets/images/background.jpg'
mosquito_image_path = './assets/images/mosquito.png'
mosquito_crushed_image_path = './assets/images/crushed.png'

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SCREEN_FILL_COLOR = (240, 240, 242)
MOSQUITO_WIDTH, MOSQUITO_HEIGHT = 55, 55
CRUSHED_MOSQUITO_APPEAR_TIME = 3000

mosquito_apparition_rate = 0.02  # Taux d'apparition (2%)

pygame.init()

background = pygame.image.load(background_image_path)

original_mosquito_image = pygame.image.load(mosquito_image_path)
mosquito_image = pygame.transform.scale(original_mosquito_image, (MOSQUITO_WIDTH, MOSQUITO_HEIGHT))

original_mosquito_crushed_image = pygame.image.load(mosquito_crushed_image_path)
crushed_mosquito_image = pygame.transform.scale(original_mosquito_crushed_image, (MOSQUITO_WIDTH, MOSQUITO_HEIGHT))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
alive_mosquitos_rect_properties = []
crushed_mosquitos_rect_properties = []

clock = pygame.time.Clock()
FPS = 30
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x_click, mouse_y_click = pygame.mouse.get_pos()

            # Gestion du splash
            for alive_mosquito_rect_property in alive_mosquitos_rect_properties[:]:
                if alive_mosquito_rect_property.collidepoint(mouse_x_click, mouse_y_click):
                    crushed_mosquitos_rect_properties.append((crushed_mosquito_image, alive_mosquito_rect_property.topleft, pygame.time.get_ticks()))
                    alive_mosquitos_rect_properties.remove(alive_mosquito_rect_property)

    screen.blit(background, (0, 0))

    # Gestion de l'apparition des moustiques
    if random.random() < mosquito_apparition_rate:
        mosquito_rect_property = mosquito_image.get_rect()
        setRandomPosition(SCREEN_HEIGHT, SCREEN_WIDTH, mosquito_rect_property, mosquito_image)
        alive_mosquitos_rect_properties.append(mosquito_rect_property)

    for i in range(len(alive_mosquitos_rect_properties)):
        new_position = doMosquitoFlyEffect(alive_mosquitos_rect_properties[i])
        alive_mosquitos_rect_properties[i] = pygame.Rect(new_position[0], new_position[1], MOSQUITO_WIDTH, MOSQUITO_HEIGHT)

    for alive_mosquito_rect_property in alive_mosquitos_rect_properties:
        screen.blit(mosquito_image, alive_mosquito_rect_property.topleft)

    for i in range(len(crushed_mosquitos_rect_properties)):
        substitute_image, position, start_time = crushed_mosquitos_rect_properties[i]
        current_time = pygame.time.get_ticks()

        # Afficher l'image écrasée pendant 3 secondes (3000 millisecondes)
        if current_time - start_time < CRUSHED_MOSQUITO_APPEAR_TIME:
            screen.blit(substitute_image, position)

    pygame.display.flip()

pygame.quit()