import pygame
from cores import cor
from personagens import per
from pygame.locals import *
from random import randint

pygame.init()

largura = 800
altura = 500

pos_x = largura/2
pos_y = altura/2
m, n = 0, 0
velocidade = 10
person = per.jovem[m][n]

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("IFgame")

aberto = True

while aberto:
    pygame.time.delay(50)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            aberto = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_DOWN]:
        pos_y += velocidade
        person = per.jovem[0][n]
        n += 1
        if n > 3:
            n = 0

    if comandos[pygame.K_UP]:
        pos_y -= velocidade
        person = per.jovem[1][n]
        n += 1
        if n > 3:
            n = 0

    if comandos[pygame.K_LEFT]:
        pos_x -= velocidade
        person = per.jovem[2][n]
        n += 1
        if n > 3:
            n = 0

    if comandos[pygame.K_RIGHT]:
        pos_x += velocidade
        person = per.jovem[3][n]
        n += 1
        if n > 3:
            n = 0



    if pos_x >= (largura + 10):
        pos_x = -50
    else:
        if pos_x <= -50:
            pos_x = (largura + 10)

    if pos_y >= (altura + 10):
        pos_y = -80
    else:
        if pos_y <= -80:
            pos_y = (altura + 10)

    janela.fill(cor.Azul_Brilhante)
    janela.blit(person, (pos_x, pos_y))

    pygame.display.update()

pygame.quit()
