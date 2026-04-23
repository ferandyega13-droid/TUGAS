# Nama File: Latihan5.1.list.py
# Deskripsi: Implementasi List dan operasinya

# Membuat list awal
hobi = ["Membaca", "Coding", "Traveling"]
print("List awal:", hobi)

# 1. Menambah elemen (append)
hobi.append("Memasak")

# 2. Mengubah elemen berdasarkan indeks
hobi[0] = "Menulis"

# 3. Menghapus elemen berdasarkan nilai
hobi.remove("Traveling")

# 4. Menampilkan panjang list
print("Jumlah hobi:", len(hobi))

# Menampilkan semua elemen dengan perulangan
print("Daftar hobi terbaru:")
for x in hobi:
    print("-", x)
