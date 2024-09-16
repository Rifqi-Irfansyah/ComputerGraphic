import py5
import primitif.line
import primitif.basic
import primitif.utility

import math

time = 50
frame = 0

def setup():
    py5.size(800, 600)
    margin = 5
    py5.rect_mode(py5.CENTER)

    
    

def draw():
    global frame
    py5.background(191)
   
    
    margin = 25
    
    x = -200
    y = 140
    width = 100
    height = 100
    x, y = convert_to_cartesian(x, y, py5.width, py5.width, margin)
    primitif.basic.persegi(x, y, width, c=[0,0,0,255])
    
    
    x = 100
    y = 340
    width = 100
    height = 100
    x, y = convert_to_cartesian(x, y, py5.width, py5.width, margin)
    primitif.basic.persegi_panjang(x, y, 100, 200, c=[0,0,0,255])
            
    x = -150
    y = -140
    width = 100
    height = 100
    x, y = convert_to_cartesian(x, y, py5.width, py5.width, margin)
    primitif.basic.segitiga_siku(x, y, 100, 200, c=[0,0,0,255])
            
    x = 100
    y = 30
    width = 100
    height = 100
    x, y = convert_to_cartesian(x, y, py5.width, py5.width, margin)
    primitif.basic.trapesium_siku(x, y, 100, 200, 80, c=[0,0,0,255])


def convert_to_cartesian(xa, ya, width, height, margin):
    axis = math.ceil(width/2)
    ordinat = math.ceil(height/2)
    
    return [axis+xa, ordinat-ya]

py5.run_sketch()

