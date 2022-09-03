import pygame
from random import randint
pygame.init

#vars
screen = pygame.display.set_mode((500,500))
cops = [pygame.image.load("cop1.png"),pygame.image.load("cop2.png"),pygame.image.load("cop3.png")]
robbers = [pygame.image.load("robber1.png"),pygame.image.load("robber2.png"),pygame.image.load("robber3.png")]
bg = pygame.image.load("background-pixilart.png")
cop_farme = 0
robber_farame = 0
loop = True
x = 0
AI_x = 100
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    #lode image
    screen.blit(bg,(0,0))
    screen.blit(cops[cop_farme],(x,310))
    screen.blit(robbers[robber_farame],(AI_x,310))
    #move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x = x + 5

    if keys[pygame.K_LEFT]:
        x = x - 5


    #AI CODE

    if AI_x > x:
        AI_x = AI_x + 1
    else:
        AI_x = AI_x - 1



    if AI_x < 500:
        AI_x = AI_x + 1
        print("bord")
    elif AI_x < 0:
        AI_x = AI_x - 1
        print("bord")
    pygame.display.update()
