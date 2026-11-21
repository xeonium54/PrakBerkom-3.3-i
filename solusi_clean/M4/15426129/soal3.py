# Nama: Kirani Rizky Aulia Khairunissa
# NIM: 15426129
# Tanggal: Rabu, 11 November 2026

# PROGRAM SistemKebutSemalam
# Deskripsi: User memasukkan sisa waktu belajar dan durasi belajar yang diinginkan untuk tiap modul, lalu sistem menentukan prediksi nilai yang akan didapatkan user sesuai tindakan yang dipilih

# KAMUS
# N : int
# t1, t2, t3, t4 : int
# tindakan, modul, durbel : int

# ALGORITMA
N = int(input("Masukkan sisa waktu: "))
t1 = int(input("Masukkan durasi untuk modul ke-1: "))
t2 = int(input("Masukkan durasi untuk modul ke-2: "))
t3 = int(input("Masukkan durasi untuk modul ke-3: "))
t4 = int(input("Masukkan durasi untuk modul ke-4: "))

for i in range(0,4):
    print("1. Belajar")
    print("2. Tidur")
    tindakan = int(input("Pilih tindakan (1/2): "))
    if tindakan == 1 or tindakan == 2:
        modul = int(input("Pilih modul yang ingin dipelajari: "))
        if modul == 1 or modul == 2 or modul == 3 or modul == 4:
            durbel: int(input("Masukkan durasi belajar: "))
        else:
            break
    else:
        print("Pilihan tidak tersedia!")