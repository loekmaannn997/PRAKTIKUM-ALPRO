# studi kasus menghitung daya listrik di rumah dalam satu hari
def benda(nama_brg,daya,hari):
    print("----- Menghitung Daya Listrik -----")
    print("Nama barang : ", nama_brg)
    print("Daya        : ", daya)
    print("Penggunaan  : ", hari)
    print("Hasil       : ", proses)

    

# input user
barang = input("Masukan barang :")
daya_listrik = int(input("Masukkan daya listrik : "))
waktu = int(input("Masukkan waktu dalam sehari :"))

# proses
proses = daya_listrik * waktu

# panggil fungsi
benda(barang,daya_listrik,waktu)
