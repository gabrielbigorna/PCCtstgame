import pygame
from cores import cor
from personagens import per
from pygame.locals import *
from random import randint

pygame.init()

janela = pygame.display.set_mode((500, 400))

person = per.jovem[0][0]

m, n = 0, 0

pygame.display.set_caption("!!!!!!!!!!!!!!!!!!TESTE!!!!!!!!!!!!!!!!!")

velocidade = 10
pos_x = 0
pos_y = 200

aberto = True

while aberto:
    pygame.time.delay(50)

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            aberto = False


    janela.fill(cor.Wheat)
    janela.blit(person, (pos_x, pos_y))

    person = per.jovem[m][n]


    m = 3
    n += 1

    if n > 2:
        n = 0

    pos_x += 10

    if pos_x > 510:
        pos_x = -50



    pygame.display.update()

pygame.quit()