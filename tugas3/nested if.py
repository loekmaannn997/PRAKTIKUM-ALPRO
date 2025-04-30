# membuat studi kasus belanja apakah mendapat diskon sesuai jumlah barang yang yang dibeli
barang = input('Masukkan barang :')
harga = int(input('Masukkan harga barang :'))
jumlah = int(input('Masukkan jumlah barang :'))

if harga > 300000:
    if jumlah > 5:
        print('Anda mendapat diskon')
    else:
        print('Anda tidak mendapat diskon karena jumlah barang belanja anda kurang dari 5 barang')
else:
    print('Anda tidak mendapat diskon karena harga barang anda kurang dari 300.000')
    