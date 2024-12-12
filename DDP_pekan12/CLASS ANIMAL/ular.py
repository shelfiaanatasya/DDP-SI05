from Animal import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_ular, warna_ular ):
      super().__init__(nama,makanan,hidup,berkembang_biak)
      self.jenis = jenis_ular 
      self.warna = warna_ular

    def cetak_ular(self):
       super().cetak()
       print(f'jenis ikan ini adalah {self.jenis} dan hewan ini berwarna {self.warna}')

#object pertama
print('-----object pertama-----')
beludak = ular('beludak', 'reptil', 'air', 'bertelur', 'berbisa', 'cokelat kuning terang')
beludak.cetak_ular()

#object kedua
print('-----object kedua-----')
taipan = ular('taipan', 'reptil', 'air', 'bertelur', 'berbisa', 'kuning pucat')
taipan.cetak_ular()