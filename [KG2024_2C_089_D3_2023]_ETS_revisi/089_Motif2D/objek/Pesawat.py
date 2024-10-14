import py5
from .cetak_point import cetak_point
from .CustomShape import buat_ellipse
from .CustomShape import buat_lingkaran

class Pesawat:
    def __init__(self, xc, yc,):
        self.xc = xc
        self.yc = yc
        self.points=[]
    
    def gambar_pesawat(self):
        points=[]
        points.extend(buat_ellipse(self.xc,self.yc, 102, 18, 0, 64))             
        points.extend(buat_ellipse(self.xc,self.yc, 102, 18, 85, 175))             
        points.extend(buat_ellipse(self.xc,self.yc, 102, 18, 235, 285))             
        points.extend(buat_ellipse(self.xc,self.yc, 102, 18, 331, 360))             
        points.extend(buat_ellipse(self.xc+30,self.yc, 102, 18, 225, 260))   
        points.extend(buat_lingkaran(self.xc-110, self.yc, 25, 155, 203))

        points.extend(buat_ellipse(self.xc-50,self.yc+25, 37, 18, 40, 160))             
        points.extend(buat_ellipse(self.xc-50,self.yc+11, 37, 18, 196, 280))             
        points.extend(buat_ellipse(self.xc-36,self.yc+13, 37, 18, 300, 360))

        points.extend(buat_lingkaran(self.xc+65, self.yc+22, 103, 15, 46))      #SAYAP
        points.extend(buat_lingkaran(self.xc+91, self.yc+18, 103, 12, 40))
        points.extend(buat_ellipse(self.xc-5,self.yc-20, 56, 19, 280, 315))
        points.extend(buat_ellipse(self.xc-40,self.yc-40, 56, 19, 142, 165))

        points.extend(buat_ellipse(self.xc+104,self.yc+4, 25, 28, 300, 330))
        points.extend(buat_ellipse(self.xc+124,self.yc+4, 25, 28, 315, 360))
        points.extend(buat_ellipse(self.xc+124,self.yc+4, 25, 28, 0, 22))
        points.extend(buat_ellipse(self.xc+54,self.yc+15, 56, 19, 192, 213))
        self.points = points
        cetak_point(self.points)