import pyxel


FPS = 60
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
BIRD_RADIUS = 20
IS_GAME_START = False
IS_GAME_OVER = False

TERMINAL_VELOCITY = 250

bird_x = 40
bird_y = SCREEN_HEIGHT / 2

bird_velocity_y = (50) / FPS
bird_acceleration_y = (10) / FPS


def update():
    global bird_y, bird_velocity_y, bird_acceleration_y
    global IS_GAME_START, IS_GAME_OVER
    global SCREEN_HEIGHT

    if not IS_GAME_START:
        if pyxel.btnp(pyxel.KEY_SPACE):
            IS_GAME_START = True

    if IS_GAME_START and not IS_GAME_OVER:
        if pyxel.btnp(pyxel.KEY_SPACE):
            bird_velocity_y = (-250) / FPS

        bird_y += bird_velocity_y
        bird_velocity_y += bird_acceleration_y

        if bird_y > SCREEN_HEIGHT - BIRD_RADIUS:
            IS_GAME_OVER = True


def draw():
    if not IS_GAME_OVER:
        pyxel.cls(7)
        pyxel.text(15, 15, str(pyxel.frame_count), 0)
        pyxel.circ(bird_x, bird_y, BIRD_RADIUS, 10)


pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=FPS)
pyxel.run(update, draw)
