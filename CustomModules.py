from __future__ import division

import pygame


def rotateByCenter(img, rotation, position):
    imgRect = img.get_rect()
    rotated = pygame.transform.rotate(img, rotation)
    rect = rotated.get_rect()
    rect.center = imgRect.center
    rect.center = position
    #print(rect)
    corners = (rect.topleft, rect.topright, rect.bottomright, rect.bottomleft)
    return rotated, rect, corners


def intersection(L1, L2):
    D = L1.A * L2.B - L1.B * L2.A
    Dx = L1.C * L2.B - L1.B * L2.C
    Dy = L1.A * L2.C - L1.C * L2.A
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x, y
    else:
        return False


class Colours:
    black = (0, 0, 0)

    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 255)
        self.blue = (0, 0, 255)
        self.weirdGreen = pygame.color.Color("#04e762")
        self.weirdDarkBlue = pygame.color.Color("#003485")
        self.yellowIsh = pygame.color.Color("#f5b700")
        self.lightBlue = pygame.color.Color("#0496ff")
        self.slightlyLighterBlue = pygame.color.Color("#00a1e4")
# print(line_intersection((A, B), (C, D)))
