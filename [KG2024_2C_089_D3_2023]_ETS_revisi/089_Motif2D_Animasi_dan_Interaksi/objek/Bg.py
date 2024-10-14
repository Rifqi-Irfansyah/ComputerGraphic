import primitif.line as line
import primitif.basic as basic
import config
import primitif.transformasiv2 as tf
from .cetak_point import cetak_point
from .CustomShape import buat_lingkaran

class Bg:
    def __init__(self, xc, yc,):
        self.xc = xc
        self.yc = yc

    def gambar_bg(self):
        points=[]
        points.extend(line.line_bresenham(self.xc-50, self.yc, self.xc - 46, self.yc + 230))
        points.extend(line.line_bresenham(self.xc-46, self.yc+230, self.xc - 36, self.yc + 230))
        points.extend(line.line_bresenham(self.xc-19, self.yc+180, self.xc - 36, self.yc + 230))
        points.extend(line.line_bresenham(self.xc+40, self.yc, self.xc+17 , self.yc + 70))
        points.extend(buat_lingkaran(self.xc-8, self.yc+180, 10, 0, 90))
        points.extend(buat_lingkaran(self.xc+52, self.yc+90, 40, 300, 360))
        points.extend(buat_lingkaran(self.xc+52, self.yc+90, 40, 0, 30))
        points.extend(line.line_bresenham(self.xc-8, self.yc+170, self.xc+70 , self.yc + 165))
        points.extend(line.line_bresenham(self.xc+65, self.yc+150, self.xc+70 , self.yc + 165))
        points.extend(line.line_bresenham(self.xc+65, self.yc+150, self.xc+40 , self.yc + 145))
        points.extend(line.line_bresenham(self.xc+40, self.yc+140, self.xc+40 , self.yc + 145))
        points.extend(line.line_bresenham(self.xc+32, self.yc+125, self.xc+70 , self.yc + 140))
        points.extend(line.line_bresenham(self.xc+40, self.yc+140, self.xc+70 , self.yc + 140))

        points.extend(line.line_bresenham(self.xc-30, self.yc+120, self.xc-18 , self.yc + 160))     #HURUF A
        points.extend(line.line_bresenham(self.xc-8, self.yc+160, self.xc-18 , self.yc + 160))
        points.extend(line.line_bresenham(self.xc-8, self.yc+160, self.xc-5 , self.yc + 130))
        points.extend(line.line_bresenham(self.xc-29, self.yc+120, self.xc-18 , self.yc + 120))
        points.extend(line.line_bresenham(self.xc-17, self.yc+135, self.xc-14 , self.yc + 145))
        points.extend(line.line_bresenham(self.xc-13, self.yc+135, self.xc-14 , self.yc + 145))
        points.extend(line.line_bresenham(self.xc-17, self.yc+135, self.xc-13 , self.yc + 135))
        points.extend(line.line_bresenham(self.xc-20, self.yc+120, self.xc-17 , self.yc + 130))
        points.extend(line.line_bresenham(self.xc-17, self.yc+130, self.xc-5 , self.yc + 130))
        points.extend(buat_lingkaran(self.xc-15, self.yc+140, 18, 0, 40))
        points.extend(buat_lingkaran(self.xc-15, self.yc+140, 18, 70, 238))
        points.extend(buat_lingkaran(self.xc-15, self.yc+140, 18, 286, 360))
        points.extend(buat_lingkaran(self.xc-15, self.yc+140, 14, 0, 30))
        points.extend(buat_lingkaran(self.xc-15, self.yc+140, 14, 72, 228))
        points.extend(buat_lingkaran(self.xc-15, self.yc+140, 14, 290, 360))
        points.extend(self.gambar_gedung())
        cetak_point(points, config.PURPLE)
        
        pointsb = (self.gambar_gedung())
        tm_reflection_x = tf.reflection2D('y')
        reflected_points_x = tf.transformPoints2D(pointsb, tm_reflection_x)
        cetak_point(reflected_points_x, config.PURPLE)


    def gambar_gedung(self):
        points=[]
        points.extend(line.line_bresenham(self.xc-70, self.yc+30, self.xc-50 , self.yc + 30))
        points.extend(line.line_bresenham(self.xc-70, self.yc+30, self.xc-70 , self.yc + 120))
        points.extend(line.line_bresenham(self.xc-100, self.yc+120, self.xc-70 , self.yc + 120))
        points.extend(line.line_bresenham(self.xc-100, self.yc+120, self.xc-110 , self.yc + 120))
        points.extend(line.line_bresenham(self.xc-110, self.yc+170, self.xc-110 , self.yc + 120))
        points.extend(line.line_bresenham(self.xc-110, self.yc+170, self.xc-150 , self.yc + 170))
        points.extend(line.line_bresenham(self.xc-150, self.yc+30, self.xc-150 , self.yc + 170))

        points.extend(line.line_bresenham(self.xc-150, self.yc+30, self.xc-170 , self.yc + 30))
        points.extend(line.line_bresenham(self.xc-170, self.yc+120, self.xc-170 , self.yc + 30))
        points.extend(basic.segitiga_tanpa_alas(self.xc-190,self.yc+130,40,20))

        points.extend(line.line_bresenham(self.xc-210, self.yc+120, self.xc-210 , self.yc + 150))
        points.extend(basic.segitiga_tanpa_alas(self.xc-230,self.yc+160,40,20))
        points.extend(line.line_bresenham(self.xc-250, self.yc+70, self.xc-250 , self.yc + 150))

        points.extend(line.line_bresenham(self.xc-250, self.yc+70, self.xc-255 , self.yc + 70))
        points.extend(line.line_bresenham(self.xc-255, self.yc+200, self.xc-255 , self.yc + 70))
        points.extend(line.line_bresenham(self.xc-330, self.yc+200, self.xc-255 , self.yc + 200))
        points.extend(line.line_bresenham(self.xc-330, self.yc+200, self.xc-330 , self.yc + 150))

        points.extend(line.line_bresenham(self.xc-350, self.yc+150, self.xc-330 , self.yc + 150))
        points.extend(line.line_bresenham(self.xc-350, self.yc+190, self.xc-350 , self.yc + 150))
        points.extend(line.line_bresenham(self.xc-460, self.yc+190, self.xc-350 , self.yc + 190))

        points.extend(basic.persegi_panjang(self.xc-82,self.yc+100,10, 20))     #KACA
        points.extend(basic.persegi_panjang(self.xc-98,self.yc+100,10, 20))
        points.extend(basic.persegi_panjang(self.xc-98,self.yc+70,10, 20))

        points.extend(basic.persegi_panjang(self.xc-122,self.yc+130,10, 20))
        points.extend(basic.persegi_panjang(self.xc-122,self.yc+100,10, 20))
        points.extend(basic.persegi_panjang(self.xc-138,self.yc+100,10, 20))
        points.extend(basic.persegi_panjang(self.xc-138,self.yc+155,10, 20))

        points.extend(basic.persegi_panjang(self.xc-230,self.yc+130,15, 20))
        points.extend(basic.persegi_panjang(self.xc-230,self.yc+100,15, 20))

        points.extend(basic.persegi_panjang(self.xc-280,self.yc+100,10, 20))
        points.extend(basic.persegi_panjang(self.xc-295,self.yc+125,10, 20))
        points.extend(basic.persegi_panjang(self.xc-265,self.yc+155,10, 20))
        points.extend(basic.persegi_panjang(self.xc-280,self.yc+185,10, 20))
        points.extend(basic.persegi_panjang(self.xc-295,self.yc+185,10, 20))
        points.extend(basic.persegi_panjang(self.xc-310,self.yc+155,10, 20))
        points.extend(basic.persegi_panjang(self.xc-310,self.yc+185,10, 20))

        points.extend(basic.persegi_panjang(self.xc-370,self.yc+175,10, 20))
        points.extend(basic.persegi_panjang(self.xc-385,self.yc+175,10, 20))
        points.extend(basic.persegi_panjang(self.xc-400,self.yc+145,10, 20))
        return points
