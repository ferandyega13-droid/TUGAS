# Nama File: Latihan3.1.kontrol_alur.py
# Deskripsi: Program mengelompokkan generasi berdasarkan tahun lahir

def main():
    try:
        # Mengambil input tahun lahir dari user
        tahun = int(input("Masukkan tahun lahir Anda: "))

        # Logika kontrol alur untuk menentukan kategori generasi
        if 1928 <= tahun <= 1945:
            generasi = "Silent Generation"
            deskripsi = "Tumbuh selama Depresi Besar dan Perang Dunia II, dikenal pekerja keras, sabar, dan hemat."
        elif 1946 <= tahun <= 1964:
            generasi = "Baby Boomers"
            deskripsi = "Lahir setelah Perang Dunia II, generasi ini mengalami lonjakan kelahiran dan fokus pada pencapaian personal."
        elif 1965 <= tahun <= 1980:
            generasi = "Generasi X"
            deskripsi = "Dikenal mandiri, tumbuh di masa peralihan teknologi tradisional ke digital (komputer/internet)."
        elif 1981 <= tahun <= 1996:
            generasi = "Generasi Y / Milenial"
            deskripsi = "Generasi yang melek teknologi (digital natives) dan peduli isu sosial."
        elif 1997 <= tahun <= 2012:
            generasi = "Generasi Z"
            deskripsi = "Tumbuh langsung di dunia internet dan teknologi canggih (iGeneration), sangat terhubung secara digital."
        elif 2013 <= tahun <= 2024:
            generasi = "Generasi Alpha"
            deskripsi = "Generasi pertama yang sepenuhnya lahir di abad ke-21, sangat dipengaruhi teknologi cerdas sejak kecil."
        elif 2025 <= tahun <= 2039:
            generasi = "Generasi Beta"
            deskripsi = "Generasi mendatang yang diprediksi akan melanjutkan keterhubungan digital tingkat lanjut."
        else:
            generasi = "Tidak Terdeteksi"
            deskripsi = "Tahun yang dimasukkan berada di luar jangkauan data kategori ini."

        # Menampilkan hasil
        print("-" * 30)
        print(f"Hasil Klasifikasi: {generasi}")
        print(f"Keterangan: {deskripsi}")
        print("-" * 30)

    except ValueError:
        # Penanganan jika user memasukkan input selain angka
        print("Error: Harap masukkan angka tahun yang valid (contoh: 1995).")

if __name__ == "__main__":
    main()
