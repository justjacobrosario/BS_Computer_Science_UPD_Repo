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

screen_w = 1920
screen_h = 1080

class ClassicalPhysics:
    def __init__(self, g: int = 9.81, t: int = 1):
        self.g = g
        self.t = t


    def drop(self, t: int | float) -> int:
        return int((1/2)*(-self.g)*((t/100)**2))





class Bird:
    def __init__(self, radius: int = 100, x: int | float = 0, y: int | float = 0, color: int = 10, physics: ClassicalPhysics = ClassicalPhysics()):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.physics = physics
        self._tick = 0

    def change_x(self, dx: int | float) -> None:
        self.x -= dx
    def change_y(self, dy: int | float) -> None:
        self.y -= dy

    def tele(self):
        if self.y >= screen_h:
            self._tick += 1
            self.y = 0;
            self.color = self._tick % 10


pyxel.init(screen_w, screen_h, title="My Game", fps=100)

centisecond = 0

b1 = Bird()
b2 = Bird()

b1.x = screen_w // 2
b1.y = screen_h // 2
b1.color = 5

b2.x = screen_w // 4
b2.y = screen_h // 2
b1.color = 7

birds = [b1, b2]

def update() -> None:
    global centisecond

    centisecond += 1

    #print(f"centi: {centisecond}  g: {b.physics.g}  disp: {b.physics.drop(centisecond)}")

    for b in birds:
        b.change_y(b.physics.drop(centisecond))
        if btnp(pyxel.KEY_Q):
            pyxel.quit()
        if btn(pyxel.KEY_J):
            b.change_y(12)
            centisecond = 0

        b.tele()

def draw() -> None:
    pyxel.cls(0)
    #pyxel.rect(0, 0, 30, 30, 7)
    for b in birds:
        circ(b.x, b.y, b.radius, b.color)
    
    


pyxel.run(update, draw)