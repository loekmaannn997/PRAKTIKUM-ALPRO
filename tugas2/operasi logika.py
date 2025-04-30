# membuat suatu program apakah seseorang bisa mendapatkan diskon atau tidak dalam berbelanja
def cek_diskon(harga, barang):
    if harga > 300000 and barang > 10:
        return 'Dapat Diskon'
    else :
        return 'Tidak Dapat Diskon'

# menampilkan hasil dari fungsi di atas    
print('PEMBELI 1 : ', cek_diskon(350000,18))   
print('PEMBELI 2 : ', cek_diskon(200000,11))   
print('PEMBELI 3 : ', cek_diskon(300000,10))   
