import py5
import primitif.line
import primitif.basic
import math
from random import randint

def head(w,h,r):
    py5.ellipse(w/2,h/2, r,r)

def dress(w,h,r):
    py5.triangle(w/2, h/2+r/2, w/2-r, h/2+2*r, w/2+r, h/2+2*r) 

def leg(w,h,r):
    py5.line(w/2-r/2,h/2+2*r, w/2-r/2,h/2+3*r)
    py5.line(w/2+r/2,h/2+2*r, w/2+r/2,h/2+3*r)

def boot(w,h,r):
    py5.ellipse(w/2-r/2-5,h/2+3*r, 10,10)
    py5.ellipse(w/2+r/2+5,h/2+3*r, 10,10)

def setup():
    py5.size(800,600)

def draw():
    w,h,m,r = (py5.width, py5.height, 10, 60 )
    
    head(w,h,r)
    dress(w,h,r)
    leg(w,h,r)
    boot(w,h,r)

py5.run_sketch()
