import py5
import primitif.line as line
import primitif.basic as basic
import primitif.utility as utility
import config
import math

def draw_clock(x, y, hour, minute, second, frame_style, frame_color, inner_circle_color, name_clock):
    py5.stroke_weight(2)  
    py5.stroke(*frame_color)
    
    # Radius Dalam     
    basic.draw_circle(x, y, config.CLOCK_RADIUS, config.BLACK, 'solid')
    basic.draw_circle(x, y, config.CLOCK_RADIUS+1, config.BLACK, 'solid')
    # Radius Luar    
    basic.draw_circle(x, y, config.CLOCK_RADIUS + 10, inner_circle_color, frame_style)
    
    line.draw_ticks(x, y, config.CLOCK_RADIUS - 15, config.BLUE)
    
    #Nama Waktu Jam
    py5.text(name_clock, x,y+config.CLOCK_RADIUS+40)

    #Jarum Jam
    hour_angle = (hour % 12) * 30 + minute * 0.5
    minute_angle = minute * 30 + second * 0.5
    second_angle = second * 6
    hour_end_x = x + 50 * math.cos(math.radians(hour_angle - 90))
    hour_end_y = y + 50 * math.sin(math.radians(hour_angle - 90))
    minute_end_x = x + 70 * math.cos(math.radians(minute_angle - 90))
    minute_end_y = y + 70 * math.sin(math.radians(minute_angle - 90))
    second_end_x = x + 70 * math.cos(math.radians(second_angle - 90))
    second_end_y = y + 70 * math.sin(math.radians(second_angle - 90))

    line.draw_line(x, y, hour_end_x, hour_end_y, 3, config.BLACK)  
    line.draw_line(x, y, minute_end_x, minute_end_y, 2, config.BLACK)
    line.draw_line(x, y, second_end_x, second_end_y, 2, config.RED)

def setup():
    py5.size(config.WIDTH, config.HEIGHT)
    py5.background(*config.WHITE)
    py5.text_size(24)
    py5.text_align(py5.CENTER, py5.CENTER)

def draw():
    py5.background(*config.WHITE)
    
    hour_a = 15
    minute_a = 45
    second_a = 0
    hour_b = 10
    minute_b = 45
    second_b = 0
    hour_c = 7
    minute_c = 45
    second_c = 0
    
    x = config.WIDTH/6
    y = config.HEIGHT/2

    draw_clock(x, y, hour_a, minute_a, second_a, 'dotted', config.BLUE, config.GRAY, 'Waktu Ambon')

    draw_clock(3*x, y, hour_b, minute_b, second_b, 'dotted_striped', config.GREEN, config.GRAY, 'Waktu Abu Dhabi')

    draw_clock(5*x , y, hour_c, minute_c, second_c, 'dashed', config.UNGU, config.GRAY, 'Waktu Abuja')

py5.run_sketch()