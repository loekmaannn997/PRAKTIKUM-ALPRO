# studi kasus menentukan nilai siswa dan grade yang diperoleh dari setiap siswa

#variabel
nilai = 0
grade = "E"

# menggunakan materi elif
nilai = int(input('masukan nilai : '))
if(nilai >= 90):
    grade = 'A'
elif(nilai >= 75):
    grade = 'B'
elif(nilai >= 65):
    grade = 'C'
elif(nilai >= 55):
    grade = 'D'
elif(nilai >= 50):
    grade = 'E'

# menampilkan hasilnya
print(f'grade anda = {grade}')