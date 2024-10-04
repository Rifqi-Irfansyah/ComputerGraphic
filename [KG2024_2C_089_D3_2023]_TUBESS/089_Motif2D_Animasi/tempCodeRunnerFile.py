    translated_points = []

        for x, y in points:
            # Menghitung titik yang ditranslasi
            transformed_point = tf.translate2D(tx, ty, np.array([[x], [y], [1]]))

            # Ambil x dan y dari transformed_point
            x_translated = transformed_point[0, 0]  # Pastikan ini adalah skalar
            y_translated = transformed_point[1, 0]  # Pastikan ini adalah skalar

            translated_points.append((x_translated, y_translated))

        return translated_points
