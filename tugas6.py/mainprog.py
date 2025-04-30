# study kasus mengubah suhu dan mengonversi panjang

# main.py

from suhu import celcius_ke_fahrenheit, fahrenheit_ke_celcius
from panjang import km_ke_meter, meter_ke_km

def main():
    print("=== Konversi Satuan ===")

    # Konversi Suhu
    c = float(input("Masukkan suhu (Celcius): "))
    print(f"{c} °C = {celcius_ke_fahrenheit(c):.2f} °F")

    f = float(input("Masukkan suhu (Fahrenheit): "))
    print(f"{f} °F = {fahrenheit_ke_celcius(f):.2f} °C")

    # Konversi Panjang
    km = float(input("Masukkan panjang (km): "))
    print(f"{km} km = {km_ke_meter(km)} meter")

    m = float(input("Masukkan panjang (meter): "))
    print(f"{m} meter = {meter_ke_km(m):.2f} km")

if __name__ == "__main__":
    main()