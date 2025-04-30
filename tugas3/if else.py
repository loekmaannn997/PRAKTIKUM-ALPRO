# membuat studi kasus menentukan apakah anda layak menonton film di atas 18 tahun apa tidak
print('='*30)
print('1. Rudie Habibi')
print('2. The Raid 2')
print('3. Susah Sinyal')
print('4. Suster Keramas')
print('='*30)

# variabel usia
film = input('Pilih Film Di Atas : ')
usia = int(input('Masukkan Usia Anda : '))

# kondisi
if usia > 17 :
    print('Selamat Menonton')
else:
    print('Anda Tidak Boleh menonton Film Ini Karena Usia Di Bawah 17 Tahun. Silahkan Pilih Film Lainnya!')