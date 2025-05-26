# BUAT LIST --> bracket, constructor
mylist = [5,7,3]
list(('a','b','c'))

#ORDERED --> urutan data tetap
print('data :',mylist)
print('data :',mylist)
print('---------------')

#DUPLICATE --> data ganda
mylist = [5,7,3,3]
mylist2 = list(('a','b','c','c'))
print('Duplikat :',mylist)
print('Duplikat :',mylist2)
print('---------------')

#INDEX --> 0
#ex: tampilkan nomer index angka 7
myindex = mylist.index(7)
print('index angka 7 :',myindex)
print('-------------')

#CHANGE
#TAMBAH DATA
# -> append: last, insert: index
mylist.append(8)
print('hasil append :',mylist)
print('--------------')

# ex: tambahkan angka 9 pada index 1 
mylist.insert(1,9)
print(' HASIL Insert :',mylist)
print('-----------')

# HAPUS DATA
# -> pop: last, remove: specific
mylist.pop()
print('Hasil pop :',mylist)
print('-------------')

