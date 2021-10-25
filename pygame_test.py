import pygame
import time
import random


pygame.init()

#declaring some variables

disp_width = 600
disp_height  = 400

x1 = disp_width/2
y1 = disp_height/2

x1_change = 0
y1_change = 0

snake_fps = 10  #halim was right 
snake_speed = 20

disp = pygame.display.set_mode((disp_width,disp_height))  #halim put windowsx and y instead 
pygame.display.set_caption("davinci's snake")
# # window size
# window_x = 720
# window_y = 480

#FPS as halim says
clock = pygame.time.Clock()

#setting the colors 
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128,0,128)

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 15)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, purple)
    disp.blit(value, [0, 0])

def our_snake(snake_block, snake_list):       
       for x in snake_list:
              pygame.draw.rect(disp, blue, [x[0], x[1], snake_block, snake_block])

#created function for game over message
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    disp.blit(mesg, [disp_width/2, disp_height/2])

#created function for the game 
def gameloop():
       open = True
       dead = False

       x1 = disp_width / 2
       y1 = disp_height / 2
 
       x1_change = 0
       y1_change = 0

       snake_list= []
       length_of_snake = 1
 
       foodx = round(random.randrange(0, disp_width - snake_fps) / 10.0) * 10.0
       foody = round(random.randrange(0, disp_width - snake_fps) / 10.0) * 10.0 

       #loop for game 
       while open:
               while dead == True:
                      disp.fill(black)
                      message("Game Over E to Exit or P to Play Again", red)
                      pygame.display.update()

                      for event in pygame.event.get():
                             if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_e:
                                           open = True
                                           dead = False
                                    if event.key == pygame.K_p:
                                           gameloop()
              
               for event in pygame.event.get():
                      if event.type == pygame.QUIT:
                             open = False
                      if event.type == pygame.KEYDOWN:
                             if event.key == pygame.K_LEFT:
                                    x1_change = -snake_fps
                                    y1_change = 0
                             elif event.key == pygame.K_RIGHT:
                                    x1_change = snake_fps
                                    y1_change = 0
                             elif event.key == pygame.K_UP:
                                    y1_change = -snake_fps
                                    x1_change = 0
                             elif event.key == pygame.K_DOWN:
                                    y1_change = snake_fps
                                    x1_change = 0
              


               #to make the snake warp edges
               if x1 >= disp_width:
                      x1 = 0
               elif x1 <= 0:
                      x1 = disp_width
               elif y1 >= disp_height:
                      y1 = 0
               elif y1 <= 0:
                      y1 = disp_height  

               x1 += x1_change
               y1 += y1_change

               disp.fill(black)
               pygame.draw.rect(disp, blue,[x1,y1,snake_fps,snake_fps])   #drawing for snake
               pygame.draw.rect(disp,green,[foodx,foody,snake_fps,snake_fps])  #drawing for food
               
                #Adding the snake 
               snake_Head = []
               snake_Head.append(x1)
               snake_Head.append(y1)
               snake_list.append(snake_Head)
               if len(snake_list) > length_of_snake:
                      del snake_list[0]
 
               for x in snake_list[:-1]:
                      if x == snake_Head:
                             dead = True
 
               our_snake(snake_fps, snake_list)
               
               Your_score(length_of_snake - 1)
 
 
               pygame.display.update()                     

               pygame.display.update()
               clock.tick(snake_speed)   #UNDERSTAND

               #randomly drop food 
               if x1 == foodx and y1 == foody: 
                      foodx = round(random.randrange(0, disp_width - snake_fps) / 10.0) * 10.0  
                      foody = round(random.randrange(0, disp_height - snake_fps) / 10.0) * 10.0 
                      length_of_snake += 1

                     
               clock.tick(snake_speed)    


       pygame.quit()
       quit()

gameloop()