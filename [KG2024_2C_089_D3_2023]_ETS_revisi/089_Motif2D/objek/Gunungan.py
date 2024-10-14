# import py5
import primitif.basic as basic
import primitif.line as line
import config
from .cetak_point import cetak_point
from .CustomShape import buat_lingkaran

class Gunungan:
    def __init__(self, xc, yc):
        self.xc = xc
        self.yc = yc
        self.points=[]

    def gambar_gunungan(self):
        points=[]
        points.extend(basic.segitiga_tanpa_alas(self.xc + 0,self.yc -53, 100,100))
        points.extend(buat_lingkaran(self.xc + 25,self.yc-110 + 0, 25, 125, 192))      #LEKUKAN ATAS KANAN
        points.extend(buat_lingkaran(self.xc - 25,self.yc-110 + 0, 25, 345, 360))      #KIRI
        points.extend(buat_lingkaran(self.xc - 25,self.yc-110 + 0, 25, 0, 48))

        points.extend(buat_lingkaran(self.xc + 55,self.yc-142 + 0, 20, 0, 35))         #LEKUKAN BAWAH KANAN
        points.extend(buat_lingkaran(self.xc + 55,self.yc-142 + 0, 20, 322, 360)) 
        points.extend(buat_lingkaran(self.xc - 55,self.yc-142 + 0, 20, 142, 215))      #KIRI
        points.extend(line.line_bresenham(self.xc + 160 - 200, self.yc - 155, self.xc + 40, self.yc - 155))
        points.extend(line.line_bresenham(self.xc + 204 - 200, self.yc - 155, self.xc + 4, self.yc - 200))
        points.extend(line.line_bresenham(self.xc + 196 - 200, self.yc - 155, self.xc - 4, self.yc - 200))
        points.extend(buat_lingkaran(self.xc ,self.yc-200 + 0, 4, 0, 180))
        points.extend(self.gambar_motif())
        self.points = points
        cetak_point(self.points, config.BROWN)

    def gambar_motif(self):
        points=[]
        points.extend(line.line_bresenham(self.xc, self.yc - 4, self.xc, self.yc - 155))
        points.extend(buat_lingkaran(self.xc - 10, self.yc - 42, 7, 0, 55))              # KIRI
        points.extend(buat_lingkaran(self.xc - 10, self.yc - 42, 7, 210, 360))
        points.extend(buat_lingkaran(self.xc - 7, self.yc - 40, 3, 0, 160))
        points.extend(buat_lingkaran(self.xc + 10, self.yc - 42, 7, 90, 330))            # KANAN
        points.extend(buat_lingkaran(self.xc + 7, self.yc - 40, 3, 330, 360))
        points.extend(buat_lingkaran(self.xc + 7, self.yc - 40, 3, 0, 120))

        points.extend(buat_lingkaran(self.xc - 5, self.yc - 27, 5, 180, 360))            # KIRI
        points.extend(buat_lingkaran(self.xc - 6, self.yc - 27, 3, 0, 200))
        points.extend(buat_lingkaran(self.xc + 5, self.yc - 27, 5, 180, 360))            # KANAN
        points.extend(buat_lingkaran(self.xc + 6, self.yc - 27, 3, 0, 180))
        points.extend(buat_lingkaran(self.xc + 6, self.yc - 27, 3, 330, 360))

        points.extend(buat_lingkaran(self.xc - 11, self.yc - 60, 10, 180, 315))           # KIRI
        points.extend(buat_lingkaran(self.xc - 13, self.yc - 58, 7, 270, 360))               
        points.extend(buat_lingkaran(self.xc - 13, self.yc - 58, 7, 0, 120))               
        points.extend(buat_lingkaran(self.xc - 10, self.yc - 61, 3, 90, 270))
        points.extend(buat_lingkaran(self.xc + 11, self.yc - 60, 10, 225, 360))           # KANAN
        points.extend(buat_lingkaran(self.xc + 13, self.yc - 58, 7, 30, 210))               
        points.extend(buat_lingkaran(self.xc + 10, self.yc - 61, 3, 0, 90))               
        points.extend(buat_lingkaran(self.xc + 10, self.yc - 61, 3, 270, 360))

        points.extend(buat_lingkaran(self.xc - 20, self.yc - 70, 7, 0, 230))              # KIRI
        points.extend(buat_lingkaran(self.xc - 20, self.yc - 70, 7, 330, 360))
        points.extend(buat_lingkaran(self.xc - 23, self.yc - 70, 4, 270, 360))
        points.extend(buat_lingkaran(self.xc + 20, self.yc - 70, 7, 310, 360))            # KANAN
        points.extend(buat_lingkaran(self.xc + 20, self.yc - 70, 7, 0, 160))
        points.extend(buat_lingkaran(self.xc + 23, self.yc - 70, 4, 180, 270))

        points.extend(buat_lingkaran(self.xc - 10, self.yc - 85, 7, 200, 360))            # KIRI
        points.extend(buat_lingkaran(self.xc - 10, self.yc - 85, 7, 0, 22))
        points.extend(buat_lingkaran(self.xc - 6, self.yc - 84, 3, 0, 190))
        points.extend(buat_lingkaran(self.xc + 10, self.yc - 85, 7, 128, 340))            # KANAN
        points.extend(buat_lingkaran(self.xc + 6, self.yc - 84, 3, 0, 180))
        points.extend(buat_lingkaran(self.xc + 6, self.yc - 84, 3, 350, 360))

        points.extend(buat_lingkaran(self.xc - 39, self.yc - 92, 6, 0, 130))             # KIRI
        points.extend(buat_lingkaran(self.xc + 39, self.yc - 92, 6, 50, 180))             # KANAN

        points.extend(buat_lingkaran(self.xc - 20, self.yc - 110, 20, 180, 315))         # KIRI
        points.extend(buat_lingkaran(self.xc - 26, self.yc - 102, 10, 270, 360))               
        points.extend(buat_lingkaran(self.xc - 26, self.yc - 102, 10, 0, 120))               
        points.extend(buat_lingkaran(self.xc - 22, self.yc - 106, 5, 90, 270))               
        points.extend(buat_lingkaran(self.xc - 20, self.yc - 115, 5, 70, 230))                       
        points.extend(buat_lingkaran(self.xc + 20, self.yc - 110, 20, 225, 360))         # KANAN
        points.extend(buat_lingkaran(self.xc + 26, self.yc - 102, 10, 30, 210))
        points.extend(buat_lingkaran(self.xc + 22, self.yc - 106, 5, 270, 360))                       
        points.extend(buat_lingkaran(self.xc + 22, self.yc - 106, 5, 0, 40))                       
        points.extend(buat_lingkaran(self.xc + 20, self.yc - 115, 5, 0, 110))                       
        points.extend(buat_lingkaran(self.xc + 20, self.yc - 115, 5, 270, 360)) 

        points.extend(buat_lingkaran(self.xc - 100, self.yc - 100, 100, 162, 180))      # KIRI
        points.extend(buat_lingkaran(self.xc - 10, self.yc - 125, 7, 30, 180))
        points.extend(buat_lingkaran(self.xc - 13, self.yc - 128, 3, 180, 360))
        points.extend(buat_lingkaran(self.xc + 100, self.yc - 100, 100, 0, 18))         # KANAN
        points.extend(buat_lingkaran(self.xc + 10, self.yc - 125, 7, 0, 150))
        points.extend(buat_lingkaran(self.xc + 13, self.yc - 128, 3, 180, 360))

        points.extend(buat_lingkaran(self.xc + 22, self.yc - 102, 25, 70, 190))      # KIRI
        points.extend(buat_lingkaran(self.xc - 22, self.yc - 102, 25, 0, 110))       # KANAN
        points.extend(buat_lingkaran(self.xc - 22, self.yc - 102, 25, 350, 360))
        points.extend(buat_lingkaran(self.xc + 18, self.yc - 105, 30, 110, 180))     # KIRI
        points.extend(buat_lingkaran(self.xc + 30, self.yc - 158, 25, 274, 325))
        points.extend(buat_lingkaran(self.xc - 18, self.yc - 105, 30, 0, 70))        # KANAN
        points.extend(buat_lingkaran(self.xc - 30, self.yc - 158, 25, 215, 274))
        points.extend(buat_lingkaran(self.xc - 26, self.yc - 115, 30, 68, 118))     # KIRI
        points.extend(buat_lingkaran(self.xc + 26, self.yc - 115, 30, 58, 108))  


        points.extend(basic.persegi_panjang(self.xc, self.yc-138, 20, 10))
        points.extend(line.line_bresenham(self.xc - 30, self.yc-154, self.xc - 10, self.yc - 143)) # HORIZONTAL
        points.extend(line.line_bresenham(self.xc - 15, self.yc-154, self.xc - 3, self.yc - 143))
        points.extend(line.line_bresenham(self.xc + 30, self.yc-154, self.xc + 10, self.yc - 143))
        points.extend(line.line_bresenham(self.xc + 15, self.yc-154, self.xc + 3, self.yc - 143))
        points.extend(line.line_bresenham(self.xc - 17, self.yc-147, self.xc + 17, self.yc - 147))  #VERTIKAL
        points.extend(line.line_bresenham(self.xc - 23, self.yc-151, self.xc + 23, self.yc - 151))  #VERTIKAL
        return points
