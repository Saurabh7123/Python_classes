import pygame
pygame.init()
screen=pygame.display.set_mode((500,400))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,255,255),pygame.Rect(30,40,80,20))
    pygame.display.flip()



          
