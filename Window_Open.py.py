#Import pygame library
import pygame

#Initialize game engine
pygame.init()

#Define colours
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)

#Set width and height of screen
size=[700,500]
screen=pygame.display.set_mode(size)

#Sets name at the top of the window
pygame.display.set_caption("Half-Life 3")

#Loop until the user clicks the close button
done=False

#Used to manage how fast the screen updates
clock=pygame.time.Clock()

#Main program loop:
while done==False:

    for event in pygame.event.get():        #User input
        if event.type == pygame.QUIT:       #If user closes program
            done=True                       #Loop exit
    clock.tick(20)

pygame.quit()                               #Quit game when program is closed
