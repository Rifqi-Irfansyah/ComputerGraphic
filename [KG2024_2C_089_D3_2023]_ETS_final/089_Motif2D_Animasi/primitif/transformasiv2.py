import numpy as np
import math
# Transformation functions from your code
def translate2D(tx, ty, tm=np.identity(3)):
    m = np.identity(3)
    
    m[0][2] = tx
    m[1][2] = ty

    transormed = np.matmul(m,tm)
    return transormed
    
    return np.matmul(m, tm)

def scale2D(sx, sy, refx, refy, tm=np.identity(3)):
    m = np.identity(3)
    m[0][0] = sx
    m[0][2] = (1 - sx) * refx
    m[1][1] = sy
    m[1][2] = (1 - sy) * refy
    return np.dot(m, tm)

def rotate2D(x, y, a, refx, refy):
    a = np.radians(a)
    
    rotation_matrix = np.array([
        [np.cos(a), -np.sin(a)],
        [np.sin(a), np.cos(a)]
    ])
    
    point = np.array([x - refx, y - refy])
    rotated_point = rotation_matrix @ point

    x_new, y_new = rotated_point[0] + refx, rotated_point[1] + refy
    
    return x_new, y_new


def transformPoints2D(pts, tm=np.identity(3)):
    transformed_pts = []
    for point in pts:
        # Extract x and y from the point
        x, y = point
        
        # Convert (x, y) to homogeneous coordinates (x, y, 1)
        point_homogeneous = np.array([x, y, 1])
        
        # Apply the transformation matrix to the point
        transformed_point = np.dot(tm, point_homogeneous)
        
        # Append the transformed (x, y) coordinates to the result list
        transformed_pts.append((transformed_point[0], transformed_point[1]))
    
    return transformed_pts

def reflection2D(axis, tm=np.identity(3)):
    m = np.identity(3)
    
    if axis == 'x':  # Reflection across the x-axis
        m[1][1] = -1
    elif axis == 'y':  # Reflection across the y-axis
        m[0][0] = -1
    elif axis == 'y=x':  # Reflection across the line y=x
        m[0][0] = 0
        m[0][1] = 1
        m[1][0] = 1
        m[1][1] = 0
    else:
        raise ValueError("Unsupported reflection axis. Choose 'x', 'y', or 'y=x'.")
    
    return np.dot(m, tm)
