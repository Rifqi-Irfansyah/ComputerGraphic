import numpy as np
import math

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

class Pattern():
    SOLID = 1
    DASHED = 2
    DOTTED = 3
    DASH_DOT = 4
    
def line_bresenham(xa, ya, xb, yb, pattern):
    if abs(yb - ya) < abs(xb - xa):
        if xa > xb:
            return np.array(line_low(xb, yb, xa, ya, pattern))
        else:
            return np.array(line_low(xa, ya, xb, yb, pattern))
    else:
        if ya > yb:
            return np.array(line_high(xb, yb, xa, ya, pattern))
        else:
            return np.array(line_high(xa, ya, xb, yb, pattern))

def line_low(xa, ya, xb, yb, pattern):
    res = []
    dx = xb - xa
    dy = yb - ya
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    p = (2 * dy) - dx
    twody = 2 * dy
    twodydx = 2 * (dy - dx)
    y = ya
    pattern_counter = 0
    dash_length = 5
    gap_length = 5

    for x in range(int(xa), int(xb + 1)):
        if pattern == Pattern.SOLID:
            res.append([x, y])
        elif pattern == Pattern.DASHED:
            if pattern_counter < dash_length:
                res.append([x, y])
            pattern_counter = (pattern_counter + 1) % (dash_length + gap_length)
        elif pattern == Pattern.DOTTED:
            if pattern_counter == 0:
                res.append([x, y])
                pattern_counter = 1
            elif pattern_counter == 1:
                pattern_counter = 0
        elif pattern == Pattern.DASH_DOT:
            if pattern_counter == 1:
                pass
            elif pattern_counter < dash_length:
                res.append([x, y])
            pattern_counter = (pattern_counter + 1) % (dash_length + gap_length)
        
        if p > 0:
            y += yi
            p += twodydx
        else:
            p += twody
    
    return res

def line_high(xa, ya, xb, yb, pattern):
    res = []
    dx = xb - xa
    dy = yb - ya
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    p = (2 * dx) - dy
    twodx = 2 * dx
    twodxdy = 2 * (dx - dy)
    x = xa
    pattern_counter = 0
    dash_length = 5  # contoh panjang dash
    gap_length = 5   # contoh panjang gap

    for y in range(int(ya), int(yb + 1)):
        if pattern == Pattern.SOLID:
            res.append([x, y])
        elif pattern == Pattern.DASHED:
            if pattern_counter < dash_length:
                res.append([x, y])
            pattern_counter = (pattern_counter + 1) % (dash_length + gap_length)
        elif pattern == Pattern.DOTTED:
            if pattern_counter == 0:
                res.append([x, y])
                pattern_counter = 1
            elif pattern_counter == 1:
                pattern_counter = 0
        elif pattern == Pattern.DASH_DOT:
            if pattern_counter == 1:
                pass
            elif pattern_counter < dash_length:
                res.append([x, y])
            pattern_counter = (pattern_counter + 1) % (dash_length + gap_length)
        
        if p > 0:
            x += xi
            p += twodxdy
        else:
            p += twodx
    
    return res