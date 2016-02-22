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
pi=3.141592653

#Loop until the user clicks the close button
done=False

#Used to manage how fast the screen updates
clock=pygame.time.Clock()

#Main program loop:
while done==False:

    #ALL EVENT PROCESSING TO GO HERE:

    for event in pygame.event.get():        #User input
        if event.type == pygame.QUIT:       #If user closes program
            done=True                       #Loop exit
    clock.tick(20)

    #ALL GAME LOGIC TO GO HERE:




    #ALL CODE DRAWING TO GO HERE:
    
    screen.fill(white)
    for x in range(0,100,20):
        pygame.draw.line(screen,green,[x,0],[x,100],5)


    #Draw a rectangle
    pygame.draw.rect(screen,black,[150,50,250,100],1)

    #Draw an ellipse
    pygame.draw.ellipse(screen,black,[150,50,250,100],1)


    #Draw an arc as part of an ellipse. Use radians to
    #determine what angle to draw

    pygame.draw.arc(screen,green, [400,100,250,200], pi/2, pi, 2)
    pygame.draw.arc(screen,black, [400,100,250,200], 0, pi/2, 2)
    pygame.draw.arc(screen,red,   [400,100,250,200], 3*pi/2, 2*pi, 2)
    pygame.draw.arc(screen,blue,  [400,100,250,200], pi, 3*pi/2, 2)

    #Draw a triangle, or any polygon using different point co-ords
    pygame.draw.polygon(screen,red,[[250,250],[100,400],[400,400]],2)
        
    pygame.display.flip()


pygame.quit()                               #Quit game when user closes window
