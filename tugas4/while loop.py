# membuat studi kasus menginputkan data mahasiswa dengan menggunakan while loop

# variabel ulang
ulang = True
# proses perulangannya
while ulang:
    nama = input('Masukkan Nama Kamu \t:')
    nim = input('Masukkan NIM Kamu \t:')
    matkul = input('Masukkan Matkul \t:')
# hasil    
    print('==============================')
    print('Nama \t:', (nama))
    print('NIM \t:', (nim))
    print('Matkul \t:', (matkul))
    ulang = input('Lanjut menginputkan data? y/t?')
    if ulang == 't':
        print('Program Selesai')
        ulang = False


     
       