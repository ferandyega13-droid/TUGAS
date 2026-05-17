# Nama File: Latihan6.2.Function.py
# Deskripsi: Program menggunakan fungsi dengan parameter dan mengembalikan nilai (return).

# Mendefinisikan fungsi untuk menghitung luas persegi panjang
# Fungsi ini menerima dua parameter: panjang dan lebar
def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    # Mengembalikan hasil perhitungan ke baris kode yang memanggilnya
    return luas

# Menentukan nilai input
p = 10
l = 5

# Memanggil fungsi dengan mengirimkan argumen p dan l, 
# lalu menyimpan hasilnya ke dalam variabel 'hasil_luas'
hasil_luas = hitung_luas_persegi_panjang(p, l)

# Menampilkan hasil
print(f"Panjang: {p}, Lebar: {l}")
print(f"Luas Persegi Panjang adalah: {hasil_luas}")
