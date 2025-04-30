# seseorang ingin mengelola keuangan pribadinya. dia memiliki beberapa pengeluaran dan pendapatan
# diketahui saldo yang dimiliki orang tersebut senilai Rp. 700.000
print('='*37)
print('SALDO AWAL REKENING ANDA = Rp.700.000')
print('='*37)

# membuat variabel pendapatan1
saldo1 = 700000 
saldo1 += 500000
saldo1 -= 300000
print(f'\nPENDAPATAN BULAN 1 : Rp.{saldo1:,.2f}')

# membuat variabel pendapatan2
saldo2 = saldo1
saldo2 += 400000
saldo2 -= 250000
print(f'PENDAPATAN BULAN 2 : Rp.{saldo2:,.2f}')

# membuat variabel pendapatan3
saldo3 = saldo2
saldo3 += 700000
saldo3 -= 500000
print(f'PENDAPATAN BULAN 3 : Rp.{saldo3:,.2f}')

# menghitung pendapatan selama 3 bulan
pendapatan_3_bulan = saldo1 + saldo2 + saldo3
print('\n')
print('='*43)
print(f'PENDAPATAN SELAMA 3 BULAN : Rp.{pendapatan_3_bulan:,.2f}')
print('='*43)


