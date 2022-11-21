import pygame
import numpy as np
import math
from math import *
from pygame.locals import *

vertex = []
faces = []
shape_info = []
# Reading provided csv txt file
with open("object.txt", 'r') as file:
    for i, line in enumerate(file):
        if i == 0:
            shape_info.append(list(map(int, line.strip().split(','))))
        elif 1 <= i <= shape_info[0][0]:
            vertex.append(list(map(float, line.strip().split(','))))
        else:
            faces.append(list(map(int, line.strip().split(','))))
    file.close()
    pass

points = [x[1:] for x in vertex]


def max_points(points):
    max_val = max(map(max, points))
    return max_val


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

max_element = max_points(points)
WIDTH = HEIGHT = 300 * max_element
circle_pos = [WIDTH / 2, HEIGHT / 2]
pygame.display.set_caption("Projection")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

scale = 100

angle_x = angle_y = 0

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])

projected_points = [
    [n, n] for n in range(len(points))
]


def rotation_x(point):
    # defining the rotation matrix
    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(angle_x), -sin(angle_x)],
        [0, sin(angle_x), cos(angle_x)],
    ])
    # calculating the rotated points
    rotated_x = np.dot(rotation_x, np.array(point).reshape((3, 1)))
    return rotated_x


def rotation_xy(rotated2d_x):
    # defining the rotation matrix
    rotation_y = np.matrix([
        [cos(angle_y), 0, sin(angle_y)],
        [0, 1, 0],
        [-sin(angle_y), 0, cos(angle_y)],
    ])
    # calculating the rotated points
    rotated_xy = np.dot(rotation_y, rotated2d_x)
    return rotated_xy


def cal_projection(rotated2d_xy):
    # defining the projection matrix (since last row is (0,0,0) it can be omitted)
    projection_matrix = np.matrix([
        [1, 0, 0],
        [0, 1, 0]
    ])
    # calculating projection
    projection = np.dot(projection_matrix, rotated2d_xy)
    return projection


def draw_vertex(projected2d):
    # defining x and y w.r.t the centre
    x_ = int(projected2d[0][0] * scale) + circle_pos[0]
    y_ = int(projected2d[1][0] * scale) + circle_pos[1]
    # storing the values in projected_points
    projected_points[i] = [x_, y_]
    # drawing the concerned vertex
    pygame.draw.circle(screen, BLUE, (x_, y_), 5)


def connect_points(i, j, points):
    # connecting points corresponding to vertex unique ID i, j
    pygame.draw.line(screen, BLUE, (points[i - 1][0], points[i - 1][1]), (points[j - 1][0], points[j - 1][1]))


clock = pygame.time.Clock()
clicking = False
while True:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        if event.type == pygame.MOUSEMOTION and event.buttons[0]:
            if event.rel[0] != 0:
                angle_y += math.degrees(event.rel[0] * pi * 0.05 / WIDTH)
            elif event.rel[0] == 0:
                angle_y = angle_y
            if event.rel[1] != 0:
                angle_x += math.degrees(event.rel[1] * pi * 0.05 / HEIGHT)
            elif event.rel[1] == 0:
                angle_x = angle_x

    screen.fill(WHITE)

    i = 0
    for point in points:
        rotated2d_x = rotation_x(point)
        rotated2d_xy = rotation_xy(rotated2d_x)
        projected2d = cal_projection(rotated2d_xy)
        draw_vertex(projected2d)
        i += 1

    for v in faces:
        connect_points(v[0], v[1], projected_points)
        connect_points(v[1], v[2], projected_points)
        connect_points(v[2], v[0], projected_points)

    pygame.display.update()

pygame.quit()
