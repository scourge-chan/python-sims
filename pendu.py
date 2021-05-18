import pygame
import math
from pygame.locals import *

#CHANGE ROD_LENGTHS, ROD_VELS, AND ROD_ANGLES TO CHANGE INITIAL PENDULUM STATE

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("1000 pendulums lmao")

rod_lengths = [100, 50, 75, 20, 100]
rod_vels = [0,0,0,0,0]
rod_angles = [1, 2, 0, 1, 0.5]

rod_points = [[720, 360]]

gravity = -0.01

running = True

rod_start = [540,360]

pendulumAnim = True

drawPoints = []

while running:
    screen.fill((255,255,255))
    rod_pos_cur = [720, 360]


    #print(rod_pos_cur)

    if pendulumAnim:

        for i in range(len(rod_lengths)):

            rod_x, rod_y = rod_lengths[i] * math.cos(rod_angles[i]), rod_lengths[i] * math.sin(rod_angles[i])

            #print(rod_angle, rod_vel)
            pygame.draw.circle(screen, (0,0,0), rod_pos_cur, 5)
            pygame.draw.line(screen, (0,0,0), rod_pos_cur, (rod_pos_cur[0] + int(rod_x), rod_pos_cur[1] + int(rod_y)), 3)

            rod_pos_cur[0] += int(rod_x)
            rod_pos_cur[1] += int(rod_y)

            #a = (540 + rod_length * int(math.sin(rod_angle)), 360 + rod_length* int(math.cos(rod_angle)))


            rod_vels[i] += gravity * math.cos(rod_angles[i]) * math.pi
            rod_angles[i] -= rod_vels[i] / rod_lengths[i]



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()
