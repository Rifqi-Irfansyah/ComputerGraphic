import primitif.line
import py5

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
    
    inner_width = width - 2*margin
    inner_height = height - 2*margin
    
    py5.points(primitif.line.line_dda(margin+inner_width/3, margin, margin+inner_width/3, height-margin))
    py5.points(primitif.line.line_dda(margin+inner_width*2/3, margin, margin+inner_width*2/3, height-margin))
    py5.points(primitif.line.line_bresenham(margin, margin + inner_height/3, width-margin, margin + inner_height/3))
    py5.points(primitif.line.line_bresenham(margin, margin + inner_height*2/3, width-margin, margin +inner_height*2/3))
    
def draw_x(x,y, length):
    left 	= x-length/2
    right 	= x+length/2
    top 	= y-length/2
    down 	= y+length/2
    py5.points(primitif.line.line_bresenham(left,top, right,down))
    py5.points(primitif.line.line_bresenham(left,down, right,top))
    
def draw_o(x,y,length):
    left 	= x-length/2
    right 	= x+length/2
    top 	= y-length/2
    down 	= y+length/2
    py5.points(primitif.line.line_bresenham(left,top, right,top))
    py5.points(primitif.line.line_bresenham(left,down, right,down))
    py5.points(primitif.line.line_bresenham(right,top, right,down))
    py5.points(primitif.line.line_bresenham(left,top, left,down))
    