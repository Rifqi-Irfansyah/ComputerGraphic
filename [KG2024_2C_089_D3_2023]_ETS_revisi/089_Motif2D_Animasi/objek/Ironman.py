import primitif.basic as basic
import primitif.line as line
import config
from .Animasi import Animasi
from .cetak_point import cetak_point
from .CustomShape import buat_ellipse
from .CustomShape import buat_lingkaran

class Ironman(Animasi):
    points = []
    pointsApi = []
    def __init__(self, xc, yc):
        self.xc = xc
        self.yc = yc

    def anime_translate(self, x, y, api):
        resultpoints = super().translate(x,y, self.points)
        cetak_point(resultpoints, config.RED)

        self.pointsApi = super().scale(1,api, self.xc, self.yc-165, self.pointsApi)
        cetak_point(super().translate(x,y, self.pointsApi), config.BLUE2)

    def gambar_ironman(self, rotate_tangan_kanan, rotate_tangan_kiri):
        points = []
        points.extend(self.gambar_kepala())
        points.extend(self.baju())
        points.extend(self.celana())             
        points.extend(self.sepatu())
        points_tanganKiri = self.tangan_kiri()
        points_tanganKanan = super().rotate(points_tanganKiri, self.xc, self.yc-63, 180)

        points_tanganKiri = super().rotate(points_tanganKiri, self.xc-35, self.yc-60, rotate_tangan_kanan)
        points_tanganKanan = super().rotate(points_tanganKanan, self.xc+35, self.yc-60, -rotate_tangan_kiri)

        points.extend(points_tanganKiri)
        points.extend(points_tanganKanan)

        self.points = points
        self.api()
    
    def api(self):
        self.pointsApi.extend(buat_ellipse(self.xc-22 ,self.yc-153, 10, 30, 20, 153))  
        self.pointsApi.extend(buat_ellipse(self.xc+22 ,self.yc-153, 10, 30, 20, 153))  

        
    def gambar_kepala(self):
        points=[]
        # OUTER
        points.extend(buat_lingkaran(self.xc + 18.8,self.yc + 11.9, 91.5, 0, 27))        # PELIPIS KIRI
        points.extend(buat_lingkaran(self.xc + 18.8,self.yc + 11.9, 91.5, 340, 360))
        points.extend(buat_lingkaran(self.xc -18.8,self.yc + 11.9, 91.5, 180-27, 220))   # PELIPIS KANAN
        points.extend(buat_lingkaran(self.xc + 0,self.yc -7.1, 91.5, 235, 294))          # KEPALA
        points.extend(buat_lingkaran(self.xc + 0.37,self.yc + 14, 72, 300, 340))         # DAGU
        points.extend(buat_lingkaran(self.xc + 0,self.yc + 20, 80, 38, 142))

        # TOPENG
        points.extend(buat_lingkaran(self.xc + 30,self.yc + 11.9, 91.5, 0, 25))
        points.extend(buat_lingkaran(self.xc + 30,self.yc + 11.9, 91.5, 330, 360))
        points.extend(buat_lingkaran(self.xc -30,self.yc + 11.9, 91.5, 180-25, 210))
        points.extend(buat_lingkaran(self.xc + 0,self.yc -20, 91.5, 235, 250))         # HORIZONTAL I
        points.extend(buat_lingkaran(self.xc + 0,self.yc -20, 91.5, 290, 305))         # HORIZONTAL I
        points.extend(buat_lingkaran(self.xc + 0,self.yc -43, 91.5, 255, 284))         # HORIZONTAL II
        points.extend(buat_lingkaran(self.xc + 0,self.yc -60, 91.5, 259, 280))         # HORIZONTAL III
        points.extend(buat_ellipse(self.xc - 87,self.yc -20, 80, 123.5, 210, 232))     # VERTIKAL II
        points.extend(buat_ellipse(self.xc + 87,self.yc -20, 80, 123.5, 308, 330))
        points.extend(buat_ellipse(self.xc -30,self.yc + 40, 122, 89, 130, 139))       # HORIZONTAL IV
        points.extend(buat_ellipse(self.xc + 30,self.yc + 40, 122, 89, 39, 48))        # HORIZONTAL IV
        points.extend(buat_ellipse(self.xc -75,self.yc + 0, 122, 89, 145, 159))        # VERTIKAL III
        points.extend(buat_ellipse(self.xc + 75,self.yc + 0, 122, 89, 19, 35))         # VERTIKAL III

        # WAJAH
        points.extend(basic.trapesium_tanpa_alas(self.xc + 0,self.yc -53, 25, 35, 10)) # MULUT
        points.extend(buat_ellipse(self.xc + 0,self.yc + 60, 101, 62, 49, 180-49))     # ALIS
        points.extend(buat_lingkaran(self.xc + 48,self.yc + 0, 10, 90, 220))           # MATA KANAN
        points.extend(buat_ellipse(self.xc + 40,self.yc -3, 23, 7, 0, 120))            
        points.extend(buat_ellipse(self.xc + 40,self.yc -3, 23, 7, 340, 360))            
        points.extend(buat_lingkaran(self.xc - 48,self.yc + 0, 10, 300, 360))          # MATA KIRI
        points.extend(buat_lingkaran(self.xc - 48,self.yc + 0, 10, 0, 90))
        points.extend(buat_ellipse(self.xc - 40,self.yc -3, 23, 7, 55, 190))            
        points.extend(buat_ellipse(self.xc - 65,self.yc + 4, 24, 25, 60, 80))          #TELINGA KIRI BAWAH           
        points.extend(buat_ellipse(self.xc - 65,self.yc + 4, 24, 25, 288, 310))        #ATAS
        points.extend(buat_ellipse(self.xc - 75,self.yc + 10, 8, 19, 0, 20))           #TENGAH 
        points.extend(buat_ellipse(self.xc - 75,self.yc + 10, 8, 19, 313, 360))             
        points.extend(buat_ellipse(self.xc - 75,self.yc , 8, 19, 0, 80))                              
        points.extend(buat_ellipse(self.xc - 75,self.yc , 8, 19, 330, 360))                

        points.extend(buat_ellipse(self.xc + 65,self.yc + 4, 24, 25, 90, 110))         #TELINGA KANAN BAWAH
        points.extend(buat_ellipse(self.xc + 65,self.yc + 4, 24, 25, 231, 253))        #ATAS
        points.extend(buat_ellipse(self.xc + 75,self.yc + 10, 8, 19, 145, 236))        #TENGAH 
        points.extend(buat_ellipse(self.xc + 75,self.yc, 8, 19, 80, 185))
        return points
        
    
    def baju(self):
        points=[]
        points.extend(basic.trapesium_tanpa_alas(self.xc + 0,self.yc -83, 50, 75, 50))
        points.extend(buat_ellipse(self.xc ,self.yc-92, 80, 19, 48, 180-49))            
        points.extend(buat_lingkaran(self.xc ,self.yc-80, 10, 0, 360))
        points.extend(buat_lingkaran(self.xc ,self.yc-80, 20, 30, 150))
        points.extend(buat_lingkaran(self.xc-35 ,self.yc-100, 20, 210, 255))
        points.extend(buat_lingkaran(self.xc-35 ,self.yc-112, 20, 228, 258))
        points.extend(buat_lingkaran(self.xc+35 ,self.yc-100, 20, 285, 320))
        points.extend(buat_lingkaran(self.xc+35 ,self.yc-112, 20, 278, 320))  
        points.extend(line.line_bresenham(self.xc + 12 , self.yc - 97, self.xc + 12, self.yc - 110))
        points.extend(line.line_bresenham(self.xc - 12 , self.yc - 97, self.xc - 12, self.yc - 110))
        points.extend(buat_lingkaran(self.xc ,self.yc-87, 20, 50, 126))
        points.extend(buat_lingkaran(self.xc ,self.yc-107, 12, 20, 159))
        return points

    
    def celana(self):
        points=[]
        points.extend(line.line_bresenham(self.xc + 38 , self.yc - 110, self.xc + 36, self.yc - 150))
        points.extend(line.line_bresenham(self.xc + 6 , self.yc - 130, self.xc + 8, self.yc - 150))
        points.extend(line.line_bresenham(self.xc - 38 , self.yc - 110, self.xc - 36, self.yc - 150))
        points.extend(line.line_bresenham(self.xc - 6 , self.yc - 130, self.xc - 8, self.yc - 150))
        points.extend(buat_lingkaran(self.xc ,self.yc-130, 5, 180, 360))
        points.extend(buat_lingkaran(self.xc-30, self.yc-162, 40, 230, 280))
        points.extend(buat_lingkaran(self.xc+30, self.yc-162, 40, 258, 308))
        points.extend(buat_lingkaran(self.xc-22, self.yc-140, 5, 0, 360))
        points.extend(buat_lingkaran(self.xc+22, self.yc-140, 5, 0, 360))
        return points

    def sepatu(self):
        points=[]
        points.extend(buat_ellipse(self.xc-22 ,self.yc-153, 15, 6, 0, 190))  
        points.extend(buat_ellipse(self.xc-22 ,self.yc-153, 15, 6, 340, 360))  
        points.extend(buat_ellipse(self.xc-22 ,self.yc-148, 15, 6, 0, 180))  
        points.extend(buat_ellipse(self.xc+22 ,self.yc-153, 15, 6, 0, 190))  
        points.extend(buat_ellipse(self.xc+22 ,self.yc-153, 15, 6, 340, 360))
        points.extend(buat_ellipse(self.xc+22 ,self.yc-148, 15, 6, 0, 180))  
        return points

    def tangan_kiri(self):
        points=[]
        points.extend(buat_lingkaran(self.xc-35 ,self.yc-63, 8, 110, 250))
        points.extend(buat_ellipse(self.xc-70 ,self.yc-63, 50, 9, 55, 157))  
        points.extend(buat_ellipse(self.xc-70 ,self.yc-61, 50, 9, 205, 305))  
        points.extend(buat_lingkaran(self.xc-85 ,self.yc-62, 10, 0, 90))
        points.extend(buat_lingkaran(self.xc-85 ,self.yc-62, 10, 270, 360))
        points.extend(buat_lingkaran(self.xc-77 ,self.yc-62, 10, 0, 90))
        points.extend(buat_lingkaran(self.xc-77 ,self.yc-62, 10, 270, 360))

        points.extend(buat_lingkaran(self.xc-40 ,self.yc-62, 15, 313, 360))
        points.extend(buat_lingkaran(self.xc-40 ,self.yc-62, 15, 313, 360))
        points.extend(buat_lingkaran(self.xc-30 ,self.yc-62, 15, 313, 360))
        points.extend(buat_lingkaran(self.xc-30 ,self.yc-62, 15, 313, 360))

        points.extend(buat_lingkaran(self.xc-40 ,self.yc-62, 15, 0, 38))
        points.extend(buat_lingkaran(self.xc-30 ,self.yc-62, 15, 0, 38))
        return points
