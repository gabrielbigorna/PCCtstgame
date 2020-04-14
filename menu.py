import pygame
from pygame.locals import *
from material.img.telaMenu.telaMenu import telaMenu
from jogo import *

def menu():
    pygame.init()

    largura = 500
    altura = 400

    janela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Menu")

    opc = 1

    aberto = True

    while aberto:
        pygame.time.delay(100)

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                aberto = False

        comandos = pygame.key.get_pressed()

        if comandos[pygame.K_DOWN]:
            opc +=1
            if opc > 3:
                opc = 1

        if comandos[pygame.K_UP]:
            opc -= 1
            if opc < 1:
                opc = 3


        if comandos[pygame.K_RETURN] and opc == 1:
            pygame.quit()
            game()
            break


        janela.blit(telaMenu[0], (0,0))
        janela.blit(telaMenu[opc], (0, 0))

        pygame.display.update()

    pygame.quit()

menu()