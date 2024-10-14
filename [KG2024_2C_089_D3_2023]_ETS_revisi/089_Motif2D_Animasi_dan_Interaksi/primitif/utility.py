import math

def convert_to_cartesian(xa, ya, width, height):
    axis = math.ceil(width/2)
    ordinat = math.ceil(height/2)
    
    return [axis+xa, ordinat-ya]