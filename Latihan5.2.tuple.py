# Nama File: Latihan5.2.tuple.py
# Deskripsi: Implementasi Tuple dan operasinya

# Membuat tuple (menggunakan kurung biasa)
koordinat = (10.5, -7.2)
print("Koordinat:", koordinat)

# 1. Mengakses elemen berdasarkan indeks
lat = koordinat[0]
lon = koordinat[1]
print(f"Latitude: {lat}, Longitude: {lon}")

# 2. Menghitung kemunculan nilai tertentu
angka = (1, 2, 3, 2, 4, 2)
print("Angka 2 muncul sebanyak:", angka.count(2), "kali")

# Tuple tidak bisa ditambah/dihapus elemennya secara langsung
