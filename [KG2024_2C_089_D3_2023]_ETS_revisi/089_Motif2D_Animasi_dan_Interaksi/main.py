import py5
import primitif.line as line
import config
from objek.Ironman import Ironman
from objek.Gunungan import Gunungan
from objek.Pesawat import Pesawat
from objek.Bg import Bg
from objek.cetak_point import cetak_point

def setup():
    py5.size(config.WIDTH, config.HEIGHT)

x = 1
margin = 20
rotate = 1
tangan = 1
tangan2 = 1
ironman = 1
ironman2 = 1
api = 2
pesawat = 1
speed_pesawat = 1.5
interaksi_pesawwat = 1
speed_rotate = 1

def gerakan_gunungan(speed):
    global rotate,x
    x += speed
    if(x <= 60):
        rotate += speed
    elif(x <= 120):
        rotate -= speed
    else:
        x = 1
        rotate = 1

def gerakan_pesawat():
    global pesawat, speed_pesawat
    pesawat += speed_pesawat
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
    
    if ironman2 % 2 == 0:
        api += 0.2
    else:
        api -= 0.2
    


def interaksi_guide():
    py5.fill(000)
    x = py5.width/2-margin
    y = -py5.height/2 + margin+50
    cetak_point(line.line_bresenham(-x , y, x , y))
    py5.scale(1, -1)
    py5.text_size(15)
    py5.text('Kecepatan Gunungan = '+str(speed_rotate), -x+10, -y+15)
    py5.text('Tekan O : Menaikkan Kecepatan Gunungan', -x+10, -y+34)
    py5.text('Tekan P : Menurunkan Kecepatan Gunungan', -x+10, -y+50)

    py5.text('Kecepatan Pesawat = '+str(speed_pesawat), -150, -y+15)
    py5.text('Tekan K : Menaikkan Kecepatan Pesawat', -150, -y+34)
    py5.text('Tekan L : Menurunkan Kecepatan Pesawat', -150, -y+50)

    py5.text('Tekan W A S D : Menjalankan Ironman', 150, -y+15)
    py5.scale(1, -1)


varIronmanX = 0
varIronmanY = 0
def key_pressed():
    global speed_rotate, varIronmanX, varIronmanY, speed_pesawat
    if py5.key == 'o' or py5.key == 'O':
        speed_rotate += 1
    elif py5.key == 'p' or py5.key == 'P':
        if(speed_rotate >= 1):
            speed_rotate -= 1

    if py5.key == 'k' or py5.key == 'K':
        speed_pesawat += 1
    elif py5.key == 'l' or py5.key == 'L':
        if(speed_pesawat >= 1):
            speed_pesawat -= 1

    if (py5.key == 'w' or py5.key == 'W'):
        varIronmanY += 1.5
    if (py5.key == 's' or py5.key == 'S'):
        varIronmanY -= 1.5
    if (py5.key == 'a' or py5.key == 'A'):
        varIronmanX -= 1.5
    if (py5.key == 'd' or py5.key == 'D'):
        varIronmanX += 1.5

def draw():    
    global interaksi_pesawwat
    py5.background(255)
    py5.translate(config.WIDTH /2, config.HEIGHT / 2)
    py5.scale(1, -1)

    height_guide = 50
    interaksi_guide()
    
    gerakan_gunungan(speed_rotate)                                              # OBJEK GUNUNGAN
    obj_gunungan = Gunungan(-config.WIDTH/4-180,+150 + height_guide)
    obj_gunungan.gambar_gunungan()
    obj_gunungan.anime_rotate(-rotate)

    obj_gunungan = Gunungan(config.WIDTH/4+180,+150 + height_guide)
    obj_gunungan.gambar_gunungan()
    obj_gunungan.anime_rotate(rotate)

    gerakan_pesawat()                                                           # OBJEK PESAWAT
    obj_pesawat = Pesawat(config.WIDTH/2+2*margin,config.HEIGHT/2.5)
    obj_pesawat.gambar_pesawat()
    obj_pesawat.anime_translate(-5*pesawat)

    obj_bg = Bg(0, -config.HEIGHT/2+margin + height_guide)                      # OBJEK BACKGROUND
    obj_bg.gambar_bg()

    gerakan_ironman()                                                           # OBJEK IRONMAN
    gerakan_tangan()
    obj_ironman = Ironman(0,100 + height_guide)
    obj_ironman.gambar_ironman(tangan, tangan)
    obj_ironman.anime_translate(varIronmanX, varIronmanY, api)

py5.run_sketch()
