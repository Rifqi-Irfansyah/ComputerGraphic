import py5
import numpy as np
import math
from random import randint

# https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

def line_bresenham(xa,ya,xb,yb):
    if(abs(yb-ya) < abs(xb-xa)):
        if(xa > xb):
            return np.array(line_low(xb,yb,xa,ya))
        else:
            return np.array(line_low(xa,ya,xb,yb))
    else:
        if(ya > yb):
            return np.array(line_high(xb,yb,xa,ya))
        else:
            return np.array(line_high(xa,ya,xb,yb))

def line_low(xa,ya,xb,yb):
    res = [[xa,ya]]
    dx = xb-xa
    dy = yb-ya
    yi = 1
    if (dy < 0):
        yi = -1
        dy = -dy
    p = (2*dy)- dx
    twody = 2*dy
    twodydx = 2*(dy-dx)
    y = ya
    
    for x in range(xa,xb):
        res.append([x,y])
        if(p > 0):
            y += yi
            p += twodydx
        else:
            p += twody
    
    return res

def line_high(xa,ya,xb,yb):
    res = [[xa,ya]]
    
    dx = xb-xa
    dy = yb-ya
    xi = 1
    if (dx < 0):
        xi = -1
        dx = -dx
    p = (2*dx)- dy
    twodx = 2*dx
    twodxdy = 2*(dx-dy)
    x = xa
    
    for y in range(ya,yb):
        res.append([x,y])
        if(p > 0):
            x += xi
            p += twodxdy
        else:
            p += twodx
    
    return res

def setup():
    py5.size(500,500)

def draw():
    py5.stroke(randint(0,255),0,0,255)
    py5.points(
        line_bresenham(
            50,50,500,400
            )
        )

py5.run_sketch()
