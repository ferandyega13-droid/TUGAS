# Nama File: Latihan7.2.penanganan_error.py
# Deskripsi: Program menerapkan struktur lengkap try, except, else, dan finally.

print("--- Program Konversi Nilai (Try - Except - Else - Finally) ---")

try:
    # Mengambil input string dan mencoba mengubahnya menjadi tipe data float
    input_user = input("Masukkan suhu dalam Celcius (contoh: 36.5): ")
    suhu = float(input_user)

# Blok except akan dieksekusi HANYA JIKA kode di dalam blok 'try' mengalami error
except ValueError:
    print("Gagal: Karakter yang dimasukkan tidak valid sebagai angka suhu.")

# Blok else akan dieksekusi HANYA JIKA kode di dalam blok 'try' berjalan dengan lancar tanpa error
else:
    fahrenheit = (suhu * 9/5) + 32
    print(f"Berhasil! Suhu {suhu}°C setara dengan {fahrenheit}°F.")

# Blok finally akan SELALU dieksekusi, baik terjadi error maupun tidak
finally:
    print("Sesi pengecekan suhu selesai. Terima kasih telah menggunakan program ini.")
