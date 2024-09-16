import math

def convert_to_pixel(xa, ya, xb, yb, width, height, margin):
    return [margin+xa, height-margin-ya, margin+xb, height-margin-yb]

def convert_to_cartesian(xa, ya, xb, yb, width, height, margin):
    axis = math.ceil(width/2)
    ordinat = math.ceil(height/2)
    return [axis+xa, ordinat-ya, axis+xb, ordinat-yb]
