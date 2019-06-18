import pygame as pg
import random as ram

#paleta de cores utilizada durante o desenvolvimento,
# não encontramos uma utilidade para classes nesse game
class colors:
    white=(255,255,255)
    blue=(0,0,255)
    green=(0,140,0)
    red=(255,0,0)
    orange=(200,100,0)
    black=(0,0,0)

pontosdireita=0
pontosesquerda=0

g = True
principal = True

#exibe a mensagem de início de jogo
def startgame():
    global principal
    g=True
    text = font.render(("Bem vindo ao Fut Pong"),1,cor.white)
    fundo.blit(text, (448, 370))
    text1 = font.render(("Aperte espaço para começar"),1,cor.white)
    fundo.blit(text1, (398, 400))
    pg.display.update()
    while g:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    g = False
            elif event.type == pg.QUIT:
                principal = False
                g=False

#responsável por verificar se algum jogador atingiu
# 5 pontos e assim encerrar o jogo, começando uma nova partida
def endgame():
    global principal, pontosdireita, pontosesquerda
    g = True
    if pontosdireita==5 or pontosesquerda==5:
        if pontosdireita>pontosesquerda:
            text = font.render(("Jogador direito venceu!"),1,cor.white)
            fundo.blit(text, (455, 370))
            text1 = font.render(("Aperte espaço para recomeçar"),1,cor.white)
            fundo.blit(text1, (398, 400))
            pg.display.update()
            while g:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            g = False
                    elif event.type == pg.QUIT:
                        g = False
                        principal = False
            print('Jogador esquerdo venceu!')


        elif pontosdireita<pontosesquerda:
            text = font.render(("Jogador esquerdo venceu!"),1,cor.white)
            fundo.blit(text, (428, 370))
            text = font.render(("Aperte espaço para recomeçar"),1,cor.white)
            fundo.blit(text, (398, 400))
            pg.display.update()
            while g:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            g = False

                    elif event.type == pg.QUIT:
                        g = False
                        principal = False
            print('Jogador direito venceu!')

        pontosdireita = 0
        pontosesquerda = 0


#sempre é chamado quando placar estiver abaixo de 5
#para exibir a mensagem de continuação
def continua():
    global principal
    g=True

    if x<0:
        text = font.render(("Jogador esquerdo marcou!"),1,cor.white)
        fundo.blit(text, (425,310))
        text = font.render(("Pressione espaço para continuar"),1,cor.white)
        fundo.blit(text, (370,345))
        pg.display.update()
    elif x>0:
        text = font.render(("Jogador direito marcou!"),1,cor.white)
        fundo.blit(text, (430,310))
        text = font.render(("Pressione espaço para continuar"),1,cor.white)
        fundo.blit(text, (370,345))
        pg.display.update()

    while g:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    g = False
            elif event.type == pg.QUIT:
                g = False
                principal = False

#tamanho da janela em pixels
largura=1280
altura=720

#define as raquetes
raqueteesquerda = pg.Rect(65,240,10,200)
raquetedireita = pg.Rect(1200,240,10,200)

#define a bola
bola = pg.Rect(largura/2,altura/2,10,10)

#define os limites superior e inferiro
superior = pg.Rect(0,-10,1280,10)
inferior = pg.Rect(0,720,1280,10)

#define os contadores de ponto
retangulocontesquerdo = pg.Rect(-190,0,200,720)
retangulocontdireito = pg.Rect(1270,0,200,720)

#inicia o pygame
pg.init()

#define a fonte de texto utilizada
pg.font.init()
font1 = pg.font.get_default_font()
font = pg.font.SysFont(font1, 50)

#velocidade com que a raquete se move
move = 10

#configuração de FPS e controle de uso da CPU
pg.mixer.quit()
clock = pg.time.Clock()

#velocida inicial X da bola
velocidade_bola = 5

#randomiza X e Y da bola no início do jogo
y = ram.choice([-3,3])
x = ram.choice([-velocidade_bola,velocidade_bola])

#define a janela, nome do jogo
fundo = pg.display.set_mode((largura,altura))
pg.display.set_caption('FUT PONG')

#chama a paleta de cores
cor = colors()

#exibe a mensagem de início do jogo
startgame()

# Loop principal do jogo
while principal:

    #fechamento da janela
    for event in pg.event.get():
        if event.type == pg.QUIT:
            principal = False
    #teclas
    teclas_pressionadas = pg.key.get_pressed()

    if teclas_pressionadas[pg.K_UP]:
        if not superior.colliderect(raquetedireita):
            raquetedireita.move_ip(0,-move)

    if teclas_pressionadas[pg.K_DOWN]:
        if not inferior.colliderect(raquetedireita):
            raquetedireita.move_ip(0,+move)

    if teclas_pressionadas[pg.K_w]:
        if not superior.colliderect(raqueteesquerda):
            raqueteesquerda.move_ip(0,-move)

    if teclas_pressionadas[pg.K_s]:
        if not inferior.colliderect(raqueteesquerda):
            raqueteesquerda.move_ip(0,+move)



    #inversores de sinal +/- de X quando a bola bater na raquete
    if raquetedireita.colliderect(bola):
        x += (1 * (x / abs(x)))
        x = x * -1
        i = ram.choice([1,2])
        if i==1:
            y = y * -1

    elif raqueteesquerda.colliderect(bola):
        x += (1 * (x / abs(x)))
        x = x * -1
        i = ram.choice([1,2])
        if i==1:
            y = y * -1


    #inversores de sinal +/- de Y quando a bola bater no
    #limite superior ou inferior
    if superior.colliderect(bola):
        y = y * -1

    elif inferior.colliderect(bola):
        y = y * -1


    #contadores de pontos para quando a bola bater no final da janela,
    #redefine a posição inicial das raquetes e da bola, além de permitir a
    #continuação do jogo. Também define que quem marca o ponto, recomeça
    #o jogo tendo de defender-se
    if retangulocontdireito.colliderect(bola):
        pontosesquerda+=1
        bola = pg.Rect(largura/2,altura/2,10,10)
        x = -abs(velocidade_bola)
        raqueteesquerda = pg.Rect(65,240,10,200)
        raquetedireita = pg.Rect(1200,240,10,200)
        if pontosesquerda<5:
            continua()

    elif retangulocontesquerdo.colliderect(bola):
        pontosdireita+=1
        bola = pg.Rect(largura/2,altura/2,10,10)
        x = abs(velocidade_bola)
        raqueteesquerda = pg.Rect(65,240,10,200)
        raquetedireita = pg.Rect(1200,240,10,200)
        if pontosdireita<5:
            continua()

    #responsável por fazer a movimentação da bola X e Y
    #pré definidos no início
    bola.move_ip(x,y)

    #define o fundo da janela
    fundo.fill(cor.black)

    #define o placar no topo da janela
    text = font.render((str(pontosesquerda)),1,cor.white)
    fundo.blit(text, (600, 10))

    text = font.render((str(pontosdireita)),1,cor.white)
    fundo.blit(text, (660, 10))

    text = font.render(('x'),1,cor.white)
    fundo.blit(text, (630, 10))

    #sempre é chamado para verificar o possível fim de jogo
    endgame()

    #define a propriedade reativa de impacto das raquetes
    pg.draw.rect(fundo,cor.white,raqueteesquerda)
    pg.draw.rect(fundo,cor.white,raquetedireita)

    #define a propriedade reativa de impacto dos limites superior
    # e inferior
    pg.draw.rect(fundo,cor.white,superior)
    pg.draw.rect(fundo,cor.white,inferior)

    #define a propriedade reativa de impacto dos contadores de ponto
    pg.draw.rect(fundo,cor.red,retangulocontdireito)
    pg.draw.rect(fundo,cor.red,retangulocontesquerdo)

    #define a propriedade reativa de impacto da bola
    pg.draw.rect(fundo,cor.white,bola)

    #sempre que chamado, atualiza a informação exibida na tela
    pg.display.update()

    #FPS
    clock.tick(120)
pg.quit()
