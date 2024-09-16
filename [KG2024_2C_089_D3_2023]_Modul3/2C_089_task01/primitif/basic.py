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

def lingkaran(xc, yc, radius, c=[255,0,0,255]):
    x = 0
    y = radius
    p = 1 - radius
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(circlePlotPoints(xc, yc, x, y))
    
    while(x < y):
        x+=1
        if (p < 0):
            p+= 2*x + 1
        else:
            y-=1
            p+= 2*(x-y) + 1
        py5.points(circlePlotPoints(xc, yc, x, y))
        
def ellipsePlotPoints(xc, yc, x, y):
    pass

def ellipse(xc, yc, Rx, Ry, c=[255,0,0,255]):
    pass