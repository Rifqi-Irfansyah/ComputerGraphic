import primitif.line
import py5
import numpy as np

def round(x):
    return int(x+0.5)

def draw_margin(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(margin,margin,width-margin,margin))
    py5.points(primitif.line.line_dda(margin,height-margin,width-margin,height-margin))
    py5.points(primitif.line.line_bresenham(margin,margin,margin,height-margin))
    py5.points(primitif.line.line_bresenham(width-margin,margin,width-margin,height-margin))

def draw_grid(width, height, margin, c=[0,0,0,255]):
    # Sumbu Y
    xa = margin;
    ya = 2*margin;
    xb = width - xa
    yb = height - ya
    y_range = (height / margin)
    
    py5.stroke(c[0], c[1], c[2], c[3])
    for count in range(1, int(y_range)):
        py5.points(primitif.line.line_dda(xa,ya,xb,ya))
        ya = ya + margin

    # Sumbu X
    xa = 2*margin
    ya = margin
    xb = width - xa
    yb = height - ya
    x_range = (width / margin)
    for count in range(1, int(x_range)):
        py5.points(primitif.line.line_dda(xa,ya,xa,yb))
        xa = xa + margin

def draw_kartesian(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(width/2,margin,width/2,height-margin))
    py5.points(primitif.line.line_bresenham(margin,height/2,width-margin,height/2))
    
def persegi(xa, ya, panjang, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_bresenham(xa,ya,xa+panjang,ya))
    py5.points(primitif.line.line_bresenham(xa,ya+panjang,xa+panjang,ya+panjang))
    py5.points(primitif.line.line_bresenham(xa,ya,xa,ya+panjang))
    py5.points(primitif.line.line_bresenham(xa+panjang,ya, xa+panjang,ya+panjang))

def persegi_panjang(xa, ya, panjang, lebar, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    pass

def segitiga_siku(xa, ya, alas, tinggi, c=[255,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    pass


def trapesium_siku(xa, ya, aa, ab, tinggi, c=[255,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    pass

def kali(xa, ya, panjang, c=[255,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_bresenham(xa,ya,xa+panjang,ya+panjang))
    py5.points(primitif.line.line_bresenham(xa,ya+panjang,xa+panjang,ya))


#LINGAKRAN
def draw_circle(x, y, radius, style=None):
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
        
#ELLIPS
def draw_ellipse(x, y, Rx, Ry, style=None):
    py5.stroke_weight(2)

    if style == 'solid':
        solid_ellipse(x, y, Rx, Ry)
    elif style == 'dotted':
        dotted_ellipse(x, y, Rx, Ry)
    elif style == 'dotted_striped':
        dotted_striped_ellipse(x, y, Rx, Ry)
    elif style == 'dashed':
        dashed_ellipse(x, y, Rx, Ry)
    else:
        print("Maaf, style tidak ada")


def ellipsePlotPoints(xc, yc, x, y):
    res = [
        [xc + x, yc + y],
        [xc - x, yc + y],
        [xc + x, yc - y],
        [xc - x, yc - y],
    ]
    return np.array(res)


def solid_ellipse(xc, yc, Rx, Ry):
    x = 0
    y = Ry
    Rx2 = Rx * Rx
    Ry2 = Ry * Ry
    px = 0
    py = 2 * Rx2 * y

    p1 = Ry2 - (Rx2 * Ry) + (0.25 * Rx2)
    while px < py:
        py5.points(ellipsePlotPoints(xc, yc, x, y))
        x += 1
        px += 2 * Ry2
        if p1 < 0:
            p1 += Ry2 + px
        else:
            y -= 1
            py -= 2 * Rx2
            p1 += Ry2 + px - py

    p2 = Ry2 * (x + 0.5) ** 2 + Rx2 * (y - 1) ** 2 - Rx2 * Ry2
    while y >= 0:
        py5.points(ellipsePlotPoints(xc, yc, x, y))
        y -= 1
        py -= 2 * Rx2
        if p2 > 0:
            p2 += Rx2 - py
        else:
            x += 1
            px += 2 * Ry2
            p2 += Rx2 - py + px


def dotted_ellipse(x, y, Rx, Ry):
    py5.no_fill()
    circumference = py5.TWO_PI * ((Rx + Ry) / 2)  # Approximate circumference
    dot_spacing = 10
    num_dots = int(circumference / dot_spacing)

    for i in range(num_dots):
        angle = py5.TWO_PI * i / num_dots
        dot_x = x + Rx * py5.cos(angle)
        dot_y = y + Ry * py5.sin(angle)
        py5.point(dot_x, dot_y)


def dotted_striped_ellipse(x, y, Rx, Ry):
    py5.no_fill()
    circumference = py5.TWO_PI * ((Rx + Ry) / 2)  # Approximate circumference
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
        dot_x = x + Rx * py5.cos(angle)
        dot_y = y + Ry * py5.sin(angle)
        py5.point(dot_x, dot_y)

    for i in range(num_dashes):
        next_angle = current_angle + angle_step * (dash_length / pattern_length)
        x1 = x + Rx * py5.cos(current_angle)
        y1 = y + Ry * py5.sin(current_angle)
        x2 = x + Rx * py5.cos(next_angle)
        y2 = y + Ry * py5.sin(next_angle)
        py5.line(x1, y1, x2, y2)
        current_angle = next_angle + (gap_length / pattern_length) * angle_step


def dashed_ellipse(x, y, Rx, Ry):
    py5.no_fill()
    circumference = py5.TWO_PI * ((Rx + Ry) / 2)  # Approximate circumference
    dash_length = 5
    gap_length = 10
    pattern_length = dash_length + gap_length

    num_dashes = int(circumference / pattern_length)
    angle_step = py5.TWO_PI / num_dashes

    current_angle = 0
    for i in range(num_dashes):
        next_angle = current_angle + angle_step * (dash_length / pattern_length)
        x1 = x + Rx * py5.cos(current_angle)
        y1 = y + Ry * py5.sin(current_angle)
        x2 = x + Rx * py5.cos(next_angle)
        y2 = y + Ry * py5.sin(next_angle)
        py5.line(x1, y1, x2, y2)
        current_angle = next_angle + (gap_length / pattern_length) * angle_step


