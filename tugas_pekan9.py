print('\n--- 1. celcius ke farenheit ---')
def celcius_ke_farenheit(celcius):
    print(celcius* 9/5 + 32)

celcius_ke_farenheit(4)

print('\n--- 2. mencari bilangan genap ---')
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

print('\n--- 3. keterangan lulus dan tidak lulus --')
#rata rata nilai kelulusan 70
def skor(nilai):
    if nilai >= 80:
        print('lulus')
    else:
        print('Gagal')
skor(80)
skor(60)

print('\n--- 4. Mencetak bilangan ganjil ---')
def bil_ganjil(ganjil):
    for i in range(1,ganjil+1, 2):
        print(i, end=' ')
bil_ganjil(20)
