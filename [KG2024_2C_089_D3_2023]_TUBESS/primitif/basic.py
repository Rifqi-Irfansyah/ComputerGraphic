import primitif.line
import py5
import numpy as np
import math

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


def trapesium_siku(xa, ya, aa, ab, tinggi, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_bresenham(xa, ya, xa + aa, ya))
    py5.points(primitif.line.line_bresenham(xa + aa, ya, xa + ab, ya + tinggi))
    py5.points(primitif.line.line_bresenham(xa + ab, ya + tinggi, xa, ya + tinggi))
    py5.points(primitif.line.line_bresenham(xa, ya + tinggi, xa, ya))

def trapesium_tanpa_alas(xa, ya, atas, bawah, tinggi, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_bresenham(xa-bawah/2, ya-tinggi/2, xa-atas/2, ya+tinggi/2)) #kiri
    py5.points(primitif.line.line_bresenham(xa-atas/2, ya+tinggi/2, xa+atas/2, ya+tinggi/2)) #atas
    py5.points(primitif.line.line_bresenham(xa+bawah/2, ya-tinggi/2, xa+atas/2, ya+tinggi/2)) #kanan
    
def kali(xa, ya, panjang, c=[255,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_bresenham(xa,ya,xa+panjang,ya+panjang))
    py5.points(primitif.line.line_bresenham(xa,ya+panjang,xa+panjang,ya))


#LINGAKRAN
def draw_circle(radius, center_x, center_y, pattern='solid'):
    circle_pts = circle_points(radius, center_x, center_y)
    pattern_points = []
    
    def draw_dots():
        dot_space = 1.5
        for i, (px, py) in enumerate(circle_pts):
            if i % dot_space == 0:
                pattern_points.append((px, py))
    
    def draw_dash_dot():
        dash_length = 30
        gap_length = 20
        pattern_length = dash_length + gap_length
        for i, (px, py) in enumerate(circle_pts):
            if (i // (dash_length + gap_length)) % 2 == 0:
                pattern_points.append((px, py))
    
    def draw_dash_dash():
        dash_length = 30
        gap_length = 20
        pattern_length = dash_length + gap_length
        for i, (px, py) in enumerate(circle_pts):
            if (i // pattern_length) % 2 == 0:
                if (i % pattern_length) < dash_length:
                    pattern_points.append((px, py))
    
    def draw_solid():
        for px, py in circle_pts:
            pattern_points.append((px, py))
    
    # Draw the circle with the selected pattern
    if pattern == 'dot':
        draw_dots()
    elif pattern == 'dash_dot':
        draw_dash_dot()
    elif pattern == 'dash_dash':
        draw_dash_dash()
    elif pattern == 'solid':
        draw_solid()
    else:
        print("Pattern not recognized")
    return (pattern_points)
        
def circle_points(radius, center_x, center_y):
    points = []
    x = radius
    y = 0
    p = 1 - radius  # Initial decision parameter

    # Circle points in the first octant
    while x >= y:
        points.extend([
            (center_x + x, center_y + y),
            (center_x - x, center_y + y),
            (center_x + x, center_y - y),
            (center_x - x, center_y - y),
            (center_x + y, center_y + x),
            (center_x - y, center_y + x),
            (center_x + y, center_y - x),
            (center_x - y, center_y - x)
        ])
        y += 1
        if p > 0:
            x -= 1
            p += 2 * (y - x) + 1
        else:
            p += 2 * y + 1
    points.sort(key=lambda point: math.atan2(point[1] - center_y, point[0] - center_x))
    return points


        
#ELLIPS
    
def rotate2D(a, refx, refy):
    m = np.identity(3)
    tm = np.identity(3)
    a = np.radians(a)
    m[0][0] = math.cos(a)
    m[0][1] = -math.sin(a)
    m[0][2] = refx * (1 - math.cos(a)) + refy * math.sin(a)
    m[1][0] = math.sin(a)
    m[1][1] = math.cos(a)
    m[1][2] = refy * (1 - math.cos(a)) - refx * math.sin(a)
    return np.dot(m, tm)
    
    
    new_x = x * np.cos(angle) - y * np.sin(angle)
    new_y = x * np.sin(angle) + y * np.cos(angle)
    return new_x, new_y



def ellipsePlotPoints(xc, yc, x, y):
    res = [
        [xc + x, yc + y],
        [xc - x, yc + y],
        [xc + x, yc - y],
        [xc - x, yc - y],
    ]
    return np.array(res)

def bresenham_ellipse(rx, ry, xc, yc):
    ellipse_points = []
    
    x = 0
    y = ry
    rx2 = rx * rx
    ry2 = ry * ry
    tworx2 = 2 * rx2
    twory2 = 2 * ry2
    px = 0
    py = tworx2 * y
    
    # Region 1
    p = ry2 - (rx2 * ry) + (0.25 * rx2)
    
    while px < py:
        ellipse_points.append((x + xc, y + yc))
        ellipse_points.append((-x + xc, y + yc))
        ellipse_points.append((x + xc, -y + yc))
        ellipse_points.append((-x + xc, -y + yc))
        
        x += 1
        px += twory2
        if p < 0:
            p += ry2 + px
        else:
            y -= 1
            py -= tworx2
            p += ry2 + px - py
    
    # Region 2
    p = ry2 * (x + 0.5) * (x + 0.5) + rx2 * (y - 1) * (y - 1) - rx2 * ry2
    
    while y >= 0:
        ellipse_points.append((x + xc, y + yc))
        ellipse_points.append((-x + xc, y + yc))
        ellipse_points.append((x + xc, -y + yc))
        ellipse_points.append((-x + xc, -y + yc))
        
        y -= 1
        py -= tworx2
        if p > 0:
            p += rx2 - py
        else:
            x += 1
            px += twory2
            p += rx2 - py + px
    ellipse_points.sort(key=lambda point: math.atan2(point[1] - yc, point[0] - xc))
    
    return ellipse_points


def draw_patterned_ellipse(rx, ry, xc, yc, pattern='solid'):
    ellipse_points = bresenham_ellipse(rx, ry, xc, yc)
    pattern_points = []
    
    def draw_dots():
        dot_space = 1.5
        for i, (px, py) in enumerate(ellipse_points):
            if i % dot_space == 0:
                pattern_points.append((px, py))

    
    def draw_dash_dot():
        dash_length = 30
        gap_length = 20
        pattern_length = dash_length + gap_length
        for i, (px, py) in enumerate(ellipse_points):
            if (i // (dash_length + gap_length)) % 2 == 0:
                pattern_points.append((px, py))
    
    def draw_dash_dash():
        dash_length = 30
        gap_length = 20
        pattern_length = dash_length + gap_length
        for i, (px, py) in enumerate(ellipse_points):
            if (i // pattern_length) % 2 == 0:
                if (i % pattern_length) < dash_length:
                    pattern_points.append((px, py))
    
    def draw_solid():
        for px, py in ellipse_points:
            pattern_points.append((px, py))
    
    # Draw the ellipse with the selected pattern
    if pattern == 'dot':
        draw_dots()
    elif pattern == 'dash_dot':
        draw_dash_dot()
    elif pattern == 'dash_dash':
        draw_dash_dash()
    elif pattern == 'solid':
        draw_solid()
    else:
        print("Pattern not recognized")
        
    return (pattern_points)

