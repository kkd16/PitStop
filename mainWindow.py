# MAIN FRAME WITH GRAPHICS
import pygame

import time
import math
import timeFunctions
import getx
import facts

#initialize function
f = open("userdata.txt", "w")
f.close()

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
bg0 = pygame.image.load('mainpage.jpg')
bg1 = pygame.image.load('progresspage1.1.jpg')
bg2 = pygame.image.load('scorepage1.1.jpg')
bg3 = pygame.image.load('statspage.jpg')
homePagePooIcon = pygame.image.load('poopicon.png')
homePageTrendsIcon = pygame.image.load('arrowicon.png')
dot1 = pygame.image.load('dot/dot1.png')
dot2 = pygame.image.load('dot/dot2.png')
dot3 = pygame.image.load('dot/dot3.png')
star1 = pygame.image.load('stars/star1.png')
star2 = pygame.image.load('stars/star2.png')
star3 = pygame.image.load('stars/star3.png')
star4 = pygame.image.load('stars/star4.png')
star5 = pygame.image.load('stars/star5.png')

# Colours
black = (0,0,0)
white = (255,255,255)
grey = (177,177,177)
greyLight = (240,240,240)

# Fonts
franklinLarge=pygame.font.SysFont("Franklin", 135)
franklinMed=pygame.font.SysFont("Franklin", 40)
franklinSmall=pygame.font.SysFont("Franklin", 25)

# Run Modes
modes = 0 # 0=home, 1=timer, 2=endtimer, 3=trends
dots = 0 # 0 dots, 1 dot, 2 dots, 3 dots

# Timer?
clock = pygame.time.Clock()

# User
oliver = User("Oliver", 74)

# Temps and stuff
totalSeconds = 0
freezeTimerString = ""
accum = 0
stars = 0
starTimer = 0
currentFact = ""

####

## OBJECT INITIALIZATION ##

text = franklinLarge.render(timerString, True, black, greyLight)
textRect = text.get_rect()
textRect.center = (195, 295)

bottomText = franklinSmall.render("Welcome, " + oliver.name + "!", True, grey, white)
bottomTextRect = bottomText.get_rect()
bottomTextRect.center = (197, 675)

stat1 = franklinMed.render( timeFunctions.getFastest(), True, black, white)
stat1Rect = stat1.get_rect()
stat1Rect.center = (197, 300)

stat2 = franklinMed.render( timeFunctions.getLargest(), True, black, white)
stat2Rect = stat2.get_rect()
stat2Rect.center = (197, 400)

stat3 = franklinMed.render( timeFunctions.getAverage(), True, black, white)
stat3Rect = stat3.get_rect()
stat3Rect.center = (197, 400)

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
            if modes==0 and (mousePos[0]>25 and mousePos[0]<373) and (mousePos[1]>382 and mousePos[1]<592):
                modes=1
                timerInt = 0
                tick = 0
                currentFact = facts.getFact("facts.txt")
                bottomText = franklinSmall.render(currentFact, True, grey, white)
                bottomTextRect.center = (getx.getx(currentFact), 675)

            # Poo stop button pressed
            elif modes==1 and (mousePos[0]>33 and mousePos[0]<358)and (mousePos[1]>491 and mousePos[1]<589):
                modes=2
                totalSeconds = timeFunctions.calcSeconds(timerString)
                freezeTimerString = timerString

                # Star determining
                accum = 0
                if totalSeconds < 60:
                    stars = 5
                elif totalSeconds < 120:
                    stars = 4
                elif totalSeconds < 240:
                    stars = 3
                elif totalSeconds < 480:
                    stars = 2
                elif totalSeconds < 600:
                    stars = 1
                else :
                    stars = 0

                #temporary print for time difference
                print("Time Difference: \n")
                print(timeFunctions.stop(timerString))

            elif modes==0 and (mousePos[0]>22 and mousePos[0]<375)and (mousePos[1]>132 and mousePos[1]<342):
                modes = 3
        
    # Update display

    # Home screen
    if modes == 0:
        screen.fill(white)
        img(bg0, 0, 0)
        img(homePagePooIcon, 0, 0)
        img(homePageTrendsIcon, 0, 0)
        screen.blit(bottomText, bottomTextRect)

    # In timer screen
    elif modes==1:
        # Update UI
        screen.fill(white)

        img(bg1, 0, 0)

        if dots == 1 :
            img(dot1, 0, 0)

        elif dots == 2 :
            img(dot1, 0, 0)
            img(dot2, 0, 0)
        
        elif dots == 3 :
            img(dot1, 0, 0)
            img(dot2, 0, 0)
            img(dot3, 0, 0)

        if (tick/60 % 1) == 0:
            if dots == 0:
                dots=1
            elif dots == 1:
                dots=2
            elif dots == 2:
                dots=3
            else:
                dots=0
        
        # Timer
        text = franklinLarge.render(timerString, True, black, greyLight)
        screen.blit(text, textRect)
                
        mins, secs = divmod(timerInt, 60)
        timerString = '{:02d}:{:02d}'.format(mins, secs)
        tick += 1

        timerInt = math.floor(tick/60)

        # Facts
        screen.blit(bottomText, bottomTextRect)
        if (tick/60 % 10) == 0:
            currentFact = facts.getFact("facts.txt")
            bottomText = franklinSmall.render(currentFact, True, grey, white)
            bottomTextRect.center = (getx.getx(currentFact), 675)
    
    # End timer screen
    elif modes==2:
        # Update UI
        screen.fill(white)
        img(bg2, 0, 0)

        text = franklinLarge.render(freezeTimerString, True, black, greyLight)
        screen.blit(text, textRect)

        # Stars
        starTimer += 1

        if accum == 1:
            img(star1, 0 , 0)
        elif accum == 2:
            img(star2, 0 , 0)
        elif accum == 3:
            img(star3, 0 , 0)
        elif accum == 4:
            img(star4, 0 , 0)
        else:
            img(star5, 0 , 0)
        
        if (starTimer % 15) == 0 :
            if accum < stars:
                accum += 1

    else :
        screen.fill(white)
        img(bg3, 0, 0)
        screen.blit(stat1, stat1Rect)
        screen.blit(stat2, stat2Rect)
        screen.blit(stat3, stat3Rect)

    pygame.display.update()
    clock.tick(60)