import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time
import math
import pygame
from pygame.math import Vector2
from CustomModules import rotateByCenter, Colours, intersection

pygame.init()
gameDisplay = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Deja vu Simulator")

clock = pygame.time.Clock()
colour = Colours()
crashed = False
ppu = 11.11


class Line:
    def __init__(self, point1, point2, surface):
        self.point1 = point1
        self.point2 = point2
        self.colour = colour.black
        self.line = pygame.draw.line(surface, self.colour, self.point1, self.point2, 4)
        # self.A = (self.point1[1] - self.point1[1])
        # self.B = (self.point2[0] - self.point1[0])
        # self.C = (self.point1[0] * self.point2[1] - self.point2[0] * self.point1[1])


class Track:
    def __init__(self):
        self.trackImg = pygame.image.load('track.png')
        self.leftEdge = []
        self.colour = colour.black
        self.leftPointList = [(303, 144), (1079, 145), (1193, 175), (1224, 201), (1272, 266), (1295, 326), (1304, 384),
                              (1304, 446), (1294, 501), (1261, 579), (1230, 620), (1177, 660), (1093, 680), (259, 679),
                              (152, 623), (115, 574), (82, 492), (73, 434), (75, 369), (87, 315), (108, 263),
                              (134, 223), (186, 174), (224, 156), (264, 145)]

    def draw(self):
        for point in range(len(self.leftPointList)):
            try:
                self.leftEdge.append(pygame.draw.line(gameDisplay, colour.black, self.leftPointList[point - 1], self.leftPointList[point]))
            finally:
                pass


class Car:
    def __init__(self, x, y):
        # position
        self.position = Vector2(x, y)
        #self.carImg = pygame.image.load("car.png")
        self.carImg = pygame.draw.circle(gameDisplay, colour.white, (x,y), 10)
        #self.carImg = pygame.transform.smoothscale(self.carImg, (30, 30))
        #self.carImgRect = self.carImg.get_rect()
        # self.carRect = self.carImg.get_rect()
        self.velocity = Vector2(0.0, 0.0)
        self.maxVelocity = 50
        self.currAcc = 0.0
        self.maxAcc = 100
        self.width = 50
        self.height = 24
        # steering
        self.rotation = 0
        self.lines = []

    def accelerate(self, backwards=False):
        if not backwards:
            self.currAcc += 10
        elif backwards:
            self.currAcc -= 20
        if self.currAcc > self.maxAcc:
            self.currAcc = self.maxAcc
        elif self.currAcc < -self.maxAcc:
            self.currAcc = -self.maxAcc

    def rotate(self, rotation):
        self.rotation += rotation

    def draw(self):
        #rotated, rect, corners = rotateByCenter(self.carImg, self.rotation, (self.position.x, self.position.y))
        #rotated = pygame.transform.rotate(self.carImg, self.rotation)
        self.carImg = pygame.draw.circle(gameDisplay, colour.white, (int(round(self.position.x)), int(round(self.position.y))), 10)
        # self.lines.append(Line(corners[0], corners[1], gameDisplay))
        # self.lines.append(Line(corners[1], corners[2], gameDisplay))
        # self.lines.append(Line(corners[2], corners[3], gameDisplay))
        # self.lines.append(Line(corners[3], corners[0], gameDisplay))

        self.velocity += (self.currAcc * 0.01666666666, 0)
        self.position += self.velocity.rotate(-self.rotation) * 0.01666666666 * ppu
        if self.velocity.x >= self.maxVelocity:
            self.velocity.x = self.maxVelocity
        elif self.velocity.x <= -self.maxVelocity:
            self.velocity.x = -self.maxVelocity


car = Car(674, 210)
track = Track()
frames = 0
while not crashed:
    frames +=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    # if car.carImgRect.
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        car.position.x, car.position.y = (0, 0)
        car.velocity.x, car.velocity.y = (0, 0)
    if pressed[pygame.K_w]:
        car.accelerate()
    elif pressed[pygame.K_s]:
        car.accelerate(backwards=True)
    elif not pressed[pygame.K_w] and not pressed[pygame.K_s]:
        if car.velocity.x > 0:
            car.accelerate(backwards=True)
        elif car.velocity.x < 0:
            car.accelerate()
    if pressed[pygame.K_a]:
        car.rotate(6)
    elif pressed[pygame.K_d]:
        car.rotate(-6)
    elif not pressed[pygame.K_w] and not pressed[pygame.K_s]:
        if car.velocity.x < 6:
            car.velocity.x = 0
        else:
            car.velocity *= 0.99


    # print(car.velocity)d
    # rotated = pygame.transform.rotate(car.carImg, car.currSteeringAngle)
    #if frames % 60 == 0:
    #    gameDisplay.fill(colour.red)
    #else:
    gameDisplay.fill(colour.weirdGreen)
    gameDisplay.blit(track.trackImg, (0, 0))
    track.draw()
    car.draw()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
