import pygame
from material.cores import cor
from material.personagens import jovem, estudante
from pygame.locals import *

def game():
    pygame.init()

    largura = 500
    altura = 400

    pos_x = largura/2
    pos_y = altura/2
    m, n = 0, 0
    velocidade = 10


    janela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("IFgame")

    click = False

    aberto = True

    while aberto:
        pygame.time.delay(50)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                aberto = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        comandos = pygame.key.get_pressed()

        if comandos[pygame.K_DOWN]:
            pos_y += velocidade
            m = 0
            n += 1
            if n > 3:
                n = 0

        if comandos[pygame.K_UP]:
            pos_y -= velocidade
            m = 1
            n += 1
            if n > 3:
                n = 0

        if comandos[pygame.K_LEFT]:
            pos_x -= velocidade
            m = 2
            n += 1
            if n > 3:
                n = 0

        if comandos[pygame.K_RIGHT]:
            pos_x += velocidade
            m = 3
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


        voltar = pygame.Rect(50, 100, 200, 50)

        mx, my = pygame.mouse.get_pos()

        if voltar.collidepoint((mx, my)):
            if click:
                menu()

        pygame.draw.rect(janela, cor.Preto, voltar)
        janela.fill(cor.Azul_Brilhante)
        janela.blit(estudante.estudante[m][n], (pos_x, pos_y))


        pygame.display.update()

    pygame.quit()

























































