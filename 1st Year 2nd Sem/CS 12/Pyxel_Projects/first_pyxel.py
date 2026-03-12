import pyxel
from pyxel import rect, text, circ, btn, btnp, btnr
from time import sleep

'''def update(): 
    pass 

def draw(): 
    # pyxel.text(x, y, text_string, color_index) 
    pyxel.text(0, 0, 'Hello, world!', 1) 

pyxel.init(100, 100) 
pyxel.run(update, draw)'''

class ClassicalPhysics:
    def __init__(self, g: int = 10, t: int = 1):
        self.g = g
        self.t = t


    def drop(self, t: int | float) -> int:
        return int((1/2)*(-self.g)*((t/100)**2))



class Bird:
    def __init__(self, radius: int = 15, x: int | float = 0, y: int | float = 0, color: int = 10, physics: ClassicalPhysics = ClassicalPhysics()):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.physics = physics

    def change_x(self, dx: int | float) -> None:
        self.x -= dx
    def change_y(self, dy: int | float) -> None:
        self.y -= dy



screen_w = 500
screen_h = 500

pyxel.init(screen_w, screen_h, title="My Game", fps=100)

centisecond = 0

b = Bird()
b.x = screen_w // 2
b.y = screen_h // 2

def update() -> None:
    global centisecond

    centisecond += 1

    print(f"centi: {centisecond}  g: {b.physics.g}  disp: {b.physics.drop(centisecond)}")

    b.change_y(b.physics.drop(centisecond))
    if btnp(pyxel.KEY_Q):
        pyxel.quit()
    if btn(pyxel.KEY_J):
        b.change_y(12)
        centisecond = 0

def draw() -> None:
    pyxel.cls(0)
    #pyxel.rect(0, 0, 30, 30, 7)
    circ(b.x, b.y, b.radius, b.color)
    
    


pyxel.run(update, draw)