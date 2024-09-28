import numpy as np
import py5
import math
import primitif.transformasiv2 as tf
import primitif.basic as basic
import config

rx, ry = 50, 30
xc, yc = 0,0
angle_dinamis = 0
margin = 20
y=1

class Ironman:
    def __init__(self, xc, yc):
        self.xc = xc
        self.yc = yc
        
    def buat_lingkaran(self, xc, yc, radius, start, end):
        circle_points = basic.draw_circle(radius, xc, yc, "solid")
        num_points = len(circle_points)/360
        #DRAW
        i = 0
        for x, y in circle_points:
            i += 1
            if(i >= num_points*start) and (i<= num_points*end):
                py5.point(x  , y )
            elif(i > num_points*end):
                py5.point(x  , y )
                break
    
    def buat_ellipse(self, xc, yc, Rx, Ry, start, end):
        ellipse_points = basic.draw_patterned_ellipse(Rx, Ry, xc, yc, "solid")
        num_points = len(ellipse_points)/360
        #DRAW
        i = 0
        for x, y in ellipse_points:
            i += 1
            if(i >= num_points*start) and (i<= num_points*end):
                py5.point(x  , y )
            elif(i > num_points*end):
                py5.point(x  , y )
                break
            
    def gambar_kepala(self):
        self.updatey()
        #PELIPIS KIRI KANAN
        self.buat_lingkaran(18.8, 11.9, 91.5, 0, 27)
        self.buat_lingkaran(18.8, 11.9, 91.5, 340, 360)
        self.buat_lingkaran(-18.8, 11.9, 91.5, 180-27, 220)
        #KEPALA
        self.buat_lingkaran(0, -7.1, 91.5, 235, 294)
        self.buat_lingkaran(0.37, 14, 72, 300, 340)
        #DAGU
        self.buat_lingkaran(0, 20, 80, 38, 142)

        #TOPENG
        self.buat_lingkaran(30, 11.9, 91.5, 0, 25)
        self.buat_lingkaran(30, 11.9, 91.5, 330, 360)
        self.buat_lingkaran(-30, 11.9, 91.5, 180-25, 210)
        self.buat_lingkaran(0, -20, 91.5, 235, 250)         # HORIZONTAL I
        self.buat_lingkaran(0, -20, 91.5, 290, 305)         # HORIZONTAL I
        self.buat_lingkaran(0, -30, 91.5, 253, 287) 
        self.buat_lingkaran(0, -45, 91.5, 255, 283)         # HORIZONTAL II
        self.buat_ellipse(-87,-20, 80, 123.5, 220, 232)     # VERTIKAL II
        self.buat_ellipse(87,-20, 80, 123.5, 308, 320)
        self.buat_ellipse(-30, 40, 122, 89, 130, 139)       # HORIZONTAL III
        self.buat_ellipse(30, 40, 122, 89, 39, 48)          # HORIZONTAL III
        self.buat_ellipse(-75, 0, 122, 89, 145, 159)        # VERTIKAL III
        self.buat_ellipse(75, 0, 122, 89, 19, 35)           # VERTIKAL III

        #WAJAH
        basic.trapesium_tanpa_alas(0,-50, 20, 35, 15)       # MULUT
        self.buat_ellipse(0, 70, 101, 62, 49, 180-49)       # ALIS
        self.buat_lingkaran(48, 10, 10, 90, 220)            # MATA KANAN
        self.buat_lingkaran(-48, 10, 10, 300, 360)           # MATA KIRI
        self.buat_lingkaran(-48, 10, 10, 0, 90)            


    
    def updatey(self):
        global y
        y += 0.25
        if(y == 360):
            y = 0

 

def setup():
    py5.size(config.WIDTH, config.HEIGHT)

def draw():
    global angle, xc, yc, y
    py5.background(255)
    basic.draw_margin(py5.width, py5.height, margin, c=[0,0,0,255])
    basic.draw_kartesian(py5.width, py5.height, margin, c=[0,0,0,255])
    py5.fill(000)
    py5.text(y, py5.width/2,py5.height/2)

    
    py5.translate(config.WIDTH /2, config.HEIGHT / 2)
    py5.scale(1, -1)
    
    obj_ironman = Ironman(0,0)
    obj_ironman.gambar_kepala()
    

py5.run_sketch()
