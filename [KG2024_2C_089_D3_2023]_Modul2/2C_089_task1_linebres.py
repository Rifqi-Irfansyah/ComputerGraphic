import py5
import math
import numpy as np
from random import randint

def line_bresenham(xa, ya, xb, yb):
    dx, dy = abs(xa-xb), abs(ya-yb)
    p = 2 * dy - dx
    twoDy, twoDyDx = 2 * dy, 2 * (dy - dx)
    x,y,xEnd = 0,0,0
    
    if (xa > xb):
        x=xb
        y=yb
        xEnd=xa
    else:
        x=xa
        y=ya
        xEnd=xb
    
    res = [[x,y]]
    
    while(x < xEnd):
        x+=1
        if (p<0):
            p+=twoDy
        else:
            y+=1
            p+=twoDyDx
        res.append([x,y])
    return np.array(res)

def setup():
    py5.size(500,500)

def draw():
    py5.stroke(0,0,randint(0,255),255)
    py5.points(
        line_bresenham(
            50,40,400,40
            )
        )

py5.run_sketch()