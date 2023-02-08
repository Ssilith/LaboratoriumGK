import sys

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math


viewer = [0.0, 0.0, 10.0]

rgb = 0.0
param = idx = 0
theta = phi1 = theta1 = 0.0
pix2angle = 1.0
R = 6.0
x_s = y_z = z_s = 1.0

left_mouse_button_pressed = right_mouse_button_pressed = 0
mouse_x_pos_old = mouse_y_pos_old = 0
delta_x = delta_y = 0

mat_ambient = [1.0, 1.0, 1.0, 1.0]
mat_diffuse = [1.0, 1.0, 1.0, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = 20.0

light_ambient = [0.1, 0.1, 0.0, 1.0]
light_diffuse = [0.8, 0.8, 0.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [0.0, 0.0, 10.0, 1.0]

#3.0
light_ambient1 = [0.0, 0.1, 0.1, 1.0]
light_diffuse1 = [0.0, 0.8, 0.8, 1.0]
light_specular1 = [1.0, 1.0, 1.0, 1.0]
light_position1 = [0.0, 10.0, 0.0, 1.0]

att_constant = 1.0
att_linear = 0.05
att_quadratic = 0.001

#4.5
mode = 0
vertex = list()
normal = list()
u_tab = []
v_tab = []
u = v = 0.0
N = 40
for i in range(N):
    u_tab.append(u)
    v_tab.append(v)
    u += 1 / (N - 1)
    v += 1 / (N - 1)

for u in range(N):
    vertex.append(list())
    normal.append(list())
    for v in range(N):
        x = (-90 * u_tab[u] ** 5 + 225 * u_tab[u] ** 4 - 270 * u_tab[u] ** 3 + 180 * u_tab[u] ** 2 - 45 * u_tab[u]) * math.cos(3.1415 * v_tab[v])
        y = 160 * u_tab[u] ** 4 - 320 * u_tab[u] ** 3 + 160 * u_tab[u] ** 2 - 5
        z = (-90 * u_tab[u] ** 5 + 225 * u_tab[u] ** 4 - 270 * u_tab[u] ** 3 + 180 * u_tab[u] ** 2 - 45 * u_tab[u]) * math.sin(3.1415 * v_tab[v])
        xyz = [x, y, z]
        vertex[u].append(xyz)

        xu = (-450 * u_tab[u]**4 + 900 * u_tab[u]**3 - 810 * u_tab[u]**2 + 360 * u_tab[u] - 45) * math.cos(3.1415 * v_tab[v])
        xv = 3.1415 * (90 * u_tab[u]**5 - 225 * u_tab[u]**4 + 270 * u_tab[u]**3 - 180 * u_tab[u]**2 + 45 * u_tab[u]) * math.sin(3.1415 * v_tab[v])
        yu = 640 * u_tab[u]**3 - 960 * u_tab[u]**2 + 320 * u
        yv = 0
        zu = (-450 * u_tab[u]**4 + 900 * u_tab[u]**3 - 810 * u_tab[u]**2 + 360 * u_tab[u] - 45) * math.sin(3.1415 * v_tab[v])
        zv = -3.1415 * (90 * u_tab[u]**5 - 225 * u_tab[u]**4 + 270 * u_tab[u]**3 - 180 * u_tab[u]**2 + 45 * u_tab[u]) * math.cos(3.1415 * v_tab[v])
        mag = math.sqrt((yu * zv - zu * yv)**2 + (zu * xv - xu * zv)**2 + (xu * yv - yu * xv)**2)
        if mag != 0:
            n_xyz = [(yu * zv - zu * yv)/mag, (zu * xv - xu * zv)/mag, (xu * yv - yu * xv)/mag]
        else:
            n_xyz = [(yu * zv - zu * yv), (zu * xv - xu * zv), (xu * yv - yu * xv)]
        normal[u].append(n_xyz)


def egg_triangle_strip():
    glBegin(GL_TRIANGLE_STRIP)
    for u in range(N-1):
        for v in range(N):
            glNormal3f(normal[u][v][0], normal[u][v][1], normal[u][v][2])
            glVertex3f(vertex[u][v][0], vertex[u][v][1], vertex[u][v][2])

            glNormal3f(normal[u + 1][v][0], normal[u + 1][v][1], normal[u + 1][v][2])
            glVertex3f(vertex[u + 1][v][0], vertex[u + 1][v][1], vertex[u + 1][v][2])
    glEnd()


def draw_n_vectors(): #5.0
    for u in range(N - 1):
        for v in range(N - 1):
            glBegin(GL_LINES)
            glVertex3f(vertex[u][v][0], vertex[u][v][1], vertex[u][v][2])
            glVertex3f(vertex[u][v][0] + normal[u][v][0], vertex[u][v][1] + normal[u][v][1], vertex[u][v][2] + normal[u][v][2])
            glEnd()


def change_light_color():
    if param == 0:
        if light_ambient1[idx] != 0.0 and rgb < 0 or light_ambient1[idx] != 1.0 and rgb > 0:
            light_ambient1[idx] = round(light_ambient1[idx] + rgb, 1)
            print('\nlight ambient: ' + str(light_ambient1))
    elif param == 1:
        if light_diffuse1[idx] != 0.0 and rgb < 0 or light_diffuse1[idx] != 1.0 and rgb > 0:
            light_diffuse1[idx] = round(light_diffuse1[idx] + rgb, 1)
            print('\nlight diffuse: ' + str(light_diffuse1))
    else:
        if light_specular1[idx] != 0.0 and rgb < 0 or light_specular1[idx] != 1.0 and rgb > 0:
            light_specular1[idx] = round(light_specular1[idx] + rgb, 1)
            print('\nlight specular: ' + str(light_specular1))

    glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse1)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular1)
    set_light_position()


def set_light_position():
    glLightfv(GL_LIGHT1, GL_POSITION, light_position1)
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, att_quadratic)


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    # glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)


def shutdown():
    pass


def render(time):
    global theta, phi1, theta1, R, light_position1, mode

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(viewer[0], viewer[1], viewer[2],
              0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if left_mouse_button_pressed:
        theta += delta_x * pix2angle

    glRotatef(theta, 0.0, 1.0, 0.0)

    #4.0
    # quadric = gluNewQuadric()
    # gluQuadricDrawStyle(quadric, GLU_FILL)
    # gluSphere(quadric, 3.0, 10, 10)
    egg_triangle_strip()
    glRotatef(-theta, 0.0, -1.0, 0.0)
    # gluDeleteQuadric(quadric)

    if right_mouse_button_pressed:
        theta1 += delta_x * pix2angle
        phi1 += delta_y * pix2angle

    x_s = R * math.cos(math.fmod(theta1 * (math.pi) / 180, 2 * (math.pi))) * math.cos(math.fmod(phi1 * (math.pi) / 180, 2 * (math.pi)))
    y_s = R * math.sin(math.fmod(phi1 * (math.pi) / 180, 2 * (math.pi)))
    z_s = R * math.sin(math.fmod(theta1 * (math.pi) / 180, 2 * (math.pi))) * math.cos(math.fmod(phi1 * (math.pi) / 180, 2 * (math.pi)))
    light_position1 = [x_s, y_s, z_s, 1.0]
    set_light_position()

    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_LINE)
    glTranslatef(x_s, y_s, z_s)
    gluSphere(quadric, 0.5, 6, 5)
    glTranslatef(-x_s, -y_s, -z_s)
    gluDeleteQuadric(quadric)

    if mode == 1:
        draw_n_vectors()

    glFlush()


def update_viewport(window, width, height):
    global pix2angle
    pix2angle = 360.0 / width

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(80, 1.0, 0.1, 300.0)

    if width <= height:
        glViewport(0, int((height - width) / 2), width, width)
    else:
        glViewport(int((width - height) / 2), 0, height, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard_key_callback(window, key, scancode, action, mods):
    global rgb, param, idx, mode
    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)

    if key == GLFW_KEY_SPACE and action == GLFW_PRESS:
        idx = 0
        if param == 0:
            param = 1
        elif param == 1:
            param = 2
        elif param == 2:
            param = 0

    if key == GLFW_KEY_UP and action == GLFW_PRESS:
        rgb = 0.1
        change_light_color()
    if key == GLFW_KEY_DOWN and action == GLFW_PRESS:
        rgb = -0.1
        change_light_color()

    if key == GLFW_KEY_RIGHT and action == GLFW_PRESS:
        if idx == 0:
            idx = 1
        elif idx == 1:
            idx = 2
    if key == GLFW_KEY_LEFT and action == GLFW_PRESS:
        if idx == 2:
            idx = 1
        elif idx == 1:
            idx = 0

    if key == GLFW_KEY_N and action == GLFW_PRESS: #5.0
        if mode == 0:
            mode = 1
        else:
            mode = 0


def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x, delta_y
    global mouse_x_pos_old, mouse_y_pos_old

    delta_x = x_pos - mouse_x_pos_old
    mouse_x_pos_old = x_pos

    delta_y = y_pos - mouse_y_pos_old
    mouse_y_pos_old = y_pos


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed, right_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        left_mouse_button_pressed = 1
    else:
        left_mouse_button_pressed = 0

    if button == GLFW_MOUSE_BUTTON_RIGHT and action == GLFW_PRESS:
        right_mouse_button_pressed = 1
    else:
        right_mouse_button_pressed = 0


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSetKeyCallback(window, keyboard_key_callback)
    glfwSetCursorPosCallback(window, mouse_motion_callback)
    glfwSetMouseButtonCallback(window, mouse_button_callback)
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