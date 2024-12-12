from Animal import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
      super().__init__(nama,makanan,hidup,berkembang_biak)
      self.warna = warna_ikan 
      self.jenis = jenis_ikan

    def cetak_ikan(self):
       super().cetak()
       print(f'warna ikan ini adalah {self.warna} dan hewan ini jenisnya  {self.jenis}')

#object pertama
print('-----object pertama-----')
nemo = ikan('ikan nemo', 'plankton', 'air', 'bertelur', 'kuning jingga', 'air laut')
nemo.cetak_ikan()

#object kedua
print('-----object kedua-----')
mujair = ikan('ikan mujair', 'pakan', 'air', 'bertelur', 'hitam')
mujair.cetak_ikan()