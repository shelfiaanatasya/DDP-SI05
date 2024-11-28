#soal1
nama = 'Shelfia Anatasya Dwi Artha'
nim = '0110124019'
rombel = 'SI05'
no_telpon = '085810341491'
alamat = 'Depok, Kelapa Dua'

print('nama saya adalah:', nama)
print('nim saya adalah:', nim)
print('rombel saya adalah:',)
print('no_telpon saya:', no_telpon)
print('alat saya:', alamat)
print('==========')

#soal2
nama = 'Saskia Ramadani'
nim = '0110124114'
rombel = 'SI05'
no_telp = '085778690178'
alamat = 'Depok,Kelapa Dua'

print('nama teman saya adalah;', nama)
print('nim nya aadalah:', nim)
print('rombel:', rombel)
print('alamat:', alamat)
print('============')

#soal3
TB = int(input('masukan tinggi badan :'))
bb_ideal = (TB - 100) - (TB - 100) * 0.1

print('berat badan ideal adalah :',bb_ideal)
print('===========')

#soal4
celcius = int(input("masukan suhu dalam celcius:"))
fahrenheit = (celcius * 9/5) + 32

print(celcius, 'derajat celcius sama dengan', fahrenheit, 'derajat fhrenheit.')
print('=========')

#soal5
phi = 3.14
jari_jari = float(input('masukkan jari-jari tabung:'))
tinggi = float(input('masukkan tinggi tabung:'))

luas_alas = phi * jari_jari * jari_jari 
luas_selimut = 2 * phi * jari_jari * tinggi
luas_permukaan = 2 * phi * luas_alas + luas_selimut
keliling_atas = 2 * phi * jari_jari

print('luas alas tabung:', luas_alas)
print('luas selimut tabung:', luas_selimut)
print('luas permukaan tabung:', luas_permukaan)
print('keliling alas tabung:', keliling_atas)     