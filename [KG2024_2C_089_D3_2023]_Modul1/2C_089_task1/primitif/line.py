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