import primitif.matrix as matrix
import numpy as np
import math

def translate2D(tx, ty, tm=matrix.zero_matrix3x3()):
    pass

def scale2D(sx, sy, refx, refy, tm=matrix.zero_matrix3x3()):
    pass

def rotate2D(a, refx, refy, tm=matrix.zero_matrix3x3()):
    m = matrix.identity_matrix()
    a = math.radians(a)
    pass

def transformPoints2D(pts, tm=matrix.zero_matrix3x3()):
    i, _  = pts.shape
    
    for k in range(i):
        tmp = tm[0][0] * pts[k,0] + tm[0][1] * pts[k,1] + tm[0][2]
        pts[k,1] = tm[1][0] * pts[k,0] + tm[1][1] * pts[k,1] + tm[1][2]
        pts[k,0] = tmp

    return pts
        
        