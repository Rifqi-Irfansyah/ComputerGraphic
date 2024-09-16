import py5
import primitif.line
import primitif.basic as pb
import primitif.utility
import math
import config


def setup():
    py5.size(config.WIDTH, config.HEIGHT)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.background(*config.WHITE)
    x = config.WIDTH/4
    y = config.HEIGHT/2
    x2 = config.WIDTH*3/4
    y2 = config.WIDTH/4
    
    py5.stroke(*config.BLACK)
    pb.lingkaran(x, y, 50)
    pb.ellipse(x2,y2, 150, 80)
    
py5.run_sketch()

