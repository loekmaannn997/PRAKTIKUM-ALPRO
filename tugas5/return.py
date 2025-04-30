def hitung_luas(panjang, lebar):
    return panjang * lebar

def hitung_keliling(panjang, lebar):
    return 2 * (panjang + lebar)

# ==== Input dari user ====
print("=== Hitung Persegi Panjang ===")
panjang = float(input("Masukkan panjang (cm): "))
lebar = float(input("Masukkan lebar (cm): "))

# ==== Proses ====
luas = hitung_luas(panjang, lebar)
keliling = hitung_keliling(panjang, lebar)

# ==== Output ====
print("\n=== HASIL PERHITUNGAN ===")
print(f"Panjang       : {panjang} cm")
print(f"Lebar         : {lebar} cm")
print(f"Luas          : {luas} cm²")
print(f"Keliling      : {keliling} cm")

    