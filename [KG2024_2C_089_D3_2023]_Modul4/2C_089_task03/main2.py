import py5
import numpy as np
import primitif.transformasiv2 as tf


# py5 setup function
def setup():
    py5.size(400, 400)

# Global variables for animation
angle = 0
tx, ty = 0, 0

# py5 draw function to create animation
def draw():
    global angle, tx, ty

    py5.background(255)
    
    # Rectangle corners (as a matrix)
    rect_points = np.array([
        [100, 50, 1],  # Top-left corner
        [150, 50, 1],  # Top-right corner
        [150, 100, 1], # Bottom-right corner
        [100, 100, 1]  # Bottom-left corner
    ])

    # Create transformation matrix
    tm = np.identity(3)
    
    # Apply transformations (translation, scaling, rotation)
    tm = tf.translate2D(tx, ty, tm)  # Move the rectangle
    tm = tf.scale2D(1.2, 1.2, 125, 75, tm)  # Scale the rectangle
    tm = tf.rotate2D(angle, 125, 75)  # Rotate the rectangle around its center
    
    # Transform the points of the rectangle
    transformed_points = tf.transformPoints2D(rect_points, tm)

    # Draw the transformed rectangle
    py5.begin_shape()
    for i in range(4):
        py5.vertex(transformed_points[i, 0], transformed_points[i, 1])
    py5.end_shape(py5.CLOSE)
    
    # Update transformation variables for animation
    angle += 1  # Increase rotation angle
    tx += 1     # Translate along x-axis
    ty += 0.5   # Translate along y-axis
    
    if tx > py5.width:
        tx = -150  # Reset to start position if out of bounds

py5.run_sketch()
