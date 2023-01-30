import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR

# Recebe uma imagem de sprite sheet e retorna uma lista de imagens.
# É necessário definir quantos sprites estão presentes em cada linha e coluna.
# Essa função assume que os sprites no sprite sheet possuem todos o mesmo tamanho.
def load_spritesheet(spritesheet, rows, columns):
    # Calcula a largura e altura de cada sprite.
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows

    # Percorre todos os sprites adicionando em uma lista.
    sprites = []
    for row in range(rows):
        for column in range(columns):
            # Calcula posição do sprite atual
            x = column * sprite_width
            y = row * sprite_height
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            # Cria uma imagem vazia do tamanho do sprite
            image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites

def carrega_arquivos():
    dicionario_de_arquivos = {}

    # Carregando a imagens ChihuahuaOrMuffin
    dicionario_de_arquivos['ChihuahuaOrMuffin'] = pygame.image.load(os.path.join(IMG_DIR, 'ChihuahuaOrMuffin.jpg')).convert()
    rows = 4
    columns = 4
    dicionario_de_arquivos['ChihuahuaOrMuffin'] = load_spritesheet(dicionario_de_arquivos['ChihuahuaOrMuffin'], rows, columns)

    # Fazendo a separação das imagens
    chihuahua = [1, 3, 4, 6, 9, 11, 12, 14]
    muffin = [0, 2, 5, 7, 8, 10, 13, 15]
    tamanho = 80
    dicionario_de_arquivos['Chihuahua'] = [pygame.transform.scale(dicionario_de_arquivos['ChihuahuaOrMuffin'][index], (tamanho, tamanho)) for index in chihuahua]
    dicionario_de_arquivos['Muffin'] = [pygame.transform.scale(dicionario_de_arquivos['ChihuahuaOrMuffin'][index], (tamanho, tamanho)) for index in muffin]

    dicionario_de_arquivos['btn'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1.png')).convert()
    
    #mudando tamanho das imagens
    largura = dicionario_de_arquivos['btn'].get_rect().width * .25
    altura = dicionario_de_arquivos['btn'].get_rect().height * .25
    dicionario_de_arquivos['btn'] = pygame.transform.scale(dicionario_de_arquivos['btn'], (largura, altura))

    dicionario_de_arquivos['btn_hover'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1_hover.png')).convert()
    dicionario_de_arquivos['btn_hover'] = pygame.transform.scale(dicionario_de_arquivos['btn_hover'], (largura, altura))

    #carregando Fonte
    dicionario_de_arquivos['font'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 22)
    dicionario_de_arquivos['font_media'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 30)
    return dicionario_de_arquivos
