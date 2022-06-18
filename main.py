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
beats = 8
instruments = 6

#Draw grids to seperate the screen to different parts
def draw_grid():
    left_box = pygame.draw.rect(screen, green, [0, 0, 251, HEIGHT - 200], 4)
    bottom_box = pygame.draw.rect(screen, green, [0, HEIGHT - 200, WIDTH, 200], 4)
    boxes = []
    colors = [green, white, green]
    hi_hat_text = label_font.render('HI HAT', True, white)
    screen.blit(hi_hat_text, (30, 30))
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 130))
    kick_text = label_font.render('Kick Drum', True, white)
    screen.blit(kick_text, (30, 230))
    crash_text = label_font.render('Crash Cymbal', True, white)
    screen.blit(crash_text, (30, 330))
    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (30, 430))
    tom_text = label_font.render('Floor Tom', True, white)
    screen.blit(tom_text, (30, 530))

    #Drawing lines to delineate the instruments
    for i in range(1, instruments):
        pygame.draw.line(screen, green, (0, (i * 100)), (250, (i*100)), 4)

    for i in range(beats):
        for j in range(instruments):
            rect = pygame.draw.rect(screen, green, [i * ((WIDTH - 250) // beats) + 250, (j * 100), ((WIDTH - 250) // beats), ((HEIGHT - 250) // instruments) + 8], 4, 8)

    


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




