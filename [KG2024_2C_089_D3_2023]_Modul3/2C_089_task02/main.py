class Mobil:
    def __init__(self, nama):
        self.nama = nama

class DaftarMobil:
    def __init__(self):
        self.isi_daftarMobil = ""

    def tambahMobil(self, mobil, merk):
        self.isi_daftarMobil += f"{mobil.nama} - {merk} item(s)\n"

    def tampilDaftarMobil(self):
        return self.isi_daftarMobil.strip()
    

# Membuat objek Mobil
mobil1 = Mobil("Brio")
mobil2 = Mobil("Civic")

# Membuat objek DaftarMobil
daftar = DaftarMobil()
daftar.tambahMobil(mobil1, "Honda")
daftar.tambahMobil(mobil2, "Honda") 

# Menampilkan daftar mobil
print(daftar.tampilDaftarMobil())
