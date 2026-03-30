# Program untuk mengonversi suhu dari Celsius ke Fahrenheit
# Rumus: (Celsius * 9/5) + 32

# Mengambil input dari user
celsius = float(input("Masukkan suhu dalam Celsius: "))

# Menghitung konversi menggunakan operator aritmatika
# Kita menggunakan rumus (C * 1.8) + 32
fahrenheit = (celsius * 9/5) + 32

# Menampilkan hasil konversi
print(f"{celsius} derajat Celsius sama dengan {fahrenheit} derajat Fahrenheit.")
