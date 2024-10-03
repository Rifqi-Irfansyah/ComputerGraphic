import numpy as np
import py5
import math
import primitif.transformasiv2 as tf
import primitif.basic as basic
import primitif.line as line
import config

rx, ry = 50, 30
angle_dinamis = 0
margin = 20
y=1
gerak = 1

class Ironman:
    def __init__(self, xc, yc):
        self.xc = xc
        self.yc = yc
        
    def gambar_kepala(self):
        updatey()

        # OUTER
        buat_lingkaran(self.xc + 18.8,self.yc + 11.9, 91.5, 0, 27)        # PELIPIS KIRI
        buat_lingkaran(self.xc + 18.8,self.yc + 11.9, 91.5, 340, 360)
        buat_lingkaran(self.xc -18.8,self.yc + 11.9, 91.5, 180-27, 220)   # PELIPIS KANAN
        buat_lingkaran(self.xc + 0,self.yc -7.1, 91.5, 235, 294)          # KEPALA
        buat_lingkaran(self.xc + 0.37,self.yc + 14, 72, 300, 340)         # DAGU
        buat_lingkaran(self.xc + 0,self.yc + 20, 80, 38, 142)

        # TOPENG
        buat_lingkaran(self.xc + 30,self.yc + 11.9, 91.5, 0, 25)
        buat_lingkaran(self.xc + 30,self.yc + 11.9, 91.5, 330, 360)
        buat_lingkaran(self.xc -30,self.yc + 11.9, 91.5, 180-25, 210)
        buat_lingkaran(self.xc + 0,self.yc -20, 91.5, 235, 250)         # HORIZONTAL I
        buat_lingkaran(self.xc + 0,self.yc -20, 91.5, 290, 305)         # HORIZONTAL I
        buat_lingkaran(self.xc + 0,self.yc -43, 91.5, 255, 284)         # HORIZONTAL II
        buat_lingkaran(self.xc + 0,self.yc -60, 91.5, 259, 280)         # HORIZONTAL III
        buat_ellipse(self.xc - 87,self.yc -20, 80, 123.5, 210, 232)     # VERTIKAL II
        buat_ellipse(self.xc + 87,self.yc -20, 80, 123.5, 308, 330)
        buat_ellipse(self.xc -30,self.yc + 40, 122, 89, 130, 139)       # HORIZONTAL IV
        buat_ellipse(self.xc + 30,self.yc + 40, 122, 89, 39, 48)        # HORIZONTAL IV
        buat_ellipse(self.xc -75,self.yc + 0, 122, 89, 145, 159)        # VERTIKAL III
        buat_ellipse(self.xc + 75,self.yc + 0, 122, 89, 19, 35)         # VERTIKAL III

        # WAJAH
        basic.trapesium_tanpa_alas(self.xc + 0,self.yc -53, 25, 35, 10) # MULUT
        buat_ellipse(self.xc + 0,self.yc + 60, 101, 62, 49, 180-49)     # ALIS
        buat_lingkaran(self.xc + 48,self.yc + 0, 10, 90, 220)           # MATA KANAN
        buat_ellipse(self.xc + 40,self.yc -3, 23, 7, 0, 120)            
        buat_ellipse(self.xc + 40,self.yc -3, 23, 7, 340, 360)            
        buat_lingkaran(self.xc - 48,self.yc + 0, 10, 300, 360)          # MATA KIRI
        buat_lingkaran(self.xc - 48,self.yc + 0, 10, 0, 90)
        buat_ellipse(self.xc - 40,self.yc -3, 23, 7, 55, 190)            
        buat_ellipse(self.xc - 65,self.yc + 4, 24, 25, 60, 80)          #TELINGA KIRI BAWAH           
        buat_ellipse(self.xc - 65,self.yc + 4, 24, 25, 288, 310)        #ATAS
        buat_ellipse(self.xc - 75,self.yc + 10, 8, 19, 0, 20)           #TENGAH 
        buat_ellipse(self.xc - 75,self.yc + 10, 8, 19, 313, 360)             
        buat_ellipse(self.xc - 75,self.yc , 8, 19, 0, 80)                              
        buat_ellipse(self.xc - 75,self.yc , 8, 19, 330, 360)                

        buat_ellipse(self.xc + 65,self.yc + 4, 24, 25, 90, 110)         #TELINGA KANAN BAWAH
        buat_ellipse(self.xc + 65,self.yc + 4, 24, 25, 231, 253)        #ATAS
        buat_ellipse(self.xc + 75,self.yc + 10, 8, 19, 145, 236)        #TENGAH 
        buat_ellipse(self.xc + 75,self.yc, 8, 19, 80, 185)
        self.baju()
        self.celana()             
        self.sepatu()
        self.tangan_kiri()
        self.tangan_kanan()
    
    def baju(self):
        basic.trapesium_tanpa_alas(self.xc + 0,self.yc -83, 50, 75, 50)
        buat_ellipse(self.xc ,self.yc-92, 80, 19, 48, 180-49)             
        buat_lingkaran(self.xc ,self.yc-80, 10, 0, 360)
        buat_lingkaran(self.xc ,self.yc-80, 20, 30, 150)
        buat_lingkaran(self.xc-35 ,self.yc-100, 20, 210, 255)
        buat_lingkaran(self.xc-35 ,self.yc-112, 20, 228, 258)
        buat_lingkaran(self.xc+35 ,self.yc-100, 20, 285, 320)
        buat_lingkaran(self.xc+35 ,self.yc-112, 20, 278, 320)   
        py5.points(line.line_bresenham(self.xc + 12 , self.yc - 97, self.xc + 12, self.yc - 110))
        py5.points(line.line_bresenham(self.xc - 12 , self.yc - 97, self.xc - 12, self.yc - 110))
        buat_lingkaran(self.xc ,self.yc-87, 20, 50, 126)
        buat_lingkaran(self.xc ,self.yc-107, 12, 20, 159)
    
    def celana(self):
        py5.points(line.line_bresenham(self.xc + 38 , self.yc - 110, self.xc + 36, self.yc - 150))
        py5.points(line.line_bresenham(self.xc + 6 , self.yc - 130, self.xc + 8, self.yc - 150))
        py5.points(line.line_bresenham(self.xc - 38 , self.yc - 110, self.xc - 36, self.yc - 150))
        py5.points(line.line_bresenham(self.xc - 6 , self.yc - 130, self.xc - 8, self.yc - 150))
        buat_lingkaran(self.xc ,self.yc-130, 5, 180, 360)
        buat_lingkaran(self.xc-30, self.yc-162, 40, 230, 280)
        buat_lingkaran(self.xc+30, self.yc-162, 40, 258, 308)
        buat_lingkaran(self.xc-22, self.yc-140, 5, 0, 360)
        buat_lingkaran(self.xc+22, self.yc-140, 5, 0, 360)

    def sepatu(self):
        buat_ellipse(self.xc-22 ,self.yc-153, 15, 6, 0, 190)  
        buat_ellipse(self.xc-22 ,self.yc-153, 15, 6, 340, 360)  
        buat_ellipse(self.xc-22 ,self.yc-148, 15, 6, 0, 180)  
        buat_ellipse(self.xc+22 ,self.yc-153, 15, 6, 0, 190)  
        buat_ellipse(self.xc+22 ,self.yc-153, 15, 6, 340, 360)
        buat_ellipse(self.xc+22 ,self.yc-148, 15, 6, 0, 180)  

    def tangan_kiri(self):
        buat_lingkaran(self.xc-35 ,self.yc-63, 8, 110, 250)
        buat_ellipse(self.xc-70 ,self.yc-63, 50, 9, 55, 157)  
        buat_ellipse(self.xc-70 ,self.yc-61, 50, 9, 205, 305)  
        buat_lingkaran(self.xc-85 ,self.yc-62, 10, 0, 90)
        buat_lingkaran(self.xc-85 ,self.yc-62, 10, 270, 360)
        buat_lingkaran(self.xc-77 ,self.yc-62, 10, 0, 90)
        buat_lingkaran(self.xc-77 ,self.yc-62, 10, 270, 360)

        buat_lingkaran(self.xc-40 ,self.yc-62, 15, 313, 360)
        buat_lingkaran(self.xc-40 ,self.yc-62, 15, 313, 360)
        buat_lingkaran(self.xc-30 ,self.yc-62, 15, 313, 360)
        buat_lingkaran(self.xc-30 ,self.yc-62, 15, 313, 360)

        buat_lingkaran(self.xc-40 ,self.yc-62, 15, 0, 38)
        buat_lingkaran(self.xc-30 ,self.yc-62, 15, 0, 38)

    def tangan_kanan(self):
        buat_lingkaran(self.xc+35 ,self.yc-63, 8, 110, 250)
        buat_ellipse(self.xc+70 ,self.yc-63, 50, 9, 55, 157)  
        buat_ellipse(self.xc+70 ,self.yc-61, 50, 9, 205, 305)  
        buat_lingkaran(self.xc+85 ,self.yc-62, 10, 0, 90)
        buat_lingkaran(self.xc+85 ,self.yc-62, 10, 270, 360)
        buat_lingkaran(self.xc+77 ,self.yc-62, 10, 0, 90)
        buat_lingkaran(self.xc+77 ,self.yc-62, 10, 270, 360)

        buat_lingkaran(self.xc+40 ,self.yc-62, 15, 313, 360)
        buat_lingkaran(self.xc+40 ,self.yc-62, 15, 313, 360)
        buat_lingkaran(self.xc+30 ,self.yc-62, 15, 313, 360)
        buat_lingkaran(self.xc+30 ,self.yc-62, 15, 313, 360)

        buat_lingkaran(self.xc+40 ,self.yc-62, 15, 0, 38)
        buat_lingkaran(self.xc+30 ,self.yc-62, 15, 0, 38)

def updatey():
    global y
    y += 0.25
    if(y == 360):
        y = 0


class Gunungan:
    def __init__(self, xc, yc,):
        self.xc = xc
        self.yc = yc
    
    def gambar_gunungan(self):
        updatey()
        basic.segitiga_tanpa_alas(self.xc + 0,self.yc -53, 100,100)
        buat_lingkaran(self.xc + 25,self.yc-110 + 0, 25, 125, 192)      #LEKUKAN ATAS KANAN
        buat_lingkaran(self.xc - 25,self.yc-110 + 0, 25, 345, 360)      #KIRI
        buat_lingkaran(self.xc - 25,self.yc-110 + 0, 25, 0, 48)

        buat_lingkaran(self.xc + 55,self.yc-142 + 0, 20, 0, 35)         #LEKUKAN BAWAH KANAN
        buat_lingkaran(self.xc + 55,self.yc-142 + 0, 20, 322, 360) 
        buat_lingkaran(self.xc - 55,self.yc-142 + 0, 20, 142, 215)      #KIRI
        py5.points(line.line_bresenham(self.xc + 160 - 200, self.yc - 155, self.xc + 40, self.yc - 155))
        py5.points(line.line_bresenham(self.xc + 204 - 200, self.yc - 155, self.xc + 4, self.yc - 200))
        py5.points(line.line_bresenham(self.xc + 196 - 200, self.yc - 155, self.xc - 4, self.yc - 200))
        buat_lingkaran(self.xc ,self.yc-200 + 0, 4, 0, 180)
        self.gambar_motif()

    def gambar_motif(self):
        py5.points(line.line_bresenham(self.xc, self.yc-4, self.xc, self.yc - 155))
        buat_lingkaran(self.xc - 10,self.yc-42, 7, 0, 55)              #KIRI
        buat_lingkaran(self.xc - 10,self.yc-42, 7, 210, 360)
        buat_lingkaran(self.xc - 7,self.yc-40, 3, 0, 160)
        buat_lingkaran(self.xc + 10,self.yc-42, 7, 90, 330)            #KANAN
        buat_lingkaran(self.xc + 7,self.yc-40, 3, 330, 360)
        buat_lingkaran(self.xc + 7,self.yc-40, 3, 0, 120)

        buat_lingkaran(self.xc - 5,self.yc-27, 5, 180, 360)            #KIRI
        buat_lingkaran(self.xc - 6,self.yc-27, 3, 0, 200)
        buat_lingkaran(self.xc + 5,self.yc-27, 5, 180, 360)            #KANAN
        buat_lingkaran(self.xc + 6,self.yc-27, 3, 0, 180)
        buat_lingkaran(self.xc + 6,self.yc-27, 3, 330, 360)

        buat_lingkaran(self.xc - 11,self.yc-60, 10, 180, 315)           #KIRI
        buat_lingkaran(self.xc - 13,self.yc-58, 7, 270, 360)               
        buat_lingkaran(self.xc - 13,self.yc-58, 7, 0, 120)               
        buat_lingkaran(self.xc - 10,self.yc-61, 3, 90, 270)
        buat_lingkaran(self.xc + 11,self.yc-60, 10, 225, 360)           #KANAN
        buat_lingkaran(self.xc + 13,self.yc-58, 7, 30, 210)               
        buat_lingkaran(self.xc + 10,self.yc-61, 3, 0, 90)               
        buat_lingkaran(self.xc + 10,self.yc-61, 3, 270, 360)

        buat_lingkaran(self.xc - 20,self.yc-70, 7, 0, 230)              #KIRI
        buat_lingkaran(self.xc - 20,self.yc-70, 7, 330, 360)
        buat_lingkaran(self.xc - 23,self.yc-70, 4, 270, 360)
        buat_lingkaran(self.xc + 20,self.yc-70, 7, 310, 360)            #KANAN
        buat_lingkaran(self.xc + 20,self.yc-70, 7, 0, 160)
        buat_lingkaran(self.xc + 23,self.yc-70, 4, 180, 270)

        buat_lingkaran(self.xc - 10,self.yc-85, 7, 200, 360)            #KIRI
        buat_lingkaran(self.xc - 10,self.yc-85, 7, 0, 22)
        buat_lingkaran(self.xc - 6,self.yc-84, 3, 0, 190)
        buat_lingkaran(self.xc + 10,self.yc-85, 7, 128, 340)            #KIRI
        buat_lingkaran(self.xc + 6,self.yc-84, 3, 0, 180)
        buat_lingkaran(self.xc + 6,self.yc-84, 3, 350, 360)

        buat_lingkaran(self.xc - 39,self.yc-92 , 6, 0, 130)             #KIRI
        buat_lingkaran(self.xc + 39,self.yc-92 , 6, 50, 180)             #KANAN

        buat_lingkaran(self.xc - 20,self.yc-110 , 20, 180, 315)         #KIRI
        buat_lingkaran(self.xc - 26,self.yc-102 , 10, 270, 360)               
        buat_lingkaran(self.xc - 26,self.yc-102 , 10, 0, 120)               
        buat_lingkaran(self.xc - 22,self.yc-106 , 5, 90, 270)               
        buat_lingkaran(self.xc - 20,self.yc-115 , 5, 70, 230)                       
        buat_lingkaran(self.xc + 20,self.yc-110 , 20, 225, 360)         #KANAN
        buat_lingkaran(self.xc + 26,self.yc-102 , 10, 30, 210)
        buat_lingkaran(self.xc + 22,self.yc-106 , 5, 270, 360)                       
        buat_lingkaran(self.xc + 22,self.yc-106 , 5, 0, 40)                       
        buat_lingkaran(self.xc + 20,self.yc-115 , 5, 0, 110)                       
        buat_lingkaran(self.xc + 20,self.yc-115 , 5, 270, 360) 

        buat_lingkaran(self.xc - 100,self.yc-100 , 100, 162, 180)      #KIRI
        buat_lingkaran(self.xc - 10,self.yc-125 , 7, 30, 180)
        buat_lingkaran(self.xc - 13,self.yc-128 , 3, 180, 360)
        buat_lingkaran(self.xc + 100,self.yc-100 , 100, 0, 18)         #KANAN
        buat_lingkaran(self.xc + 10,self.yc-125 , 7, 0, 150)
        buat_lingkaran(self.xc + 13,self.yc-128 , 3, 180, 360)

        buat_lingkaran(self.xc + 22,self.yc-102 , 25, 70, 190)      #KIRI
        buat_lingkaran(self.xc - 22,self.yc-102 , 25, 0, 110)       #KANAN
        buat_lingkaran(self.xc - 22,self.yc-102 , 25, 350, 360)
        buat_lingkaran(self.xc + 18,self.yc-105 , 30, 110, 180)     #KIRI
        buat_lingkaran(self.xc + 30,self.yc-158 , 25, 274, 325)
        buat_lingkaran(self.xc - 18,self.yc-105 , 30, 0, 70)        #KANAN
        buat_lingkaran(self.xc - 30,self.yc-158 , 25, 215, 274)
        buat_lingkaran(self.xc - 26,self.yc-115 , 30, 68, 118)     #KIRI
        buat_lingkaran(self.xc + 26,self.yc-115 , 30, 58, 108)     #KANAN


        basic.persegi_panjang(self.xc, self.yc-138, 20, 10)
        py5.points(line.line_bresenham(self.xc - 30, self.yc-154, self.xc - 10, self.yc - 143)) # HORIZONTAL
        py5.points(line.line_bresenham(self.xc - 15, self.yc-154, self.xc - 3, self.yc - 143))
        py5.points(line.line_bresenham(self.xc + 30, self.yc-154, self.xc + 10, self.yc - 143))
        py5.points(line.line_bresenham(self.xc + 15, self.yc-154, self.xc + 3, self.yc - 143))
        py5.points(line.line_bresenham(self.xc - 17, self.yc-147, self.xc + 17, self.yc - 147))  #VERTIKAL
        py5.points(line.line_bresenham(self.xc - 23, self.yc-151, self.xc + 23, self.yc - 151))  #VERTIKAL
        


def buat_lingkaran(xc, yc, radius, start, end):
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
    
def buat_ellipse(xc, yc, Rx, Ry, start, end):
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

def setup():
    py5.size(config.WIDTH, config.HEIGHT)

def gerakin():
    global gerak
    gerak += 1

def draw():
    global angle, xc, yc, y, gerak
    py5.background(255)
    basic.draw_margin(py5.width, py5.height, margin, c=[0,0,0,255])
    basic.draw_kartesian(py5.width, py5.height, margin, c=[0,0,0,255])
    py5.fill(000)
    py5.text(y, py5.width/3,py5.height/2)
    # gerakin()

    
    py5.translate(config.WIDTH /2, config.HEIGHT / 2)
    py5.scale(1, -1)
    
    obj_ironman = Ironman(gerak,gerak)
    obj_ironman.gambar_kepala()
    
    obj_gunungan = Gunungan(-config.WIDTH/4,-50)
    obj_gunungan.gambar_gunungan()

    obj_gunungan = Gunungan(config.WIDTH/4,-50)
    obj_gunungan.gambar_gunungan()

py5.run_sketch()
