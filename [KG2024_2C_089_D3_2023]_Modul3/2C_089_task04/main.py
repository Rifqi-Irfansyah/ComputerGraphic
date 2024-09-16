import py5
import primitif.line
import primitif.basic
import primitif.utility
import math
import config

margin = 25

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.background(191)
    primitif.basic.draw_margin(py5.width, py5.height, margin, c=[0,0,0,255])
    primitif.basic.draw_kartesian(py5.width, py5.height, margin, c=[0,0,0,255])
    
    
    width_2 = (py5.width-2*margin)/4
    height_2 = (py5.height-2*margin)/4
    positionX = margin + width_2
    positionY = margin + height_2
    
    if config.anim <= config.times:
        y = 1
        for i in range(0, 4, 2):
            for x in range(0, 4, 2):
                primitif.basic.persegi(positionX + i*width_2, positionY + x*height_2, 120, y, c=[0,0,0,255])
                y = y+1
                
    elif config.anim <= 2*config.times:
        y = 1
        for i in range(0, 4, 2):
            for x in range(0, 4, 2):
                primitif.basic.persegi_panjang(positionX + i*width_2, positionY + x*height_2, 200, 75, y, c=[0,0,0,255])
                y = y+1
                
    elif config.anim <= 3*config.times:
        y = 1
        for i in range(0, 4, 2):
            for x in range(0, 4, 2):
                primitif.basic.segitiga_siku(positionX + i*width_2, positionY + x*height_2, 180, 100, y, c=[0,0,0,255])
                y = y+1

    elif config.anim <= 4*config.times:
        y = 1
        for i in range(0, 4, 2):
            for x in range(0, 4, 2):
                primitif.basic.trapesium_siku(positionX + i*width_2, positionY + x*height_2, 100, 180, 100, y, c=[0,0,0,255])
                y = y+1
    
    if config.anim > 4*config.times:
        config.anim = 0
        
    config.anim += 1
    

py5.run_sketch()
