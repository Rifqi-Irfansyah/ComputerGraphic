import primitif.line
import py5

def draw_margin(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(margin, margin, width-margin, margin))
    py5.points(primitif.line.line_dda(margin, margin, margin, height-margin))
    py5.points(primitif.line.line_dda(margin, height-margin, width-margin, height-margin))
    py5.points(primitif.line.line_dda(width-margin, height-margin, width-margin, margin))

def draw_kartesian(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(margin, height/2, width-margin, height/2))
    py5.points(primitif.line.line_dda(width/2, margin, width/2, height-margin))