import py5
import math
import primitif.transformasiv2 as tf
import primitif.basic as basic


rx, ry = 50, 30
xc, yc = 200, 200
angle = 0  

def setup():
    py5.size(400, 400)
    py5.frame_rate(30) 

def draw():
    global angle
    py5.background(255)  
    
    
    ellipse_points = basic.bresenham_ellipse(rx, ry, xc, yc)
    
    
    rotated_ellipse = [tf.rotate2D(x, y, angle, xc, yc) for x, y in ellipse_points]
    

    py5.stroke(0)  
    for x, y in rotated_ellipse:
        py5.point(x, y)

    
    angle += 2  


py5.run_sketch()
