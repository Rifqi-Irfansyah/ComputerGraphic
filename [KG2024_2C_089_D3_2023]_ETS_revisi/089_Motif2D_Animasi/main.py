import py5
import primitif.basic as basic
import config
from objek.Ironman import Ironman
from objek.Gunungan import Gunungan
from objek.Pesawat import Pesawat
from objek.Bg import Bg
from objek.cetak_point import cetak_point

margin = 20
x = 1
rotate = 1
pesawat = 1
tangan = 1
tangan2 = 1
ironman = 1
ironman2 = 1
api = 0

def gerakan_gunungan():
    global rotate,x
    x += 1.5
    if(x <= 60):
        rotate += 1.5
    elif(x <= 120):
        rotate -= 1.5
    else:
        x = 1
        rotate = 1

def gerakan_pesawat():
    global pesawat
    pesawat += 1.5
    if(pesawat >= 230):
        pesawat = 1

def gerakan_tangan():
    global tangan, tangan2
    tangan2 += 1.5
    if tangan2 <=65:
        tangan += 1.5
    elif tangan2 <= 130:
        tangan -= 1.5
    else:
        tangan2 = 1

def gerakan_ironman():
    global ironman, ironman2, api
    ironman2 += 1
    if ironman2 <= 43:
        ironman += 1
    elif ironman2 <= 86:
        ironman -= 1
    else:
        ironman2 = 1 

    if ironman2 <= 15:
        api += 0.15
    elif ironman2 <= 71:
        if ironman2 % 2 == 0:
            api += 0.2
        else:
            api -= 0.2
    elif ironman2 <= 86:
        api -= 0.15

def setup():
    py5.size(config.WIDTH, config.HEIGHT)

def draw():    
    py5.background(255)
    cetak_point(basic.draw_margin(py5.width, py5.height, margin))    
    py5.translate(config.WIDTH /2, config.HEIGHT / 2)
    py5.scale(1, -1)
    
    gerakan_gunungan()                                                           # OBJEK GUNUNGAN
    obj_gunungan = Gunungan(-config.WIDTH/4-180,+150)
    obj_gunungan.gambar_gunungan()
    obj_gunungan.anime_rotate(-rotate)

    obj_gunungan = Gunungan(config.WIDTH/4+180,+150)
    obj_gunungan.gambar_gunungan()
    obj_gunungan.anime_rotate(rotate)

    gerakan_pesawat()                                                           # OBJEK PESAWAT
    obj_pesawat = Pesawat(config.WIDTH/2+2*margin,config.HEIGHT/2.5)
    obj_pesawat.gambar_pesawat()
    obj_pesawat.anime_translate(-5*pesawat)

    obj_bg = Bg(0, -config.HEIGHT/2+margin)                                     # OBJEK BACKGROUND
    obj_bg.gambar_bg()

    gerakan_ironman()                                                           # OBJEK IRONMAN
    gerakan_tangan()
    obj_ironman = Ironman(0,100)
    obj_ironman.gambar_ironman(tangan, tangan)
    obj_ironman.anime_translate(0, ironman, api)

py5.run_sketch()
