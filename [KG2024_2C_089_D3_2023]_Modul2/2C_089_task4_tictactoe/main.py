import py5
import primitif.line
import primitif.basic

import math

margin = 25

def setup():
    py5.size(550, 550)
    py5.rect_mode(py5.CENTER) 
    py5.background(191)

def draw():
    py5.stroke_weight(5)
    primitif.basic.draw_margin(py5.width, py5.height, margin, c=[0,0,0,255])
    primitif.basic.draw_kartesian(py5.width, py5.height, margin, c=[0,0,0,255])
    

    width_6 = (py5.width-2*margin)/6
    position1 = margin + width_6
    position2 = margin + width_6 * 3
    position3 = margin + width_6 * 5
    
    py5.stroke_weight(15)
    
    py5.stroke(0, 0, 255)
    primitif.basic.draw_o(position3, position3, 80)
    primitif.basic.draw_o(position1, position2, 80)
    primitif.basic.draw_o(position2, position1, 80)
    primitif.basic.draw_o(position1, position3, 80)
    
    py5.stroke(255, 0, 0)
    primitif.basic.draw_x(position1, position1, 80)
    primitif.basic.draw_x(position2, position2, 80)
    primitif.basic.draw_x(position2, position3, 80)
    primitif.basic.draw_x(position3, position1, 80)
    primitif.basic.draw_x(position3, position2, 80)
    
    
    
py5.run_sketch()

