# BUAT SET --> bracket, constructor
myset = {'s','e','t','1'}
myset2 = set(('s','e','t','2'))

# UNORDERED --> urutan tidak sama
print('data :',myset)
print('data :',myset2)
print('-----------')

# UNDUPLICATABLE --> unique
myset = {'s','e','t',1,1}
myset2 = (('s','e','t',2,2))
print('data :',myset)
print('data :',myset2)
print('----------')

# UNINDEXED --> tidak memiliki index
# ex: tampilkan index angka 1
myindex = myset.index(1)
print('index angka 1 :',myindex)
print('-----------')

# UCHANGEABLE --> tidak dapat di rubah
# ex: ubah angka index 3 dengan 9
myset[3] = 9
print('hasil edit :',myset)
print('-----------')

# TAMBAH DATA
# POP: random, remove: specific
myset.pop()
print('hasil pop :',myset)
print('-------------')

# ex: hapus 's' dari myset
myset.remove('s')
print('hasil remove :',myset)
print('--------------')

