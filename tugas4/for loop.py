#  1. Buat looping sebanyak 10x dari angka 15 sampai 30
#  2. Buat looping dari angka 100 dengan step -3 sebanyak 11x
for i in range (1, 11):
   print (f"sebanyak 10x, {i}")
   for a in range (15, 31):
    print (f"angka mulai (15 sampi 30), {a}")

    for i in range (1, 12):
      print (f"looping luar, {i}")
    for j in range (100, 67, -3):
      print (f"looping dalam, {j}")