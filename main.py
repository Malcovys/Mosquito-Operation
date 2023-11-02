import pygame
import random

def setRandomPosition(screen_height, screen_width, image):
    x_position = random.randint(0, screen_width - image.get_width())
    y_position = random.randint(0, screen_height - image.get_height())
    print(x_position, y_position)
    return (x_position, y_position)

present_mosquito = 0

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 550
SCREEN_FEEL_COLOR = (240, 240, 242)
MOSQUITO_DISAPPEAR = (0, 0, 0, 0)

IMAGE_WIDTH, IMAGE_HEIGHT = (50, 50)

MAX_MOSQUITO_APPARITION_NUMBER_SYNC = 1

mouse_x_click = -1
mouse_y_click = -1

image_path = './assets/images/mosquito2.jpeg'

pygame.init()

original_image = pygame.image.load(image_path)
image = pygame.transform.scale(original_image, (IMAGE_WIDTH, IMAGE_HEIGHT))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0, 0, 0))

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x_click, mouse_y_click = pygame.mouse.get_pos()
        
    if run:

        if not present_mosquito:
            x_mosquito_position, y_mosquito_position = setRandomPosition(SCREEN_HEIGHT, SCREEN_WIDTH, image)
            screen.blit(image, (x_mosquito_position, y_mosquito_position))
            present_mosquito = 1

        if (x_mosquito_position < mouse_x_click  and mouse_x_click < x_mosquito_position + IMAGE_WIDTH):
            if(y_mosquito_position < mouse_y_click and mouse_y_click < y_mosquito_position + IMAGE_HEIGHT):
                print("Touché !")
                mouse_x_click = -1
                mouse_y_click = -1

                # mosquito = image.get_rect()
                # mosquito.fill(MOSQUITO_DISAPPEAR)

                present_mosquito = 0

        pygame.display.flip()

pygame.quit()
