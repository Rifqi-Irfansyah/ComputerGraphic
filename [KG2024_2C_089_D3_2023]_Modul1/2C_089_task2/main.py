import py5
import primitif.line
import primitif.basic

import math

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER) 
    py5.background(191)

def draw():
    primitif.basic.draw_margin(py5.width, py5.height, 25, c=[0,0,0,255])
    primitif.basic.draw_kartesian(py5.width, py5.height, 25, c=[0,0,0,255])
    #RIFQI IRFANSYAH (231511089)
    
    py5.fill(255, 255, 0)
    py5.no_stroke()
    py5.rect(py5.width/4 - 70, py5.height/2 + 125, 45, 15, 7)
    py5.rect(py5.width/4 + 70, py5.height/2 + 125, 45, 15, 7)
   
    py5.fill(255, 255, 0)    
    py5.ellipse(py5.width/4, py5.height/2 + 70, 115, 105)
    py5.square(py5.width/4, py5.height/2 + 120, 115)
    
    py5.fill(0, 0, 0)
    py5.rect(py5.width/4, py5.height/2 + 70, 116, 20, 7)
    
    py5.fill(0,0,0)
    py5.circle(py5.width/4 - 26, py5.height/2 + 70, 45)
    py5.circle(py5.width/4 + 26, py5.height/2 + 70, 45)
    py5.fill(255, 255, 255)
    py5.circle(py5.width/4 - 26, py5.height/2 + 70, 30)
    py5.circle(py5.width/4 + 26, py5.height/2 + 70, 30)
    py5.fill(0,0,0)
    py5.ellipse(py5.width/4 - 26, py5.height/2 + 70, 10, 13)
    py5.ellipse(py5.width/4 + 26, py5.height/2 + 70, 10, 13)
    py5.arc(py5.width/4, py5.height/2 + 100, 50, 50, 0, py5.PI)
    
    py5.fill(255, 255, 0)
    py5.rect(py5.width/4 - 28, py5.height/2 + 225, 15, 50, 7)
    py5.rect(py5.width/4 + 28, py5.height/2 + 225, 15, 50, 7)
    py5.fill(0, 0, 0)
    py5.rect(py5.width/4 - 28, py5.height/2 + 255, 25, 20, 50,50,7,7)
    py5.rect(py5.width/4 + 28, py5.height/2 + 255, 25, 20, 50,50,7,7)
    
    py5.fill(0, 102, 204)
    py5.rect(py5.width/4, py5.height/2 + 140, 116, 16, 7)    
    py5.rect(py5.width/4, py5.height/2 + 160, 75, 55, 115, 115, 55, 55)
    py5.rect(py5.width/4, py5.height/2 + 180, 115, 45, 15, 15, 55, 55)
    #END OF RIFQI IRFANSYAH
    
    
    #DIO
    py5.fill(255, 239, 0)
    py5.circle(590, 440, 200)
    
    py5.fill(0, 0, 0)
    py5.rect(540, 370, 50, 15, 7)
    py5.rect(640, 370, 50, 15, 7)

    
    py5.fill(255, 255, 255)
    py5.circle(555, 420, 60)
    py5.circle(630, 420, 60)
    
    py5.fill(100, 20, 10)
    py5.circle(555, 420, 30)
    py5.circle(630, 420, 30)
    
    py5.fill(255, 255, 255)
    py5.rect(590, 500, 25, 55, 7)
    
    py5.fill(255, 25, 25)
    py5.rect(590, 500, 25, 25, 7)
    
    
    
    
    #AFRIZA
    py5.stroke(1)
    py5.fill(238,210,0)
    py5.circle(570, 230, 100)
    py5.line(540, 185, 490, 130)
    py5.line(570, 175, 570, 120)
    py5.line(600, 185, 650, 130)
    
    
    py5.fill(154,252,0)
    py5.triangle(400, 300, 500, 200, 600, 300)
    py5.fill(154,252,0)
    py5.triangle(520, 300, 680, 150, 775, 300)
    
    py5.fill(161,200,240)
    py5.circle(730, 82, 80)
    py5.circle(700, 82, 80)
    py5.circle(670, 82, 80)
    
    
    # Muhammad Wildan Gumilang (231511087)
    # GAMBAR PELANGI DENGAN LINGKARAN BERTUMPUK
    margin = 25
    width = py5.width
    height = py5.height
    # WARNA BAYANGAN
    py5.fill(50, 50, 50, 100)
    py5.ellipse((width / 4) + margin / 2 + 10, (height / 4) + margin / 2 + 10, 250, 250)
    
    py5.fill(255, 0, 0)
    py5.ellipse((width / 4) + margin / 2, (height / 4) + margin / 2, 250, 250)
    py5.fill(255, 165, 0)
    py5.ellipse((width / 4) + margin / 2, (height / 4) + margin / 2, 200, 200)
    py5.fill(255, 255, 0)
    py5.ellipse((width / 4) + margin / 2, (height / 4) + margin / 2, 150, 150)
    py5.fill(0, 255, 0)
    py5.ellipse((width / 4) + margin / 2, (height / 4) + margin / 2, 100, 100)
    
    # GAMBAR TITIK HITAM
    py5.fill(0) 
    py5.ellipse((width / 4) + margin / 2, (height / 4) + margin / 2, 10, 10)
    
    # GAMBAR PANAH
    py5.line(width / 2, height / 2, (width / 4) + margin / 2, (height / 4) + margin / 2)
    
py5.run_sketch()
