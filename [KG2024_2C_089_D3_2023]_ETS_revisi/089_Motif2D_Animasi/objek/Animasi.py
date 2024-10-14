import numpy as np
import primitif.transformasiv2 as tf

class Animasi:
    points = []
    def __init__(self, points):
        self.points = points

    def setPoints(self, points):
        self.points = points
    
    def rotate(self, points, refx, refy, angle):
        rotated_ellipse = [tf.rotate2D(x, y, angle, refx, refy) for x, y in points]    
        return rotated_ellipse 
    
    def scale(self, sx, sy, refx, refy, points):
        scaled_points = []

        for x, y in points:
            transformed_point = tf.scale2D(sx, sy, refx,refy, np.array([[x], [y], [1]]))
            x_scaled = transformed_point[0, 0]
            y_scaled = transformed_point[1, 0]
            
            scaled_points.append((x_scaled, y_scaled))

        return scaled_points
    
    def translate(self, tx, ty, points):
        translated_points = []

        for x, y in points:
            transformed_point = tf.translate2D(tx, ty, np.array([[x], [y], [1]]))
            x_translated = transformed_point[0, 0] 
            y_translated = transformed_point[1, 0] 

            translated_points.append((x_translated, y_translated))

        return translated_points
