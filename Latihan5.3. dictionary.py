# Nama File: Latihan5.3.dictionary.py
# Deskripsi: Implementasi Dictionary dan operasinya

# Membuat dictionary data mahasiswa
mahasiswa = {
    "nama": "Andi",
    "nim": "2021001",
    "prodi": "Informatika"
}
print("Data awal:", mahasiswa)

# 1. Menambah/Update elemen
mahasiswa["semester"] = 4
mahasiswa["nama"] = "Andi Wijaya" # Update nilai

# 2. Mengakses nilai berdasarkan key
print("Nama Mahasiswa:", mahasiswa.get("nama"))

# 3. Menghapus elemen
del mahasiswa["prodi"]

# 4. Menampilkan semua key dan value
print("Isi Dictionary:")
for k, v in mahasiswa.items():
    print(f"{k}: {v}")
