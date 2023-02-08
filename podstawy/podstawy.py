#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def render(time):
    # do_triangle()
    # do_rectangle(-70.0, 10.0, 30.0, 40.0)
    glClear(GL_COLOR_BUFFER_BIT)
    # do_rectangle_deform(-70.0, 10.0, 30.0, 40.0, 1.0, 0.0, 0.0, 1.5)
    x = -40
    y = -25
    a = 50
    b = 70
    do_rectangle_deform(x, y, a, b, 0.0, 0.0, 0.0, 0.0)
    do_fractal(x, y, a, b, 2)
    glFlush()


def do_triangle():
    #zad 1
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-50.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.0, 50.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(50.0, 0.0)
    glEnd()
    glFlush()


def do_rectangle(x, y, a, b):
    #zad 2
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(x, y)
    glVertex2f(x, y + b)
    glVertex2f(x + a, y)
    glVertex2f(x + a, y + b)
    glEnd()
    glFlush()


def do_rectangle_deform(x, y, a, b, red, green, blue, d):
    #zad 3
    if d == 0.0:
        d = 1

    glColor3f(red, green, blue)
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x + b * d, y)
    glVertex2f(x, y + a * d)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x + b * d, y + a * d)
    glVertex2f(x + b * d, y)
    glVertex2f(x, y + a * d)
    glEnd()


def do_fractal(x, y, a, b, n):
    #zad 4
    d = 0.0
    red = 1.0
    green = 1.0
    blue = 1.0

    a = a / 3
    b = b / 3
    do_rectangle_deform(x + b, y + a, a, b, red, green, blue, d)

    for i in range(n):
        do_fractal(x, y, a, b, n - 1)
        do_fractal(x, y + a, a, b, n - 1)
        do_fractal(x, y + 2 * a, a, b, n - 1)
        do_fractal(x + b, y, a, b, n - 1)
        do_fractal(x + b, y + 2 * a, a, b, n - 1)
        do_fractal(x + 2 * b, y, a, b, n - 1)
        do_fractal(x + 2 * b, y + a, a, b, n - 1)
        do_fractal(x + 2 * b, y + 2 * a, a, b, n - 1)


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
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


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
        #do_fractal(-50.0, -50.0, 80.0, 120.0)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
