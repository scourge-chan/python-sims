import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("trippy")

font = pygame.font.SysFont(None, 20)
img = font.render('click to start a line, click again to end it.', True, (0,0,0))
img2 = font.render('press any key to start bezier animation.', True, (0,0,0))
img3 = font.render('press any key again after animation to make another bezier', True, (0,0,0))

running = True

drawingLine = False
drawingBezier = False
finishedBezier = False
linePoints = []

bezierPos = 0
increase = 0.001

bezierPoints = []
curveDots = []

colors = [(255,0,0), (0,0,255), (0,255,0), (255,0,255),(0,255,255)]

def getBezierPoint(points, t, prevPoints):
    print(points)
    if len(points) == 2:
        x = (points[0][0]*(1-t) + points[1][0]*t)
        y = (points[0][1]*(1-t) + points[1][1]*t)
        finishedBezier = True
        prevPoints.append(points)
        return (int(x), int(y)), prevPoints
    elif len(points) > 2:
        newpoints = []
        for i in range(len(points)-1):
            x = (points[i][0]*(1-t) + points[i+1][0]*t)
            y = (points[i][1]*(1-t) + points[i+1][1]*t)
            newpoints.append((int(x), int(y)))

        prevPoints.append(points)

        return getBezierPoint(newpoints, t, prevPoints)


while running:
    screen.fill((255,255,255))
    screen.blit(img, (10, 10))
    screen.blit(img2, (10, 30))
    screen.blit(img3, (10, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #print('quitadf aksdlfasd')
            running = False
        if not drawingBezier:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print("aaaaaaaaaa start drawing plsflsdjfskdf")
                linePoints.append(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if len(linePoints) > 1:
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
            pygame.draw.line(screen, (0,0,0), linePoints[i], linePoints[i+1],2)
        if bezierPos < 1:
            bezData = getBezierPoint(linePoints, bezierPos, [])

            bezierPos += increase
            curveDots.append(bezData[0])

            for i in range(len(bezData[1])):
                for j in range(len(bezData[1][i])-1):
                    pygame.draw.circle(screen, (0,0,0), bezData[1][i][j], 3)
                    pygame.draw.circle(screen, (0,0,0), bezData[1][i][j+1], 3)
                    pygame.draw.line(screen, colors[j%5], bezData[1][i][j], bezData[1][i][j+1], 1)

        else:
            finishedBezier = True;
        for i in range(len(curveDots)):
            pygame.draw.circle(screen, (0,0,0), curveDots[i], 1)

    pygame.display.update()
