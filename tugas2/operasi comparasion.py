# menentukan perbandingan nilai ujian dan kkm apakah bisa dikatakan lulus atau tidak
# membuat variabel
def nilai_ujian (nilai):
    if nilai >= 75 :
        return 'LULUS'
    else :
        return 'TIDAK LULUS'

# membuat variabel inputan    
nilai_siswa = int(input('Masukkan Nilai : '))

# memanggil fungsi dan menampilkan hasilnya
print('Apakah lulus?', nilai_ujian(nilai_siswa))

