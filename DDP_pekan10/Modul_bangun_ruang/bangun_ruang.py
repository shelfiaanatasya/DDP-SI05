import math

def kubus(sisi):
    luas = 6 * sisi * sisi
    volume = sisi * sisi * sisi
    print(f'volume kubus {sisi} * {sisi} * {sisi} = {volume}')
    print(f'luas permukaan kubus {6} * {sisi} * {sisi} = {luas}')

def l_balok(panjang, lebar, tinggi):
    luas = 2 * panjang * lebar + panjang * tinggi + lebar * tinggi
    volume = panjang * lebar * tinggi
    print(f'luas permukaan balok {2} * {panjang} * {lebar} + {panjang} * {tinggi} + {lebar} * {tinggi} = {luas}')
    print(f'volume balok {panjang} * {lebar} * {tinggi} = {volume}')

def prisma(l_alas, kel_alas, tinggi ):
    luas = 2 * l_alas + kel_alas * tinggi
    volume = l_alas * tinggi
    print(f'luas permukaan prisma {2} * {l_alas} + {kel_alas} * {tinggi} = {luas}')
    print(f'volume prisma {l_alas} * {tinggi} = {volume}')

def bola(jarijari):
    luas = 4 * 3.14 * jarijari * jarijari
    volume = 4/3 * 3.14 * jarijari * jarijari * jarijari
    print(f'Luas Permukaan Bola {4} * {3.14} * {jarijari} * {jarijari} = {luas}')
    print(f'Volume Bola {4/3} * {3.14} * {jarijari} * {jarijari} * {jarijari} = {volume}')

def tabung(jarijari, tinggi):
    luas = 2 * 3.14 * jarijari * tinggi + 2 * 3.14 * jarijari * jarijari
    volume = 3.14 * jarijari * jarijari * tinggi
    print(f'luas permukaan tabung {2} * {3.14} * {tinggi} + {2} * {3.14} * {jarijari} * {jarijari} = {luas}')
    print(f'Volume tabung {3.14} * {jarijari} * {jarijari} * {tinggi} = {volume}')