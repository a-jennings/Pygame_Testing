import pygame

pygame.init()

screen_size=[1000,600]
screen_display=pygame.display.set_mode(screen_size)
pygame.display.set_caption("Test game 1")

end_game=False
clock=pygame.time.Clock()

while end_game==False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game == True
    clock.tick(20)


pygame.quit()


#Currently window doesn't close without PyShell reset.
