import py5
import math
import config

def draw_line(x1, y1, x2, y2, weight, color):
    py5.stroke(*color)
    py5.stroke_weight(weight)
    py5.line(x1, y1, x2, y2)

def draw_ticks(x, y, radius, color):
    py5.stroke(*color)  
    tick_length = 10
        
    py5.fill(*config.BLACK)
    py5.text_size(20)
    py5.text("3", x+config.CLOCK_RADIUS-15,y)
    py5.text("6", x,y+config.CLOCK_RADIUS-15)
    py5.text("9", x-config.CLOCK_RADIUS+15,y)
    py5.text("12", x,y-config.CLOCK_RADIUS+15)

    py5.stroke_weight(5)  
    for hour in range(12):
        angle = math.radians(hour * 30 - 90) 
        dot_x = x + (radius - 15) * math.cos(angle)
        dot_y = y + (radius - 15) * math.sin(angle)
        py5.point(dot_x, dot_y)