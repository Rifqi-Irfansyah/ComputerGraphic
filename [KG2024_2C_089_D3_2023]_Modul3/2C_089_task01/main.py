import py5
import primitif.line
import primitif.basic
import primitif.utility
import math
import config

w, h, r = (py5.width, py5.height, 200)
top_left, top_middle, top_right = (0,0,0)
middle_left, middle_middle, middle_right = (0,0,0)
bottom_left, bottom_middle, bottom_right = (0,0,0)
turn = 1


def switch_turns():
    global turn
    if turn == 1:
        turn = 2
    else:
        turn = 1

def draw_xoxBoard():
    for y in range(3):
        for x in range(3):
            primitif.basic.persegi(r*x,r*y,r)
            
def zero_sign(x,y,r):
    primitif.basic.lingkaran(x,y,r/2)

def x_sign(x,y,r):
    primitif.basic.kali(x,y,r)

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.background(191)
    (top_left,0)
    (top_middle,0)
    (top_right,0)
    (middle_left,0)
    (middle_middle,0)
    (middle_right,0)
    (bottom_left,0)
    (bottom_middle,0)
    (bottom_right,0)
    draw_xoxBoard()
    
    ## Top Row   
    if top_left == 2: 
        zero_sign(r/2,r/2,r)
    elif top_left == 1:
        x_sign(0,0,r)
    if top_middle == 2: 
        zero_sign(3*r/2,r/2,r)
    elif top_middle == 1:
        x_sign(r,0,r)    
    if top_right == 2:
        zero_sign(5*r/2,r/2,r)
    elif top_right == 1:
        x_sign(2*r,0,r)
        
    ## Middle Row   
    if middle_left == 2: 
        zero_sign(r/2,r+r/2,r)
    elif middle_left == 1:
        x_sign(0,r,r)
    if middle_middle == 2: 
        zero_sign(3*r/2,r+r/2,r)
    elif middle_middle == 1:
        x_sign(r,r,r)    
    if middle_right == 2: 
        zero_sign(5*r/2,r+r/2,r)
    elif middle_right == 1:
        x_sign(2*r,r,r)
        
    ## Bottom Row   
    if bottom_left == 2: 
        zero_sign(r/2,2*r+r/2,r)
    elif bottom_left == 1:
        x_sign(0,2*r,r)
    if bottom_middle == 2: 
        zero_sign(3*r/2,2*r+r/2,r)
    elif bottom_middle == 1:
        x_sign(r,2*r,r)    
    if bottom_right == 2: 
        zero_sign(5*r/2,2*r+r/2,r)
    elif bottom_right == 1:
        x_sign(2*r,2*r,r)
    
def mouse_pressed():
    print(f"({py5.mouse_x}, {py5.mouse_y})")
    global top_left, top_middle, top_right
    global middle_left, middle_middle, middle_right
    global bottom_left, bottom_middle, bottom_right
    
    if((py5.mouse_x > 0 and py5.mouse_x < r) and (py5.mouse_y > 0 and py5.mouse_y < r )):
        if top_left == 0:
            top_left = turn
            switch_turns()
    elif((py5.mouse_x > r and py5.mouse_x < r*2) and (py5.mouse_y > 0 and py5.mouse_y < r )):
        if top_middle == 0:
            top_middle = turn
            switch_turns()
    elif((py5.mouse_x > r*2 and py5.mouse_x < r*3) and (py5.mouse_y > 0 and py5.mouse_y < r )):
        if top_right == 0:
            top_right = turn
            switch_turns()
    
    elif((py5.mouse_x > 0 and py5.mouse_x < r) and (py5.mouse_y > r and py5.mouse_y < r*2 )):
        if middle_left == 0:
            middle_left = turn
            switch_turns()
    elif((py5.mouse_x > r and py5.mouse_x < r*2) and (py5.mouse_y > r and py5.mouse_y < r*2 )):
        if middle_middle == 0:
            middle_middle = turn
            switch_turns()
    elif((py5.mouse_x > r*2 and py5.mouse_x < r*3) and (py5.mouse_y > r and py5.mouse_y < r*2 )):
        if middle_right == 0:
            middle_right = turn
            switch_turns()

    elif((py5.mouse_x > 0 and py5.mouse_x < r) and (py5.mouse_y > r*2 and py5.mouse_y < r*3 )):
        if bottom_left == 0:
            bottom_left = turn
            switch_turns()
    elif((py5.mouse_x > r and py5.mouse_x < r*2) and (py5.mouse_y > r*2 and py5.mouse_y < r*3 )):
        if bottom_middle == 0:
            bottom_middle = turn
            switch_turns()
    elif((py5.mouse_x > r*2 and py5.mouse_x < r*3) and (py5.mouse_y > r*2 and py5.mouse_x < r*3 )):
        if bottom_right == 0:
            bottom_right = turn
            switch_turns()    

py5.run_sketch()

