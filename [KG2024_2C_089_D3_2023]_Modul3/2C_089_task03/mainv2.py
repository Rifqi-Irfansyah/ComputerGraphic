import py5
import primitif.line
import primitif.basic
import math
from random import randint

class Asteroid():
    def __init__(self):
        self.x = randint(0,599)
        self.y = randint(0,599)
        
    def draw(self):
        print(self.x, self.y)
        primitif.basic.lingkaran(self.x, self.y, 10)
    
    def move(self):
        self.x = self.x + 1
        self.y = self.y + 1
        
        if self.x > py5.width:
            self.x = randint(0,599)
            self.y = randint(0,599)

space = []
for n in range(10):
    space.append(Asteroid())

def setup():
    py5.size(600, 600)
    
def draw():
    py5.background(0)
    for roid in space:
        roid.move()
        roid.draw()

py5.run_sketch()