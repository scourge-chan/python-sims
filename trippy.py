import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("trippy")

running = True

drawingLine = False
drawingBezier = False
finishedBezier = False
linePoints = []

bezierPos = 0
increase = 0.001

bezierPoints = []
curveDots = []

while running:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #print('quitadf aksdlfasd')
            running = False
        if not drawingBezier:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print("aaaaaaaaaa start drawing plsflsdjfskdf")
                linePoints.append(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                bezierPoints = linePoints.copy()
                drawingBezier = True
        elif finishedBezier:
            if event.type == pygame.KEYDOWN:
                drawingLine = False
                drawingBezier = False
                finishedBezier = False
                linePoints = []

                bezierPos = 0

                bezierPoints = []
                curveDots = []


    if not drawingBezier:
        for i in range(len(linePoints)-1):
            pygame.draw.line(screen, (0,0,0), linePoints[i], linePoints[i+1],2)

        if len(linePoints) > 0:
            pygame.draw.line(screen, (0,0,0), linePoints[-1], pygame.mouse.get_pos(),2)
    else:
        for i in range(len(linePoints)-1):
            pygame.draw.line(screen, (0,0,0), linePoints[i], linePoints[i+1])
            x = (linePoints[i][0]*(1-bezierPos) + linePoints[i+1][0]*bezierPos)
            y = (linePoints[i][1]*(1-bezierPos) + linePoints[i+1][1]*bezierPos)

            bezierPoints[i] = (int(x), int(y))
            print(linePoints, x, y)
            pygame.draw.circle(screen, (0, 0, 0), bezierPoints[i], 5)

            pygame.draw.line(screen, (0, 0, 0), bezierPoints[i], bezierPoints[i+1], 2)

            x1 = (bezierPoints[i][0]*(1-bezierPos) + bezierPoints[i+1][0]*bezierPos)
            y1 = (bezierPoints[i][1]*(1-bezierPos) + bezierPoints[i+1][1]*bezierPos)

            curveDots.append((int(x1), int(y1)))

            if bezierPos < 1:
                bezierPos += increase
            else:
                finishedBezier = True

    pygame.display.update()
