import py5
import primitif.line
import primitif.basic as basic
import primitif.utility
import math
import config
    
class Garis:
    def __init__(self, warna, tebal):
        self.warna = warna
        self.tebal = tebal

    def apply_stroke(self):
        py5.stroke(self.warna[0], self.warna[1], self.warna[2])
        py5.stroke_weight(self.tebal)


class Bunga:
    def __init__(self, xc, yc, radius_lingkaran, jumlah_kelopak, color, pattern):
        self.xc = xc
        self.yc = yc
        self.radius_lingkaran = radius_lingkaran
        self.jumlah_kelopak = jumlah_kelopak
        self.pattern = pattern
        self.color = color

    def lingkaran_tengah(self):
        basic.draw_circle(self.xc, self.yc, self.radius_lingkaran, self.pattern)

    def kelopak_bunga(self, Rx, Ry):
        angle_step = 360 / self.jumlah_kelopak
        for i in range(self.jumlah_kelopak):
            angle = math.radians(i * angle_step)
            kelopak_x = self.xc + self.radius_lingkaran * math.cos(angle)
            kelopak_y = self.yc + self.radius_lingkaran * math.sin(angle)
            py5.push_matrix()
            py5.translate(kelopak_x, kelopak_y)
            py5.rotate(angle)
            basic.draw_ellipse(0, 0, Rx * 2, Ry * 2, self.pattern)
            py5.pop_matrix()

    def gambar_bunga(self):
        py5.stroke(*self.color)
        self.kelopak_bunga(self.radius_lingkaran, self.radius_lingkaran // 2)
        self.lingkaran_tengah()

margin = 25
def setup():
    py5.size(config.WIDTH, config.HEIGHT)
    py5.background(255)

def draw():
    primitif.basic.draw_margin(py5.width, py5.height, margin, c=[0,0,0,255])
    primitif.basic.draw_kartesian(py5.width, py5.height, margin, c=[0,0,0,255])
    
    py5.translate(config.WIDTH /2, config.HEIGHT / 2)
    py5.scale(1, -1)
    x = (config.WIDTH-margin)/4 -margin/2
    y = (config.HEIGHT-margin)/4 -margin/2

    bunga1 = Bunga(x, y, 40, 4, config.GREEN, "solid")
    bunga1.gambar_bunga()
    
    bunga2 = Bunga(-x, y, 40, 5, config.BLUE, "dotted")
    bunga2.gambar_bunga()
    
    bunga2 = Bunga(-x, -y, 40, 7, config.MAGENTA, "dotted_striped")
    bunga2.gambar_bunga()
    
    bunga2 = Bunga(x, -y, 40, 8, config.PURPLE, "dashed")
    bunga2.gambar_bunga()
        

py5.run_sketch()

