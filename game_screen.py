import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
from sprites import *
def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING
    pontos=0

    lista_de_imagens= pygame.sprite.Group()
    for i in range(5):

        chiuaua= ChihuahuaOrMuffin(dicionario_de_arquivos)
        lista_de_imagens.add(chiuaua)

    # ===== Loop principal =====
    while state != DONE:
        font = pygame.font.SysFont(None, 40)
        text = font.render(f'PONTOS: {pontos} ', True, (255, 255, 255))
        clock.tick(FPS)
        vidas=0
            
            # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.MOUSEBUTTONUP:
                for foto in lista_de_imagens:
                    if foto.rect.collidepoint(event.pos):
                        foto.kill()
                        chiuaua= ChihuahuaOrMuffin(dicionario_de_arquivos)
                        lista_de_imagens.add(chiuaua)
                        if foto.chiuaua==True:
                            pontos+=1
                        else:
                            chiuaua= ChihuahuaOrMuffin(dicionario_de_arquivos)
                            lista_de_imagens.add(chiuaua)
                    




                        
            
        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        lista_de_imagens.update()
        lista_de_imagens.draw(window)
        window.blit(text, (10,10))
        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
