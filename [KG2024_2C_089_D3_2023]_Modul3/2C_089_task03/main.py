import py5
import primitif.line
import primitif.basic
import math

turn = 1

class Tile:
    def __init__(self, label : int):
        self.label = label
        self.visible = False
        
    def draw():
        pass

rows = 3
cols = 3

grid = [ [Tile(0) for n in range(rows)] for n in range(cols) ]

w = 70

def switch_turns():
    global turn
    if turn == 1:
        turn = 2
    else:
        turn = 1

def zero_sign(x,y,r):
    primitif.basic.lingkaran(x,y,r/2)

def x_sign(x,y,r):
    primitif.basic.kali(x,y,r)
    
def draw_xoxBoard():
    for y in range(rows):
        for x in range(cols):
            primitif.basic.persegi(w*x,w*y,w)

def draw_player():
    for y in range(rows):
        for x in range(cols):
            if grid[y][x].label == 2:
                zero_sign(x*w+w/2,y*w+w/2,w)
            elif grid[y][x].label == 1:
                x_sign(x*w, y*w, w)

def setup():
    py5.size(800, 600)

def draw():
    draw_xoxBoard()
    draw_player()

def mouse_pressed():
    if (grid[py5.mouse_y//w][py5.mouse_x//w].label == 0):
        grid[py5.mouse_y//w][py5.mouse_x//w].label = turn
        switch_turns()
        
py5.run_sketch()
