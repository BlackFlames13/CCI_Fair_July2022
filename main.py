#CCI Fair July 2022 - Riyaan R.
#Shoot Up Project
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Shoot Up!")
#Colors
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)
yellow=(255,255,0)
grey=(107,103,103)
#Clock (FPS/Hz)
clock=pygame.time.Clock()
hz=240
print("Would you like to play easy, medium, hard, or super hard mode?")
print("Please enter 60 if you want easy mode. Please enter 150 for the medium mode. Please enter 200 for the hard mode. Please enter 240 for the super hard mode.")
hz=int(input())
#Plaer
mx=350
my=665
left=0
right=0
#Bullet
bx=mx
by=my
space=0
shots=0
#Aliens
ax=0
ay=0
#Points
score=0
while True:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                left=1
            if event.key==K_RIGHT:
                right=1
        if event.type==MOUSEBUTTONDOWN:
            if event.button==1:
                pygame.draw.circle(screen,green,(bx,by),5,0)
                by=by-20
                space=1
        if event.type==KEYUP:
            if event.key==K_LEFT:
                left=0
            if event.key==K_RIGHT:
                right=0  
        if event.type==QUIT:
            pygame.quit()
            exit()
    if left==1:
        mx=mx-3
        bx=mx
    if right==1:
        mx=mx+3
        bx=mx
    screen.fill(black)
    pygame.draw.circle(screen,red,(mx,my),35,0)
    if mx<=0:
        mx=350
    if mx>=700:
        mx=350
    if space==1:
        pygame.draw.circle(screen,green,(bx,by),5,0)
        by=by-10
    if by<=0:
        by=my
        space=0
        shots=shots+1
    pygame.draw.rect(screen,white,(ax,ay,100,30),0)
    if ax>=601:
        ax=600
        a=1
    if ax<=0:
        ax=0
        a=0
    if a==0:
        if hz==60:
            ax=ax+1
        if hz==150:
            ax=ax+3
        if hz==200:
            ax=ax+4
        if hz==240:
            ax=ax+5
    if a==1:
        if hz==60:
            ax=ax-1
        if hz==150:
            ax=ax-3
        if hz==200:
            ax=ax-4
        if hz==240:
            ax=ax-5
    if bx in range(ax,ax+100):
        if by in range(ay,ay+30):
            by=my
            score=score+1
    if score==10:
        print("You won! It took you",shots,"shots to kill 10 UFOs.")
        pygame.quit()
        exit()
    clock.tick(hz)
    pygame.display.update()
