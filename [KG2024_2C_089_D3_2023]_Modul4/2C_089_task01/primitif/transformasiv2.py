import numpy as np
import math

def translate2D(tx, ty, tm):
    m = np.identity(3)
    m[0][2] = tx
    m[1][2]=ty
    return np.dot(m, tm)

def scale2D(sx, sy, refx, refy, tm):
    m = np.identity(3)
    m[0][0] = sx
    m[0][2] = (1-sx)*refx
    m[1][1] = sy 
    m[1][2] = (1-sy)*refy
    return np.dot(m, tm)

def rotate2D(a, refx, refy):
    m = np.identity(3)
    tm = np.identity(3)
    a = math.radians(a)
    m[0][0] = round(math.cos(a))
    m[0][1] = round(- math.sin(a))
    m[0][2] = refx * (1 - round(math.cos(a))) + refy * round(math.sin(a))
    m[1][0] = round(math.sin(a))
    m[1][1] = round(math.cos(a))
    m[1][2] = refy * (1 -round(math.cos(a))) - refx * round(math.sin(a))
    return np.dot(m, tm)

def transformPoints2D(pts, tm):
    i, _  = pts.shape
    
    for k in range(i):
        tmp = tm[0][0] * pts[k,0] + tm[0][1] * pts[k,1] + tm[0][2]
        pts[k,1] = tm[1][0] * pts[k,0] + tm[1][1] * pts[k,1] + tm[1][2]
        pts[k,0] = tmp

    return pts