# Nama File: Latihan6.3.Function.py
# Deskripsi: Program menerapkan Keyword Argument saat pemanggilan fungsi.

# Mendefinisikan fungsi untuk menampilkan biodata singkat
def tampilkan_biodata(nama, umur, jurusan):
    print(f"Nama    : {nama}")
    print(f"Umur    : {umur} tahun")
    print(f"Jurusan : {jurusan}")

# Memanggil fungsi menggunakan Keyword Argument.
# Dengan cara ini, urutan argumen tidak harus sama dengan urutan parameter di fungsi.
tampilkan_biodata(jurusan="Sistem Informasi", nama="Ferrr", umur=19)
