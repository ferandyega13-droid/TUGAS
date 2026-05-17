# Nama File: Latihan6.4.Function.py
# Deskripsi: Program menerapkan Parameter Dinamis (*args) untuk menerima jumlah input acak.

# Mendefinisikan fungsi yang menerima parameter dinamis
# Tanda bintang (*) berarti fungsi bisa menerima banyak argumen sekaligus dalam bentuk Tuple
def jumlahkan_semua_angka(*angka):
    total = 0
    # Melakukan perulangan untuk menjumlahkan setiap angka yang dikirim
    for n in angka:
        total += n
    return total

# Memanggil fungsi dengan jumlah parameter yang berbeda-beda
hasil_1 = jumlahkan_semua_angka(10, 20, 30)
hasil_2 = jumlahkan_semua_angka(5, 7, 12, 25, 40)

# Menampilkan hasil penjumlahan dinamis
print(f"Hasil penjumlahan pertama (3 angka): {hasil_1}")
print(f"Hasil penjumlahan kedua (5 angka): {hasil_2}")
