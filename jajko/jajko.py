#!/usr/bin/env python3
import sys

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *

import random
import math

N = 25

u_tab = []
v_tab = []
u = v = 0.0
for i in range(N): #wypełnienie u_tab i v_tab wartościami od 0.0 do 1.0
    u_tab.append(u)
    v_tab.append(v)
    u += 1 / (N - 1)
    v += 1 / (N - 1)


def get_random_color(): #tworzenie randomowych kolorów
    red = random.random()
    green = random.random()
    blue = random.random()
    return red, green, blue


vertex = list()
colors = list()
for u in range(N):
    vertex.append(list())
    colors.append(list())
    for v in range(N):
        x = (-90 * u_tab[u] ** 5 + 225 * u_tab[u] ** 4 - 270 * u_tab[u] ** 3 + 180 * u_tab[u] ** 2 - 45 * u_tab[u]) * math.cos(3.1415 * v_tab[v])
        y = 160 * u_tab[u] ** 4 - 320 * u_tab[u] ** 3 + 160 * u_tab[u] ** 2 - 5
        z = (-90 * u_tab[u] ** 5 + 225 * u_tab[u] ** 4 - 270 * u_tab[u] ** 3 + 180 * u_tab[u] ** 2 - 45 * u_tab[u]) * math.sin(3.1415 * v_tab[v])
        xyz = [x, y, z]
        colors[u].append(get_random_color())
        vertex[u].append(xyz)


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()


def egg_points():
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_POINTS)
    for u in range(N):
        for v in range(N):
            glVertex3f(vertex[u][v][0], vertex[u][v][1], vertex[u][v][2])
    glEnd()


def egg_lines():
    glColor3f(1.0, 1.0, 1.0)
    for u in range(N-1):
        for v in range(N-1):
            glBegin(GL_LINES)
            glVertex3f(vertex[u][v][0], vertex[u][v][1], vertex[u][v][2])
            glVertex3f(vertex[u+1][v][0], vertex[u+1][v][1], vertex[u+1][v][2])

            glVertex3f(vertex[u][v][0], vertex[u][v][1], vertex[u][v][2])
            glVertex3f(vertex[u][v+1][0], vertex[u][v+1][1], vertex[u][v+1][2])
            glEnd()


def egg_triangles():
    for u in range(N-1):
        colors[u][0] = colors[N - 1 - u][N - 1] #aby nie było widać linii "połączenia"
        colors[u][1] = colors[N - 1 - u][N - 2]
        for v in range(N-1):
            glBegin(GL_TRIANGLES)
            glColor3f(colors[u][v][0], colors[u][v][1], colors[u][v][2])
            glVertex3f(vertex[u][v][0], vertex[u][v][1], vertex[u][v][2])

            glColor3f(colors[u + 1][v][0], colors[u + 1][v][1], colors[u + 1][v][2])
            glVertex3f(vertex[u + 1][v][0], vertex[u + 1][v][1], vertex[u + 1][v][2])

            glColor3f(colors[u][v + 1][0], colors[u][v + 1][1], colors[u][v + 1][2])
            glVertex3f(vertex[u][v + 1][0], vertex[u][v + 1][1], vertex[u][v + 1][2])


            glColor3f(colors[u+1][v+1][0], colors[u+1][v+1][1], colors[u+1][v+1][2])
            glVertex3f(vertex[u+1][v+1][0], vertex[u+1][v+1][1], vertex[u+1][v+1][2])

            glColor3f(colors[u + 1][v][0], colors[u + 1][v][1], colors[u + 1][v][2])
            glVertex3f(vertex[u + 1][v][0], vertex[u + 1][v][1], vertex[u + 1][v][2])

            glColor3f(colors[u][v + 1][0], colors[u][v + 1][1], colors[u][v + 1][2])
            glVertex3f(vertex[u][v + 1][0], vertex[u][v + 1][1], vertex[u][v + 1][2])
            glEnd()


def egg_triangle_strip():
    glBegin(GL_TRIANGLE_STRIP)
    for u in range(N-1):
        colors[u][0] = colors[N - 1 - u][N - 1]
        colors[u][1] = colors[N - 1 - u][N - 2]

        for v in range(N-1):
            glColor3f(colors[u][v][0], colors[u][v][1], colors[u][v][2])
            glVertex3f(vertex[u][v][0], vertex[u][v][1], vertex[u][v][2])

            glColor3f(colors[u][v + 1][0], colors[u][v + 1][1], colors[u][v + 1][2])
            glVertex3f(vertex[u][v + 1][0], vertex[u][v + 1][1], vertex[u][v + 1][2])

            glColor3f(colors[u + 1][v][0], colors[u + 1][v][1], colors[u + 1][v][2])
            glVertex3f(vertex[u + 1][v][0], vertex[u + 1][v][1], vertex[u + 1][v][2])

            glColor3f(colors[u + 1][v + 1][0], colors[u + 1][v + 1][1], colors[u + 1][v + 1][2])
            glVertex3f(vertex[u+1][v+1][0], vertex[u+1][v+1][1], vertex[u+1][v+1][2])
    glEnd()


def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    spin(time * 180 / 3.1415)

    # egg_points()
    # egg_lines()
    egg_triangles()
    # egg_triangle_strip()

    axes()
    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()

    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
