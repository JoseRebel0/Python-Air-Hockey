
import pygame
import math
import sys, pygame
from pygame.locals import *
from pygame.draw import circle

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
GREEN=(0, 255, 0)
RED=(255, 0, 0)
RED2=(186,0,0)
BLUE=(0, 0, 255)
BLUE2=(32, 42, 68)
BLUE3=(28,57,187)
BACKG=(47,68,84)
YELLOW=(255,186,1)
GREY=(105,105,105)

def jogador1(screen,x_coord,y_coord):
    pygame.draw.circle(screen, RED2, [x_coord, y_coord], 50, 50)
    pygame.draw.circle(screen, RED, [x_coord, y_coord], 30, 30)

    
def jogador2(screen,x_coord2,y_coord2):
    pygame.draw.circle(screen, BLUE2, [x_coord2, y_coord2], 50, 50)
    pygame.draw.circle(screen, BLUE, [x_coord2, y_coord2], 30, 30)    

pygame.init()

size=(1000,500)
screen=pygame.display.set_mode(size)

pygame.display.set_caption('Air Hockey')

done=False
clock=pygame.time.Clock()

# Esconder o cursor do rato
pygame.mouse.set_visible(0)

#Coisas para o disco
circle_x = 500
circle_y = 250
# Velocidade e direção do ângulo
circle_change_x = 5
circle_change_y = 5

#Coisas para os controlos
# Velocidade nos pixels por frame
x_speed = 0
y_speed = 0
x_speed2 = 0
y_speed2 = 0

# Posição
x_coord = 200
y_coord = 250
x_coord2 = 800
y_coord2 = 250

colidiu=False
pontos1=0
pontos2=0

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    
    # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed2 = -3
            elif event.key == pygame.K_RIGHT:
                x_speed2 = 3
            elif event.key == pygame.K_UP:
                y_speed2 = -3
            elif event.key == pygame.K_DOWN:
                y_speed2 = 3

            if event.key == pygame.K_a:
                x_speed = -3
            elif event.key == pygame.K_d:
                x_speed = 3
            elif event.key == pygame.K_w:
                y_speed = -3
            elif event.key == pygame.K_s:
                y_speed = 3

            # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed2 = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed2 = 0        

            # User let up on a key
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_speed = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                y_speed = 0     


    #Mover o objeto conforme o veto de velocidade
    x_coord += x_speed
    y_coord += y_speed
    x_coord2 += x_speed2
    y_coord2 += y_speed2

    screen.fill(BACKG)
    
    pygame.draw.line(screen,YELLOW,[945,0],[945,172],2)
    pygame.draw.line(screen,YELLOW,[945,320],[945,500],2)
    pygame.draw.line(screen,YELLOW,[50,0],[50,173],2)
    pygame.draw.line(screen,YELLOW,[50,320],[50,500],2)
    pygame.draw.line(screen,YELLOW,[500,0],[500,500],2)
    pygame.draw.line(screen,YELLOW,[625,0],[625,500],2)
    pygame.draw.line(screen,YELLOW,[375,0],[375,500],2)
    
    #Linhas de perda de velocidade
    pygame.draw.line(screen,BLUE3,[0,0],[1000,0],2)
    pygame.draw.line(screen,BLUE3,[0,499],[1000,499],2)
    pygame.draw.line(screen,BLUE3,[0,0],[0,499],2)
    pygame.draw.line(screen,BLUE3,[999,499],[999,0],2)


    #Linhas de ponto
    pygame.draw.line(screen,GREEN,[0,150],[0,350],1)
    pygame.draw.line(screen,GREEN,[999,150],[999,350],1)
    #pygame.draw.line(screen,YELLOW,[800,0],[0,0],1)
    
    #y_offset=0
    #while y_offset<100:
        #pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5)
        #y_offset=y_offset+10
    
    #for i in range(200):
 
        #radians_x = i / 20
        #radians_y = i / 6
 
        #x = int(75 * math.sin(radians_x)) + 200
        #y = int(75 * math.cos(radians_y)) + 200
 
        #pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)

    #for x_offset in range(30, 300, 30):
    #    pygame.draw.line(screen,BLACK,[x_offset,100],[x_offset-10,90],2)
    #    pygame.draw.line(screen,BLACK,[x_offset,90],[x_offset-10,100],2)
    
    #pygame.draw.rect(screen,BLACK,[20,20,250,100],2)
    #pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)
    pygame.draw.arc(screen, YELLOW, [870,170,150,155],  math.pi/2,     math.pi, 3)
    pygame.draw.arc(screen, YELLOW, [-22,170,149,150],     0,   math.pi/2, 3)
    pygame.draw.arc(screen, YELLOW,   [-22,171,148,150],3*math.pi/2,   2*math.pi, 3)
    pygame.draw.arc(screen, YELLOW,  [870,170,150,155],    math.pi, 3*math.pi/2, 3)
    
    #Cículos amarelos
    pygame.draw.circle(screen, YELLOW, [500,250],80,2)
    pygame.draw.circle(screen, YELLOW, [500,250],65,2)
    pygame.draw.circle(screen, YELLOW, [500,250],46,0)

    #Círculos brancos
    pygame.draw.circle(screen, WHITE, [225,100],70,2)
    pygame.draw.circle(screen, WHITE, [225,400],70,2)
    pygame.draw.circle(screen, WHITE, [800,100],70,2)
    pygame.draw.circle(screen, WHITE, [800,400],70,2)

    #Disco
    pygame.draw.circle(screen, BLACK, [circle_x, circle_y], 30, 60)
    pygame.draw.circle(screen, GREY, [circle_x , circle_y ], 20, 35)


    #rects para colisão
    rectlinha1=pygame.Rect(0,0,1000,0)
    rectlinha2=pygame.Rect(0,499,1000,0)
    rectlinha3=pygame.Rect(0,0,0,499)
    rectlinha4=pygame.Rect(999,499,999,0)
    rectg1=pygame.Rect(1,150,1,350)
    rectg2=pygame.Rect(999,150,999,350)
    rect3=pygame.Rect(x_coord2, y_coord2,50, 50)
    rect2=pygame.Rect(circle_x, circle_y,30,60)
    rect1 = pygame.Rect(x_coord,y_coord,50,50)
    #Colisão entre o disco e os jogadores
    collide= rect1.colliderect(rect2)
    collide2=rect3.colliderect(rect2)
    #Colisão para ponto
    collide3=rect2.colliderect(rectg1)
    collide4=rect2.colliderect(rectg2)
    #Colisão para perda de velocidade
    collide5=rect2.colliderect(rectlinha1)
    collide6=rect2.colliderect(rectlinha2)
    collide7=rect2.colliderect(rectlinha3)
    collide8=rect2.colliderect(rectlinha4)

    if collide:
        print('Colidiu')
        colidiu = True
        circle_change_x = circle_change_x * -1  

    if collide2:
        print('Também colidiu')
        colidiu = True
        circle_change_x = circle_change_x * -1  

    if collide3 :
        print('Ponto!')
        #colidiu=True
        pontos1=pontos1+1
        circle_x = 500
        circle_y = 250

        circle_change_x = 5
        circle_change_y = 5

        x_speed = 0
        y_speed = 0
        x_speed2 = 0
        y_speed2 = 0

        x_coord = 200
        y_coord = 250
        x_coord2 = 800
        y_coord2 = 250

        colidiu=False

    if collide4:
        print('Ponto!')
        colidiu=True
        pontos2=pontos2+1
        circle_x = 500
        circle_y = 250

        circle_change_x = 5
        circle_change_y = 5

        x_speed = 0
        y_speed = 0
        x_speed2 = 0
        y_speed2 = 0

        x_coord = 200
        y_coord = 250
        x_coord2 = 800
        y_coord2 = 250

        colidiu=False


    if colidiu:
        circle_x += circle_change_x
        circle_y += circle_change_y

    if circle_y > 490 or circle_y < 0:
        circle_change_y = circle_change_y * -1
    if circle_x > 990 or circle_x < 0:
        circle_change_x = circle_change_x * -1   

    jogador1(screen, x_coord, y_coord)
    jogador2(screen, x_coord2, y_coord2)
    

    
    #pygame.draw.polygon(screen, BLACK, [[100,100], [0,200], [200,200]], 5)
    font = pygame.font.SysFont('Comic Sans MS', 25, True, False)

    pontos2
    text = font.render('Score:'+ str(pontos2),True,BLACK)
    screen.blit(text, [50, 50])
    
    text2 = font.render('Score:' + str(pontos1),True,BLACK)
    screen.blit(text2, [850, 50])

 
    
    pygame.display.flip()

    clock.tick(150)

pygame.quit