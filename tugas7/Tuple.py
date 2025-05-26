# CREATE --> bracket, constructor
mytuple = ('alif',83) 
mytuple2 = tuple(('alif','alfy'))

#   OREDERED --> urutan data tetap
print('data :',mytuple)
print('data :',mytuple2)
print('--------------')

# DUPLICATE --> data ganda
ytuple = ('alif',83) 
mytuple2 = tuple(('alif','alfy','alfy'))
print('duplikat :',mytuple)
print('duplikat :',mytuple2)
print('--------------')

# INDEX --> 0
# ex: tampilkan no. index angka 83
# ,myindex = mytuple.index(83)
# print ('index angka 83 :',myindex)
# print('-----------')

# UNCHANGEABLE --> tidak dapat dirubah
# ex: ubah data index 1 dengan 90
mytuple[1] = 90
print('hasil edit :',mytuple)
print('-----------')



