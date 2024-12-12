from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
      super().__init__(nama,makanan,hidup,berkembang_biak)
      self.jenis_bulu = jenis_bulu
      self.bunyi = bunyi

    def cetak_burung(self):
      super().cetak()
      print(f'hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}')

#obejct pertama
print('-----object pertama-----')
beo = Burung('Burung Beo', 'biji-bijian', 'udara', 'bertelur', 'biru and orange', 'hallowww')
beo.cetak_burung()

#object kedua
print('-----object kedua-----')
merpati= Burung('Burung merpati', 'biji-bijian', 'darat', 'bertelur', 'putih', 'cicit-cicit')
merpati.cetak_burung()

