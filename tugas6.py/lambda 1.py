# membuat study kasus mencari siswa yang lulus dan mengurutkan berdasarkan nilai

# membuat daftar list siswa dan nilai
siswa = [
    {"nama": "lukman", "nilai": 80},
    {"nama": "Andaru", "nilai": 72},
    {"nama": "Sihab", "nilai": 90},
    {"nama": "Terompet", "nilai": 65},
    {"nama": "Daus", "nilai": 77},
]

# Filter siswa yang nilainya >= 75
lulus = list(filter(lambda s: s["nilai"] >= 75, siswa))

print("Siswa yang lulus:")
for s in lulus:
    print(f"{s['nama']} (nilai: {s['nilai']})")

# Urutkan semua siswa berdasarkan nilai 
siswa_urut = sorted(siswa, key=lambda s: s["nilai"], reverse=True)

print("\nSiswa diurutkan berdasarkan nilai:")
for s in siswa_urut:
    print(f"{s['nama']} (nilai: {s['nilai']})")