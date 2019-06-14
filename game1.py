import pygame as pg
import random as ram

class colors:
    white=(255,255,255)
    blue=(0,0,255)
    green=(0,140,0)
    red=(255,0,0)
    orange=(200,100,0)
    black=(0,0,0)

# class powerup:
#     def

pontosdireita=0
pontosesquerda=0
#att = pontosesquerda
#att1 = pontosdireita

g = True
sair = True

def startgame():
    global sair
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
                sair = False
                g=False
def endgame():
    global sair, pontosdireita, pontosesquerda
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
                        sair = False
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
                        sair = False
            print('Jogador direito venceu!')

        pontosdireita = 0
        pontosesquerda = 0

def continua():
    global sair
    g=True

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
                sair = False



largura=1280
altura=720

interancoes = 0

altura_da_raquete = 200
raqueteesquerda = pg.Rect(65,240,10,altura_da_raquete)
raquetedireita = pg.Rect(1200,240,10,altura_da_raquete)
#raqueteesquerda = pg.Rect(-25,240,100,altura_da_raquete)
#raquetedireita = pg.Rect(1200,240,100,altura_da_raquete)

bola = pg.Rect(largura/2,altura/2,10,10)

superior = pg.Rect(0,-10,1280,10)
inferior = pg.Rect(0,720,1280,10)

retangulocontesquerdo = pg.Rect(-190,0,200,720)
retangulocontdireito = pg.Rect(1270,0,200,720)
#retangulocontesquerdo = pg.Rect(0,0,10,720)
#retangulocontdireito = pg.Rect(1270,0,10,720)


pg.init()
#pg.key.set_repeat(5)

pg.font.init()
font1 = pg.font.get_default_font()
font = pg.font.SysFont(font1, 50)

move = 10

pg.mixer.quit()
clock = pg.time.Clock()

velocidade_bola = 5

y = ram.choice([-3,3])
x = ram.choice([-velocidade_bola,velocidade_bola])

fundo = pg.display.set_mode((largura,altura))
pg.display.set_caption('FUT PONG')
cor = colors()

startgame()
# Loop principal

while sair:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sair = False

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




    if raquetedireita.colliderect(bola):
        altura_da_raquete = altura_da_raquete-20

        x += (1 * (x / abs(x)))

        x = x * -1
        i = ram.choice([1,2])
        #y = ram.choice([-6,6])
        #y = 6
        if i==1:
            y = y * -1

    elif raqueteesquerda.colliderect(bola):
        altura_da_raquete = altura_da_raquete-20

        x += (1 * (x / abs(x)))

        x = x * -1

        i = ram.choice([1,2])
        #y = ram.choice([-6,6])
        #y = 6
        if i==1:
            y = y * -1

    if superior.colliderect(bola):
        y = y * -1

    elif inferior.colliderect(bola):
        y = y * -1



    if retangulocontdireito.colliderect(bola):
        pontosesquerda+=1
        print('Jogador esquerdo',pontosdireita)
        bola = pg.Rect(largura/2,altura/2,10,10)
        x = -abs(velocidade_bola)
        altura_da_raquete = 200
        raqueteesquerda = pg.Rect(65,240,10,altura_da_raquete)
        raquetedireita = pg.Rect(1200,240,10,altura_da_raquete)
        #raqueteesquerda = pg.Rect(-25,240,100,altura_da_raquete)
        #raquetedireita = pg.Rect(1200,240,100,altura_da_raquete)
        if pontosesquerda<5:

            continua()



    elif retangulocontesquerdo.colliderect(bola):
        pontosdireita+=1
        print('Jogador direito',pontosesquerda)
        bola = pg.Rect(largura/2,altura/2,10,10)
        x = abs(velocidade_bola)
        altura_da_raquete = 200
        raqueteesquerda = pg.Rect(65,240,10,altura_da_raquete)
        raquetedireita = pg.Rect(1200,240,10,altura_da_raquete)
        #raqueteesquerda = pg.Rect(-25,240,100,altura_da_raquete)
        #raquetedireita = pg.Rect(1200,240,100,altura_da_raquete)
        if pontosdireita<5:

            continua()


    bola.move_ip(x,y)
    fundo.fill(cor.black)


    text = font.render((str(pontosesquerda)),1,cor.white)
    fundo.blit(text, (600, 10))

    text = font.render((str(pontosdireita)),1,cor.white)
    fundo.blit(text, (660, 10))

    text = font.render(('x'),1,cor.white)
    fundo.blit(text, (630, 10))

    endgame()


#plataformas
    pg.draw.rect(fundo,cor.white,raqueteesquerda)
    pg.draw.rect(fundo,cor.white,raquetedireita)
#superior e inferior
    pg.draw.rect(fundo,cor.white,superior)
    pg.draw.rect(fundo,cor.white,inferior)


#contadores de pontos
    pg.draw.rect(fundo,cor.red,retangulocontdireito)
    pg.draw.rect(fundo,cor.red,retangulocontesquerdo)
#bolinha
    pg.draw.rect(fundo,cor.white,bola)

    pg.display.update()
    clock.tick(120)
pg.quit()
