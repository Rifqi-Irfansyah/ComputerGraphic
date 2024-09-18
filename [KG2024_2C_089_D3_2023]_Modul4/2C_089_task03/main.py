import numpy as np
import py5
import math
import primitif.transformasiv2 as tf
import primitif.basic as basic
import config

rx, ry = 50, 30
xc, yc = 0,0
angle_dinamis = 0
margin = 20
translasi_x = py5.width/2
translasi_y = py5.height/2 + margin
scale_x, scale_y,helper = 0,0, 0
gerakan_ke_bawah = False
gerakan_ke_kiri = False
gerakan_ke_atas = False
gerakan_ke_kanan = True

class Bunga:
    points = 0
    def __init__(self, xc, yc, radius_lingkaran, jumlah_kelopak, color, pattern):
        self.xc = xc
        self.yc = yc
        self.radius_lingkaran = radius_lingkaran
        self.jumlah_kelopak = jumlah_kelopak
        self.pattern = pattern
        self.color = color

    def lingkaran_tengah(self, radius):
        circle_points = basic.draw_circle(radius, self.xc, self.yc, self.pattern)
        #DRAW
        for x, y in circle_points:
            py5.point(x  , y )
            
    def satu_kelopak(self, Rx, Ry):
        ellipse_points = basic.draw_patterned_ellipse(Rx, Ry, self.xc, self.yc, self.pattern)
        return ellipse_points


    def kelopak_bunga(self, Rx, Ry):
        ellipse_points = basic.draw_patterned_ellipse(Rx, Ry, self.xc, self.yc, self.pattern)
        
        anchor_radius = min(Rx, Ry) + self.radius_lingkaran# Adjust as needed
        angle_step = 360 / self.jumlah_kelopak
        
        angle = 0 + angle_dinamis
        for i in range (self.jumlah_kelopak):
            # ROTATE
            rotated_ellipse = [tf.rotate2D(x, y, angle, self.xc, self.yc) for x, y in ellipse_points]    
            
            # DRAW
            for x, y in rotated_ellipse:
                py5.point(x + anchor_radius * np.cos(np.deg2rad(angle)) , y + anchor_radius * np.sin(np.deg2rad(angle)))
            
            angle += angle_step
            angle = angle % 360
    
    def gambar_bunga(self):
        points = 0
        py5.stroke(*self.color)
        
        i = 0
        while i <= 2:
            self.lingkaran_tengah(self.radius_lingkaran + i)
            self.kelopak_bunga(self.radius_lingkaran * 2 + i, self.radius_lingkaran + i)
            i += 0.2
            
    def gambar_bunga_translasi(self, time):
        py5.stroke(*self.color)
        updateTranslasi(time)
        
        a=0
        while a <= 2:
            circle_points = basic.draw_circle(self.radius_lingkaran+a, self.xc, self.yc, self.pattern)
            tm = tf.translate2D(translasi_x, translasi_y)
            translasi = tf.transformPoints2D(circle_points, tm)
            
            for x, y in translasi:
                py5.point(x  , y )



            Rx = self.radius_lingkaran * 2 +a 
            Ry = self.radius_lingkaran  +a
            
            ellipse_points = basic.draw_patterned_ellipse(Rx, Ry, self.xc, self.yc, self.pattern)
            
            anchor_radius = min(Rx, Ry) + self.radius_lingkaran +a# Adjust as needed
            angle_step = 360 / self.jumlah_kelopak
            
            angle = 0 + angle_dinamis
            for i in range (self.jumlah_kelopak):
                # ROTATE
                rotated_ellipse = [tf.rotate2D(x, y, angle, self.xc, self.yc) for x, y in ellipse_points]
                tm = tf.translate2D(translasi_x, translasi_y)
                translasi = tf.transformPoints2D(rotated_ellipse, tm)
                
                # DRAW
                for x, y in translasi:
                    py5.point(x + anchor_radius * np.cos(np.deg2rad(angle)) , y + anchor_radius * np.sin(np.deg2rad(angle)))
                
                angle += angle_step
                angle = angle % 360
            a += 0.2
            
    def gambar_bunga_scale(self):
        py5.stroke(*self.color)
        a=0
        while a <= 2:
                
            # Draw and scale the center circle first
            circle_points = basic.draw_circle(self.radius_lingkaran+a, self.xc, self.yc, self.pattern)
            
            # Apply scaling transformation matrix
            tm = tf.scale2D(scale_x, scale_y, self.xc, self.yc)  # Create the scale matrix once
            scaled_circle_points = tf.transformPoints2D(circle_points, tm)
            
            # Draw the scaled circle
            for x, y in scaled_circle_points:
                py5.point(x, y)

            # Scale the ellipse (petals) points
            Rx = self.radius_lingkaran * 2+a
            Ry = self.radius_lingkaran+a
            ellipse_points = basic.draw_patterned_ellipse(Rx, Ry, self.xc, self.yc, self.pattern)

            # Apply the same scaling matrix to the ellipse points
            scaled_ellipse_points = tf.transformPoints2D(ellipse_points, tm)

            # Now position and rotate each scaled petal
            anchor_radius = min(Rx, Ry) + self.radius_lingkaran+a  # Calculate anchor radius
            angle_step = 360 / self.jumlah_kelopak
            angle = angle_dinamis

            for i in range(self.jumlah_kelopak):
                # Rotate the scaled ellipse points around the center
                rotated_ellipse = [tf.rotate2D(x, y, angle, self.xc, self.yc) for x, y in scaled_ellipse_points]
                
                # Draw the rotated and scaled petals
                for x, y in rotated_ellipse:
                    # Anchor petals to the center of the circle using the angle
                    py5.point(x + anchor_radius * np.cos(np.deg2rad(angle)),
                              y + anchor_radius * np.sin(np.deg2rad(angle)))

                angle += angle_step  # Move to the next petal position
                angle = angle % 360  # Keep the angle within [0, 360] degrees
                
            a += 0.2



def updateTime():
    global angle_dinamis, scale_x, scale_y, helper
    

    helper += 0.025

    if(helper >= 3):
        helper = 0

    if(helper <= 1.5):
        scale_x += 0.025
        scale_y += 0.025

    elif(1.5<= helper <= 3):
        scale_x -= 0.025
        scale_y -= 0.025
        

    if(angle_dinamis <= 360):
        angle_dinamis += 5
    else:
        angle_dinamis = 0
        

def updateTranslasi(r):
    global gerakan_ke_bawah, gerakan_ke_kiri, gerakan_ke_atas, gerakan_ke_kanan, translasi_x, translasi_y
    if gerakan_ke_bawah:
        translasi_y += r
        if translasi_y >= py5.height/4-margin*2:
            gerakan_ke_bawah = False
            gerakan_ke_kiri = True
    elif gerakan_ke_kiri:
        translasi_x -= r
        if translasi_x <= 0 - py5.height/4 - margin:
            gerakan_ke_kiri = False
            gerakan_ke_atas = True
    elif gerakan_ke_atas:
        translasi_y -= r
        if translasi_y <= -(py5.height/4-margin*2):
            gerakan_ke_atas = False
            gerakan_ke_kanan = True
    elif gerakan_ke_kanan:
        translasi_x += r
        if translasi_x >= py5.width/4 - margin:
            gerakan_ke_kanan = False
            gerakan_ke_bawah = True
            

def setup():
    py5.size(config.WIDTH, config.HEIGHT)

def draw():
    global angle, xc, yc
    py5.background(255)
    basic.draw_margin(py5.width, py5.height, margin, c=[0,0,0,255])
    basic.draw_kartesian(py5.width, py5.height, margin, c=[0,0,0,255])
    
    updateTime()
    
    py5.translate(config.WIDTH /2, config.HEIGHT / 2)
    py5.scale(1, -1)
    
    xc = (config.WIDTH-margin)/4 -margin/2
    yc = (config.HEIGHT-margin)/4 -margin/2
    
    bunga1 = Bunga(xc, yc, 30, 4, config.GREEN, "solid")
    bunga1.gambar_bunga()
    
    bunga2 = Bunga(-xc, yc, 30, 5, config.PURPLE, "dash_dash")
    bunga2.gambar_bunga_translasi(20)
    
    bunga3 = Bunga(xc, -yc, 30, 7, config.MAGENTA, "dot")
    bunga3.gambar_bunga_scale()
    
    bunga4 = Bunga(-xc, -yc, 30, 8, config.BLUE, "dash_dot")
    bunga4.gambar_bunga()


py5.run_sketch()
