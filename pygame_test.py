import pygame
import time
import random


pygame.init()

snake_speed = 15

disp = pygame.display.set_mode((800,600))  #halim put windowsx and y instead 
pygame.display.set_caption("davinci's snake")
# # window size
# window_x = 720
# window_y = 480

#FPS
clock = pygame.time.Clock()

#setting the colors 
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)




open = True
while open:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            open == False

    pygame.draw.rect(disp, blue,[200,200,10,10])
    pygame.display.update()
pygame.quit
quit()