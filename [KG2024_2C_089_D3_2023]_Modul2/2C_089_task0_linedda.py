import py5
import numpy as np
import math
from random import randint

def round(x):
    return int(x+0.5)

def line_dda(xa, ya, xb, yb):      
    dx = abs(xb - xa)
    dy = abs(yb - ya)
    
    length = max(dx,dy)
    dx = (xb-xa)/length
    dy = (yb-ya)/length
    
    x = xa
    y = ya
    res = [[xa, ya]]
    
    for i in range(length+1):    
        res.append([round(x), round(y)])
        x = x+dx
        y = y+dy
    return np.array(res)

def setup():
    py5.size(500,500)

def draw():
    py5.stroke(0,randint(0,255),0,255)
    py5.points(
        line_dda(
            50,40,400,40
            )
        )

py5.run_sketch()