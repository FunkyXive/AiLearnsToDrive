import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time
import pygame
import tensorflow

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Deja vu Simulator")

clock = pygame.time.Clock()

crashed = False
class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.carImg = pygame.image.load("car.png")
        self.rotation = 0
        gameDisplay.blit(self.carImg, (self.x, self.y))

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


        print(event)

    car = Car(100,100)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
