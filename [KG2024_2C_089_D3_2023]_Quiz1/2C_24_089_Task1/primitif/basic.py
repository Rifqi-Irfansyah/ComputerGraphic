import py5
import numpy as np

def draw_circle(x, y, radius, color, style=None):
    py5.stroke_weight(2)

    if style == 'solid':
        solid_circle(x, y, radius)
    elif style == 'dotted':
        dotted_circle(x, y, radius)
    elif style == 'dotted_striped':
        dotted_striped_circle(x, y, radius)
    elif style == 'dashed':
        dashed_circle(x, y, radius)
    else:
        print("Maaf, style tidak ada")
        
def circlePlotPoints(xc, yc, x, y):
    res = [
        [xc + x, yc + y],
        [xc - x, yc + y],
        [xc + x, yc - y],
        [xc - x, yc - y],
        [xc + y, yc + x],
        [xc - y, yc + x],
        [xc + y, yc - x],
        [xc - y, yc - x],
        ]
    return np.array(res)

def solid_circle(xc, yc, radius):
    x = 0
    y = radius
    p = 1 - radius
    py5.points(circlePlotPoints(xc, yc, x, y))
    
    while(x < y):
        x+=1
        if (p < 0):
            p+= 2*x + 1
        else:
            y-=1
            p+= 2*(x-y) + 1
        py5.points(circlePlotPoints(xc, yc, x, y))
        
def dotted_circle(x, y, radius):
    py5.no_fill()
    circumference = py5.TWO_PI * radius
    dot_spacing = 10
    num_dots = int(circumference / dot_spacing)
    
    for i in range(num_dots):
        angle = py5.TWO_PI * i / num_dots
        dot_x = x + radius * py5.cos(angle)
        dot_y = y + radius * py5.sin(angle)
        py5.point(dot_x, dot_y)
        
def dotted_striped_circle(x,y,radius):
    py5.no_fill()
    circumference = py5.TWO_PI * radius
    dot_spacing = 10
    num_dots = int(circumference / dot_spacing)
    
    dash_length = 10
    gap_length = 20
    pattern_length = dash_length + gap_length
    num_dashes = int(circumference / pattern_length)
    angle_step = py5.TWO_PI / num_dashes
    current_angle = 0
    
    for i in range(num_dots):
        angle = py5.TWO_PI * i / num_dots
        dot_x = x + radius * py5.cos(angle)
        dot_y = y + radius * py5.sin(angle)
        py5.point(dot_x, dot_y)
    
    for i in range(num_dashes):
        next_angle = current_angle + angle_step * (dash_length / pattern_length)
        x1 = x + radius * py5.cos(current_angle)
        y1 = y + radius * py5.sin(current_angle)
        x2 = x + radius * py5.cos(next_angle)
        y2 = y + radius * py5.sin(next_angle)
        py5.line(x1, y1, x2, y2)
        current_angle = next_angle + (gap_length / pattern_length) * angle_step


def dashed_circle(x, y, radius):
    py5.no_fill()
    circumference = py5.TWO_PI * radius
    dash_length = 5
    gap_length = 10
    pattern_length = dash_length + gap_length

    num_dashes = int(circumference / pattern_length)
    angle_step = py5.TWO_PI / num_dashes

    current_angle = 0
    for i in range(num_dashes):
        next_angle = current_angle + angle_step * (dash_length / pattern_length)
        x1 = x + radius * py5.cos(current_angle)
        y1 = y + radius * py5.sin(current_angle)
        x2 = x + radius * py5.cos(next_angle)
        y2 = y + radius * py5.sin(next_angle)
        py5.line(x1, y1, x2, y2)
        current_angle = next_angle + (gap_length / pattern_length) * angle_step


