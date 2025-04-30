#study kasus : buatkan program penjumlahan dengan casting angka yang diinput ke tipe data integer untuk melakukan operasi perkalian

#input
angka1_str = input("Masukkan angka pertama: ")
angka2_str = input("Masukkan angka kedua: ")

#melakukan casting dari string ke integer
angka1 = int(angka1_str)
angka2 = int(angka2_str)

#melakukan operasi perkalian
jumlah = angka1 + angka2

#menampilkan hasil
print(f"Hasil penjumlahan {angka1} * {angka2} = {jumlah}")