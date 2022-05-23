#Building Beats!!!
import pygame
from pygame import mixer
pygame.init()

#Resolution
WIDTH = 1500
HEIGHT = 790

#Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (34,139,34)

#setting up the screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('LinearBeats') #setting caption on top
label_font = pygame.font.Font('PlayfairDisplay-Bold.ttf', 32)

#<add more stuff from here>

frame_rate = 60
timer = pygame.time.Clock()

#Draw grids to seperate the screen to different parts
def draw_grid():
    left_box = pygame.draw.rect(screen, green, [0, 0, 200, HEIGHT])
    bottom_box = pygame.draw.rect(screen, green, [0, HEIGHT - 200, WIDTH, 200], 3)
    hi_hat_text = label_font.render('HI HAT', True, white)
    screen.blit(hi_hat_text, (30, 30))

# To continuosly run the pygame screen for given frame rate
run = True
while run:
    timer.tick(frame_rate)
    screen.fill(black)
    draw_grid()

    #check events happening while on screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()




