# ==========================================
# Nama File: Latihan8.1.operasi_file.py
# Deskripsi: Implementasi seluruh mode operasi file
# ==========================================

# 1. IMPLEMENTASI MODE 'w' (Write / Menulis Baru)
# Membuka file untuk menulis teks awal. Jika file belum ada, otomatis dibuat.
file = open("contoh_tugas.txt", "w")
file.write("Ini adalah baris pertama menggunakan mode 'w'.\n")
file.close() # Selalu tutup file setelah digunakan

# 2. IMPLEMENTASI MODE 'r' (Read / Membaca)
# Membuka file yang tadi dibuat untuk dibaca isinya.
file = open("contoh_tugas.txt", "r")
isi_file = file.read()
print("--- Hasil Mode 'r' ---")
print(isi_file)
file.close()

# 3. IMPLEMENTASI MODE 'a' (Append / Menambah)
# Membuka file untuk menambah teks baru di baris bawahnya tanpa menghapus teks lama.
file = open("contoh_tugas.txt", "a")
file.write("Ini teks tambahan menggunakan mode 'a'.\n")
file.close()

# 4. IMPLEMENTASI MODE 'r+' (Read and Write)
# Membuka untuk membaca sekaligus menulis dari awal file.
file = open("contoh_tugas.txt", "r+")
print("--- Hasil Mode 'r+' (Sebelum ditulis ulang) ---")
print(file.read())
file.write("Teks dari mode 'r+'.\n")
file.close()

# 5. IMPLEMENTASI MODE 'w+' (Write and Read)
# Membuka untuk menulis dan membaca, tapi isi sebelumnya akan DIHAPUS total terlebih dahulu.
file = open("contoh_tugas.txt", "w+")
file.write("File di-reset dan diisi teks baru oleh mode 'w+'.\n")
file.seek(0) # Mengembalikan kursor ke awal file agar bisa dibaca
print("--- Hasil Mode 'w+' ---")
print(file.read())
file.close()

# 6. IMPLEMENTASI MODE 'a+' (Append and Read)
# Membuka untuk menambah data di akhir sekaligus membaca.
file = open("contoh_tugas.txt", "a+")
file.write("Baris ini ditambahkan oleh mode 'a+'.\n")
file.seek(0) # Kembalikan kursor ke awal untuk membaca seluruh isi file
print("--- Hasil Mode 'a+' ---")
print(file.read())
file.close()
