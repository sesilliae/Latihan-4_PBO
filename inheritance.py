class Hewan:

     def __init__(self, nama, warna):
         self.nama = nama     
         self.warna = warna

class Sapi(Hewan):
     def melahirkan(self):
         print("Sapi sedang melahirkan")

binatang = Sapi("Mwoo", "putih")
 
print(binatang.nama)
binatang.melahirkan()