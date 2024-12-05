import math

def lk_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'Luas Persegi {sisi} * {sisi} = {luas}')
    print(f'Keliling Persegi adalah {keliling}')

def lk_persegi_panjang(panjang, lebar):
    luas = panjang * lebar 
    keliling = 2 * panjang * lebar 
    print(f'hasil luas persegi panjang dari', panjang, 'x', lebar, '=', luas)
    print(f'keliling persegi panjang adalah {2} * {panjang} * {lebar} = {keliling}')

def l_segitiga(alas, tinggi, sisi1=0, sisi2=0, sisi3=0):
    luas = 1/2 * alas * tinggi 
    print(f'Luas Segitiga {1/2} * {alas} * {tinggi} = {luas}')

def l_lingkaran(r1, r2,):
    luas = 3.14 * r1 * r2
    print(f'Luas Lingkaran ini adalah phi * {r1} * {r2} = {luas}')

def l_j_genjang(alas, tinggi):
    luas = alas * tinggi 
    keliling =  2 * alas + tinggi
    print(f'Luas Jajar Genjang {alas} * {tinggi} = {luas} = {luas}')
    print(f'keliling jajar genjang {2} * {alas} + {tinggi} = {keliling}')
