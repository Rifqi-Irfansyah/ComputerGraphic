import numpy as np
import py5
import primitif.line
import primitif.basic as basic
import primitif.utility
import math
import config
import primitif.transformasiv2 as tf
    
class Garis:
    def __init__(self, warna, tebal):
        self.warna = warna
        self.tebal = tebal

    def apply_stroke(self):
        py5.stroke(self.warna[0], self.warna[1], self.warna[2])
        py5.stroke_weight(self.tebal)


class Bunga:
    points = 0
    def __init__(self, xc, yc, radius_lingkaran, jumlah_kelopak, color, pattern):
        self.xc = xc
        self.yc = yc
        self.radius_lingkaran = radius_lingkaran
        self.jumlah_kelopak = jumlah_kelopak
        self.pattern = pattern
        self.color = color

    def lingkaran_tengah(self):
        basic.draw_circle(self.xc, self.yc, self.radius_lingkaran, self.pattern)

#     def kelopak_bunga(self, Rx, Ry):
#         angle_step = 360 / self.jumlah_kelopak
#         for i in range(self.jumlah_kelopak):
#             angle = math.radians(i * angle_step)
#             kelopak_x = self.xc + self.radius_lingkaran * math.cos(angle)
#             kelopak_y = self.yc + self.radius_lingkaran * math.sin(angle)
#             py5.push_matrix()
#             py5.translate(kelopak_x, kelopak_y)
#             py5.rotate(angle)
#             basic.draw_ellipse(0, 0, Rx * 2, Ry * 2, self.pattern)
#             py5.pop_matrix()

    def kelopak_bunga(self, Rx, Ry):
        angle_step = 360 / self.jumlah_kelopak
        for i in range(self.jumlah_kelopak):
            angle = i * angle_step
            
            # Compute the petal position
            kelopak_x = self.xc + self.radius_lingkaran * math.cos(math.radians(angle))
            kelopak_y = self.yc + self.radius_lingkaran * math.sin(math.radians(angle))
            
            # Create the transformation matrix for translation and rotation
#             translation_matrix = tf.translate2D(kelopak_x, kelopak_y, np.identity(3))
            rotation_matrix = tf.rotate2D(angle_step, self.xc, self.yc)
#             scale_matrix = tf.scale2D(1, 1, 0, 0, np.identity(3))
#             transformation_matrix = np.dot(translation_matrix, np.dot(rotation_matrix, scale_matrix))
            
            # Define the petal shape as a set of points (ellipse approximation)
            petal_points = np.array([
                [-Rx, -Ry],
                [Rx, -Ry],
                [Rx, Ry],
                [-Rx, Ry]
            ])
            
            # Apply the transformation to the petal points
            transformed_points = tf.transformPoints2D(petal_points, rotation_matrix)
            
            # Compute the center of the ellipse in the transformed space
            center_x = transformed_points.mean(axis=0)[0]
            center_y = transformed_points.mean(axis=0)[1]

            # Draw the petal using basic.draw_ellipse
            points = basic.draw_ellipse(0, 0, Rx * 2, Ry * 2, self.pattern)
            return (points)
    
    def gambar_bunga(self, value=None, name_animate=None):
        points = 0
        py5.stroke(*self.color)
        if (name_animate=="skala"):
            self.gambar_bunga_withscale(value)
        else:
            self.lingkaran_tengah()
            points = self.kelopak_bunga(self.radius_lingkaran, self.radius_lingkaran // 2)
        
        return(points)
    
    def gambar_bunga_withscale(self, scale_matrix):
        self.lingkaran_tengah()
        
        py5.push_matrix()
        # Apply matrix elements as individual parameters
        py5.apply_matrix(
            scale_matrix[0, 0], scale_matrix[0, 1], scale_matrix[0, 2],
            scale_matrix[1, 0], scale_matrix[1, 1], scale_matrix[1, 2]
        )
        py5.stroke(*self.color)
        self.kelopak_bunga(self.radius_lingkaran, self.radius_lingkaran // 2)
        
        py5.pop_matrix()

    def gambar_bunga_withrotate(self):
        angle_step = 360 / self.jumlah_kelopak
        for i in range(self.jumlah_kelopak):
            angle_radians = math.radians(i * angle_step)
            kelopak_x = self.xc + self.radius_lingkaran * math.cos(angle_radians)
            kelopak_y = self.yc + self.radius_lingkaran * math.sin(angle_radians)
            
            # Define the points of the petal as a rectangle
            petal_points = np.array([
                [-self.radius_lingkaran, -self.radius_lingkaran // 2, 1],  # Top-left corner
                [self.radius_lingkaran, -self.radius_lingkaran // 2, 1],   # Top-right corner
                [self.radius_lingkaran, self.radius_lingkaran // 2, 1],    # Bottom-right corner
                [-self.radius_lingkaran, self.radius_lingkaran // 2, 1]    # Bottom-left corner
            ])

            # Create transformation matrix for rotation
            tm = tf.rotate2D(math.degrees(angle_radians + math.radians(angle)), 0, 0)
            # Apply translation to move the petal to the correct position
            tm = tf.translate2D(kelopak_x, kelopak_y, tm)

            # Transform the points of the petal
            transformed_points = tf.transformPoints2D(petal_points, tm)

            # Draw the petal
            py5.begin_shape()
            for pt in transformed_points:
                py5.vertex(pt[0], pt[1])
            py5.end_shape(py5.CLOSE)


margin = 25
def setup():
    py5.size(config.WIDTH, config.HEIGHT)
    py5.background(255)
    
scaleX = 1
scaleY = 1
helper = 1
angle = 0

def updateTime():
    global scaleX, scaleY, helper, angle
    
    helper += 0.01
    
    if(helper >= 2):
        helper = 1
    
    if(helper <= 1.5):
        scaleX += 0.01
        scaleY += 0.01
        
    elif(1.5<= helper <= 2):
        scaleX -= 0.01
        scaleY -= 0.01
        
    angle += 1
    if angle >= 360:
        angle = 0


def draw():
    py5.background(255)
    
    primitif.basic.draw_margin(py5.width, py5.height, margin, c=[0,0,0,255])
    primitif.basic.draw_kartesian(py5.width, py5.height, margin, c=[0,0,0,255])
    
    updateTime()
    
    x = (config.WIDTH-margin)/4 -margin/2
    y = (config.HEIGHT-margin)/4 -margin/2
    py5.translate(config.WIDTH /2, config.HEIGHT / 2)
    
    py5.fill(*config.MAGENTA)
    py5.text(helper, x,-y)
    
    py5.scale(1, -1)
    
    
    scale_matrix = tf.scale2D(scaleX, scaleY, x, y, np.identity(3))
#     rotate_matrix = tf.rotate2D(rotation_angle, x, y)

    
    bunga1 = Bunga(x, y, 30, 4, config.GREEN, "solid")
    bunga1.gambar_bunga(scale_matrix, "skala")
    
    bunga2 = Bunga(-x, y, 40, 5, config.BLUE, "dotted")
#     bunga2.gambar_bunga_withrotate()
    
    bunga3 = Bunga(-x, -y, 40, 7, config.MAGENTA, "dotted_striped")
    bunga3.gambar_bunga()
    
    bunga4 = Bunga(x, -y, 40, 8, config.PURPLE, "dashed")
#     bunga4.gambar_bunga_withrotate()
    
    
    a = py5.width//2
    b = py5.height//2
    x = 0
    y = 0
    r = py5.width//15

    bentuk = bunga2.gambar_bunga()
    global angle
    
    tm = tf.rotate2D(angle, x, y)    
    rotasi = tf.transformPoints2D(bentuk, tm)
    translasi = tf.translate2D(a, b)
    rotasi = tf.transformPoints2D(rotasi, translasi)
    bunga2.gambar_bunga(rotasi)
    
            
    angle += 10
        

py5.run_sketch()

