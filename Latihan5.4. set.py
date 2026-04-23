# Nama File: Latihan5.4.set.py
# Deskripsi: Implementasi Set dan operasinya

# Membuat set (menggunakan kurung kurawal)
buah = {"Apel", "Jeruk", "Mangga"}
print("Set awal:", buah)

# 1. Menambah elemen tunggal
buah.add("Durian")

# 2. Menambah elemen duplikat (tidak akan masuk)
buah.add("Apel")

# 3. Menghapus elemen
buah.discard("Jeruk")

# 4. Operasi himpunan (contoh: gabungan/union)
buah_lain = {"Salak", "Anggur", "Apel"}
semua_buah = buah.union(buah_lain)

print("Daftar buah unik setelah digabung:")
for b in semua_buah:
    print(">", b)
