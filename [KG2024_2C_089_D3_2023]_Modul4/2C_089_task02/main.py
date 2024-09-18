import numpy as np
import py5
import math
import primitif.transformasiv2 as tf
import primitif.basic as basic
import config

class Bunga:
    points = 0
    def __init__(self, xc, yc, radius_lingkaran, jumlah_kelopak, color, pattern):
        self.xc = xc
        self.yc = yc
        self.radius_lingkaran = radius_lingkaran
        self.jumlah_kelopak = jumlah_kelopak
        self.pattern = pattern
        self.color = color

    def lingkaran_tengah(self, radius):
        circle_points = basic.draw_circle(radius, self.xc, self.yc, self.pattern)
        #DRAW
        for x, y in circle_points:
            py5.point(x  , y )


    def kelopak_bunga(self, Rx, Ry):
        ellipse_points = basic.draw_patterned_ellipse(Rx, Ry, self.xc, self.yc, self.pattern)
        
        anchor_radius = min(Rx, Ry) + self.radius_lingkaran# Adjust as needed
        angle_step = 360 / self.jumlah_kelopak
        angle = 0
        while angle <= 360:
            # ROTATE
            rotated_ellipse = [tf.rotate2D(x, y, angle, self.xc, self.yc) for x, y in ellipse_points]    
            
            # DRAW
            for x, y in rotated_ellipse:
                py5.point(x + anchor_radius * np.cos(np.deg2rad(angle)) , y + anchor_radius * np.sin(np.deg2rad(angle)))
            
            angle += angle_step
    
    
    def gambar_bunga(self, name_animate="solid"):
        points = 0
        py5.stroke(*self.color)
        
        i = 0
        while i <= 5:
            self.lingkaran_tengah(self.radius_lingkaran + i)
            self.kelopak_bunga(self.radius_lingkaran * 2 + i, self.radius_lingkaran + i)
            i += 0.2


rx, ry = 50, 30
xc, yc = 200, 200
angle = 0
margin = 20

def setup():
    py5.size(config.WIDTH, config.HEIGHT)
    py5.frame_rate(30) 

def draw():
    global angle
    py5.background(255)
    basic.draw_margin(py5.width, py5.height, margin, c=[0,0,0,255])
    basic.draw_kartesian(py5.width, py5.height, margin, c=[0,0,0,255])
    
    py5.translate(config.WIDTH /2, config.HEIGHT / 2)
    py5.scale(1, -1)
    
    xc = (config.WIDTH-margin)/4 -margin/2
    yc = (config.HEIGHT-margin)/4 -margin/2
    
    bunga1 = Bunga(xc, yc, 30, 4, config.GREEN, "solid")
    bunga1.gambar_bunga("skala")
    
    bunga2 = Bunga(-xc, yc, 30, 5, config.PURPLE, "dash_dash")
    bunga2.gambar_bunga("skala")
    
    bunga3 = Bunga(xc, -yc, 30, 7, config.MAGENTA, "dot")
    bunga3.gambar_bunga("skala")
    
    bunga4 = Bunga(-xc, -yc, 30, 8, config.BLUE, "dash_dot")
    bunga4.gambar_bunga("skala")


py5.run_sketch()

