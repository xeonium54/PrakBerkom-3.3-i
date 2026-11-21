# NIM/Nama : 15626050/Yohanes Yoel Christopher Naibaho
# Tanggal : 14-10-2026
# Deskripsi : membantu tuan toji mengatur alur kereta

# KAMUS
# Jenis kereta A, Jenis kereta B : str
# DA,DB,VA,VB : int
# TA, TB, selisih waktu tiba kereta A dan B : float
# Prioritas A,Prioritas B: int
# tunggu : float

# ALGORITMA
Jenis_kereta_A= input("Masukkan Jenis kereta A(Eksekutif/Bisnis/Kargo): ")
DA = int(input("Masukkan jarak kereta A(meter): "))
VA = int(input("Masukkan Kecepatan kereta A(m/s): "))

Jenis_kereta_B= input("Masukkan Jenis kereta B(Eksekutif/Bisnis/Kargo): ")
DB = int(input("Masukkan jarak kereta B(meter): "))
VB = int(input("Masukkan Kecepatan kereta B(m/s): "))

TA = DA/VA
TB = DB/VB

selisih_waktu_tiba = TA - TB

