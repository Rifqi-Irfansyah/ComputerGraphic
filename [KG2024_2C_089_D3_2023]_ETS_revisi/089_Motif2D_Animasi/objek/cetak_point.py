import py5
import config

def cetak_point(points, color=config.BLACK):
    py5.stroke(*color)
    for x,y in points:
        py5.point(x, y)