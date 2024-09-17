import py5
import math
import numpy as np
import primitif.transformasiv2 as tf  # Pastikan ini mengacu pada modul yang memiliki fungsi transformasi
import primitif.basic as basic
import config

# Global angle for rotation animation
angle = 0

class Bunga:
    def __init__(self, xc, yc, radius_lingkaran, jumlah_kelopak, pattern):
        self.xc = xc  # Pusat bunga (x)
        self.yc = yc  # Pusat bunga (y)
        self.radius_lingkaran = radius_lingkaran  # Radius lingkaran yang menjadi dasar kelopak
        self.jumlah_kelopak = jumlah_kelopak  # Jumlah kelopak bunga
        self.pattern = pattern  # Pola atau warna kelopak

    def kelopak_bunga(self, Rx, Ry):
        angle_step = 360 / self.jumlah_kelopak
        for i in range(self.jumlah_kelopak):
            angle_radians = math.radians(i * angle_step)
            kelopak_x = self.xc + self.radius_lingkaran * math.cos(angle_radians)
            kelopak_y = self.yc + self.radius_lingkaran * math.sin(angle_radians)
            
            py5.push_matrix()
            py5.translate(kelopak_x, kelopak_y)
            py5.rotate(angle_radians + math.radians(angle))  # Rotasi kelopak
            basic.draw_ellipse(0, 0, Rx * 2, Ry * 2, self.pattern)  # Menggambar kelopak bunga
            py5.pop_matrix()

def setup():
    py5.size(400, 400)
    py5.no_stroke()
    py5.frame_rate(60)

# Fungsi untuk menggambar kelopak bunga secara animasi
def draw():
    global angle

    py5.background(255)
    
    # Objek bunga
    py5.stroke(*config.MAGENTA)
    bunga = Bunga(200, 200, 100, 6, "solid")  # Bunga dengan 6 kelopak
    
    # Menggambar bunga dan memberikan rotasi pada setiap kelopak
    bunga.kelopak_bunga(20, 40)  # Ukuran Rx dan Ry untuk kelopak
    
    # Update angle untuk rotasi animasi
    angle += 1  # Mengatur kecepatan rotasi

py5.run_sketch()
