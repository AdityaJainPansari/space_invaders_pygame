#!/usr/bin/env/python
from random import *
import pygame
import sys
from pygame.locals import *
from space_ship import *
from Missile1 import *
from Missile2 import *
from alien import *

x = 0
count = 0
shots1 = []
shots2 = []
state = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
alien = []
pygame.font.init()
default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 25)


def find_rand():
    temp1 = randint(0, 1)
    flag = 0
    for a in state[temp1]:
        if a == 0:
            flag = 1
            break
    if flag == 0:
        temp1 = temp1 ^ 1
        for a in state[temp1]:
            if a == 0:
                flag = 1
                break
        if flag == 0:
            return 0, 0
    while True:
        temp2 = randint(0, 7)
        if state[temp1][temp2] == 0:
            break
    state[temp1][temp2] = 1
    return temp1+1, temp2


def is_collision(shot, alien):
    if shot.left == alien.left and shot.top == alien.top:
        return True
    else:
        return False


def shot_update():
    for s in shots1:
        if s.is_alive:
            s.update(screen)
    for s in shots2:
        if s.is_alive:
            s.update(screen)


def check():
    for a in alien:
        if a.is_alive > 0:
            for s in shots1:
                if s.is_alive:
                    if is_collision(s, a):
                        s.is_alive = False
                        a.is_alive = 0
                        global count
                        count = count+1
                        state[a.temp1-1][a.temp2] = 0
            for s in shots2:
                if s.is_alive:
                    if is_collision(s, a):
                        s.is_alive = False
                        if a.is_alive > 0:
                            a.alive_time = a.alive_time+4000
                            a.is_alive = 1
            if pygame.time.get_ticks() > a.alive_time:
                a.is_alive = 0
                state[a.temp1-1][a.temp2] = 0


def scr_draw():
    for a in alien:
        if a.is_alive != -1:
            a.draw(screen, ali_ima[a.is_alive])
    for s in shots1:
        if s.is_alive:
            s.draw(screen, bullet1)
    for s in shots2:
        if s.is_alive:
            s.draw(screen, bullet2)


def spawn(state1):
    global width
    if state1[K_SPACE] and not state1[K_s]:
        shots1.append(Missile1(move_x-width/2, screen))
    if state1[K_s] and not state1[K_SPACE]:
        shots2.append(Missile2(move_x-width/2, screen))


clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 640))
pygame.display.update()

width = (int)(screen.get_width()/8)
height = (int)(screen.get_height()/9)
bullet1 = pygame.image.load("bullet.png")
bullet1 = pygame.transform.scale(bullet1, (width, height))
bullet2 = pygame.image.load("bullet3.png")
bullet2 = pygame.transform.scale(bullet2, (width, height))
ali_ima = [0, 0, 0]
ali_ima[0] = pygame.image.load("alien_by1.png")
ali_ima[1] = pygame.image.load("alien_fin.png")
ali_ima[2] = pygame.image.load("alien_ini.png")
ali_ima[0] = pygame.transform.scale(ali_ima[0], (width, height))
ali_ima[1] = pygame.transform.scale(ali_ima[1], (width, height))
ali_ima[2] = pygame.transform.scale(ali_ima[2], (width, height))

move_x = width*7/2
pygame.mouse.set_visible(0)
temp = (int)(height*9/8)
ship = pygame.image.load("spa_shi1.png")
SS = space_ship(width, temp, ship)
SS.ship = pygame.transform.scale(SS.ship, (SS.width, SS.height))

tim = pygame.time.get_ticks()
temp1, temp2 = find_rand()
alien.append(Alien(screen, tim, temp1, temp2))

while True:
    clock.tick(10)
    screen.fill((0, 0, 0))
    screen.blit(SS.ship, (move_x-SS.width/2, SS.top))

    if tim+7000 < pygame.time.get_ticks():
        tim = pygame.time.get_ticks()
        temp1, temp2 = find_rand()
        if temp1 != 0 and temp2 != 0:
            alien.append(Alien(screen, tim, temp1, temp2))

    shot_update()
    check()
    scr_draw()
    label = "Score: " + str(count)
    label = font_renderer.render(label, 1, (255, 255, 255))
    screen.blit(label, (0, screen.get_height()-100))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Congratulations ! Your score is ", count)
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                print("Congratulations ! Your score is ", count)
                sys.exit()
    state1 = pygame.key.get_pressed()
    move_x = SS.movement(move_x, state1[K_a], state1[K_d])
    spawn(state1)


# https://stackoverflow.com/questions/12990602/libpng-warning-interlace-handling-should-be-turned-on-when-using-png-read-image
