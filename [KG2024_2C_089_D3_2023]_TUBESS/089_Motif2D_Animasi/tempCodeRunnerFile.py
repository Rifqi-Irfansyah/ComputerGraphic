        scaled_circle_points = [tf.scale2D(scale_factor, scale_factor, 0, 0, (x, y)) for x, y in points]
        ret