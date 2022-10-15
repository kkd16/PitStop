# MAIN FRAME WITH GRAPHICS
import pygame

import time
import math
import timeFunctions

#Timer string
timerString = "00:00"
timerInt = 0
tick = 0

## ALL FUNCTIONS ##

# Image display function
def img(img, x, y):
    if img!=None :
        screen.blit(img, (x,y))

####

## ALL CLASSES ##

class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age

####

## WINDOW INITIALIZATION ##

pygame.init()

background_colour = (255,255,255)
(width, height) = (394, 700)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PitStop')
screen.fill(background_colour)

pygame.display.flip()

####

## VARIABLE INITIALIZATION ##

# Images
bg = pygame.image.load('mainpage.jpg')

# Colours
black = (0,0,0)
white = (255,255,255)
grey = (177,177,177)

# Fonts
franklinLarge=pygame.font.SysFont("Franklin", 40)
franklinSmall=pygame.font.SysFont("Franklin", 25)

# Run Modes
modes = 0 # 0=home, 1=timer, 2=endtimer, 3=trends

# Timer?
clock = pygame.time.Clock()

# User
oliver = User("Oliver", 74)

####

## OBJECT INITIALIZATION ##

text = franklinLarge.render(timerString, True, black, white)
textRect = text.get_rect()
textRect.center = (150, 350)

welcomeBack = franklinSmall.render("Welcome, " + oliver.name + "!", True, black, white)
welcomeBackRect = welcomeBack.get_rect()
welcomeBackRect.center = (197, 675)

####

# Main Runtime loop
running = True
while running:
    # Check events code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            mousePos=pygame.mouse.get_pos()

            # Homescreen Poo button presssed
            if modes==0 and (mousePos[0]>43 and mousePos[0]<343) and (mousePos[1]>50 and mousePos[1]<200):
                modes=1
                timerInt = 0
                tick = 0
        
    # Update display

    # Homescreen
    if modes == 0:
        screen.fill(white)
        img(bg, 0, 0)
        screen.blit(welcomeBack, welcomeBackRect)

    # In timer
    elif modes==1:
        screen.fill(white)
        text = franklinLarge.render(timerString, True, black, white)
        screen.blit(text, textRect)

        mins, secs = divmod(timerInt, 60)
        timerString = '{:02d}:{:02d}'.format(mins, secs)
        print(timerString, end="\r")
        #time.sleep(1)
        tick += 1

        timerInt = math.floor(tick/60)

    pygame.display.update()
    clock.tick(60)