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
            
    def satu_kelopak(self, Rx, Ry):
        ellipse_points = basic.draw_patterned_ellipse(Rx, Ry, self.xc, self.yc, self.pattern)
        return ellipse_points


    def kelopak_bunga(self, Rx, Ry):
        ellipse_points = basic.draw_patterned_ellipse(Rx, Ry, self.xc, self.yc, self.pattern)
        
        anchor_radius = min(Rx, Ry) + self.radius_lingkaran# Adjust as needed
        angle_step = 360 / self.jumlah_kelopak
        
        angle = 0 + angle_dinamis
        for i in range (self.jumlah_kelopak):
            # ROTATE
            rotated_ellipse = [tf.rotate2D(x, y, angle, self.xc, self.yc) for x, y in ellipse_points]    
            
            # DRAW
            for x, y in rotated_ellipse:
                py5.point(x + anchor_radius * np.cos(np.deg2rad(angle)) , y + anchor_radius * np.sin(np.deg2rad(angle)))
            
            angle += angle_step
            angle = angle % 360
    
    def gambar_bunga(self):
        points = 0
        py5.stroke(*self.color)
        
        i = 0
        while i <= 0.6:
            self.lingkaran_tengah(self.radius_lingkaran + i)
            self.kelopak_bunga(self.radius_lingkaran * 2 + i, self.radius_lingkaran + i)
            i += 0.2
            
#     def gambar_bunga_transform(self, type_transformasi = "rotate"):
#         if (type_transformasi == "rotate"):
#             
#             Rx = self.radius_lingkaran * 2
#             Ry = self.radius_lingkaran
#             
#             i = 0
#             while i <= 5:
#                 self.lingkaran_tengah(self.radius_lingkaran + i)
#                 
#                 anchor_radius = min(Rx, Ry) + self.radius_lingkaran# Adjust as needed
#                 ellipse_points = basic.draw_patterned_ellipse(Rx, Ry, self.xc, self.yc, self.pattern)
#         
#                 # ROTATE
#                 rotated_ellipse = [tf.rotate2D(x, y, angle_dinamis, self.xc, self.yc) for x, y in ellipse_points]    
#                 
#                 # DRAW
#                 for x, y in rotated_ellipse:
#                     py5.point(x + anchor_radius * np.cos(np.deg2rad(angle_dinamis)) , y + anchor_radius * np.sin(np.deg2rad(angle_dinamis)))
#                 
#                 i += 0.2
                

rx, ry = 50, 30
xc, yc = 200, 200
angle_dinamis = 0
margin = 20

def updateTime():
    global angle_dinamis

    if(angle_dinamis <= 360):
        angle_dinamis += 5
    else:
        angle_dinamis = 0

def setup():
    py5.size(config.WIDTH, config.HEIGHT)

def draw():
    global angle
    py5.background(255)
    basic.draw_margin(py5.width, py5.height, margin, c=[0,0,0,255])
    basic.draw_kartesian(py5.width, py5.height, margin, c=[0,0,0,255])
    
    updateTime()
    
    py5.translate(config.WIDTH /2, config.HEIGHT / 2)
    py5.scale(1, -1)
    
    xc = (config.WIDTH-margin)/4 -margin/2
    yc = (config.HEIGHT-margin)/4 -margin/2
    
    bunga1 = Bunga(xc, yc, 30, 4, config.GREEN, "solid")
    bunga1.gambar_bunga()
    
    bunga1 = Bunga(-xc, yc, 30, 5, config.PURPLE, "dash_dash")
    bunga1.gambar_bunga()
    
    bunga1 = Bunga(xc, -yc, 30, 7, config.MAGENTA, "dot")
    bunga1.gambar_bunga()
    
    bunga1 = Bunga(-xc, -yc, 30, 8, config.BLUE, "dash_dot")
    bunga1.gambar_bunga()


py5.run_sketch()

