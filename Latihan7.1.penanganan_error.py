# Nama File: Latihan7.1.penanganan_error.py
# Deskripsi: Program menggunakan blok try dan except untuk menangani error saat runtime.

print("--- Program Pembagian Angka (Try - Except) ---")

# Blok try digunakan untuk membungkus kode yang berpotensi menimbulkan error
try:
    # Meminta input dari pengguna dan mengubahnya menjadi integer
    angka1 = int(input("Masukkan angka pertama (pembilang): "))
    angka2 = int(input("Masukkan angka kedua (penyebut): "))
    
    # Melakukan operasi pembagian
    hasil = angka1 / angka2
    print(f"Hasil pembagian: {hasil}")

# Blok except pertama untuk menangani error jika input bukan berupa angka/integer
except ValueError:
    print("Error: Input yang Anda masukkan harus berupa angka bulat!")

# Blok except kedua untuk menangani error matematika jika penyebut bernilai 0
except ZeroDivisionError:
    print("Error: Angka tidak bisa dibagi dengan nol (0)!")

# Blok except umum jika terjadi error lain di luar dugaan
except Exception as e:
    print(f"Terjadi kesalahan yang tidak diketahui: {e}")
