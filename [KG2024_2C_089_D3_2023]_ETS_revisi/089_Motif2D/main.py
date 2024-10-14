import py5
import primitif.basic as basic
import config
from objek.Ironman import Ironman
from objek.Gunungan import Gunungan
from objek.Pesawat import Pesawat
from objek.Bg import Bg
from objek.cetak_point import cetak_point

margin = 20
def setup():
    py5.size(config.WIDTH, config.HEIGHT)

def draw():
    py5.background(255)
    points=[]
    points.extend(basic.draw_margin(py5.width, py5.height, margin))

    cetak_point(points)
    py5.fill(000)
    py5.translate(config.WIDTH /2, config.HEIGHT / 2)
    py5.scale(1, -1)
    
    
    obj_gunungan = Gunungan(-config.WIDTH/4-100,+150)
    obj_gunungan.gambar_gunungan()

    obj_gunungan = Gunungan(config.WIDTH/4+100,+150)
    obj_gunungan.gambar_gunungan()

    obj_pesawat = Pesawat(config.WIDTH/4,config.HEIGHT/2.5)
    obj_pesawat.gambar_pesawat()

    obj_bg = Bg(0, -config.HEIGHT/2+margin)
    obj_bg.gambar_bg()
    
    obj_ironman = Ironman(0,100)
    obj_ironman.gambar_ironman()

py5.run_sketch()
