# studi kasus menghitung gaji karyawan
print('========== RINCIAN GAJI ==========')
print('GAJI POKOK      = Rp.20.000.000')
print('PAJAK GAJI      = 10%')
print('UANG LEMBUR/JAM = Rp. 10.000')
print('==================================')

# membuat variabel
nama = 'RACMAD LUKMAN MAULANA'
gaji_pokok = 20000000
uang_lembur = 10000
lama_lembur_jam = 4
gaji_lembur = uang_lembur * lama_lembur_jam
gaji_kotor = gaji_pokok + gaji_lembur
pajak = 10/100
potongan = gaji_kotor * pajak
gaji_bersih = gaji_kotor - potongan

# menampilkan hasil
print('\nNAMA ANDA           : ', nama)
print('GAJI POKOK ANDA     : ', gaji_pokok)
print('UANG LEMBUR ANDA    : ', uang_lembur)
print('LAMA LEMBUR/JAM     : ', lama_lembur_jam)
print(f'GAJI LEMBUR ANDA    :  Rp.{gaji_lembur:,.2f}')
print(f'GAJI KOTOR ANDA     :  Rp.{gaji_kotor:,.2f}')
print('PAJAK GAJI ANDA     : ',pajak)
print(f'POTONGAN GAJI ANDA  :  Rp.{potongan:,.2f}')
print(f'GAJI BERSIH ANDA    :  Rp.{gaji_bersih:,.2f}')

print('\n===================================================')
print('Jadi gaji yang Anda terima adalah = Rp. 18.036.000')
print('===================================================')