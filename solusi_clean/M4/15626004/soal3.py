# NIM/Nama : 15626004 / Nirmala Rahma Maulida
# Tanggal : Rabu, 11 November 2026
# Deskripsi : Program memprediksi nilai UAS Tuan Ky berdasarkan durasi belajar dan tidur
# KAMUS :
# lebar, tinggi : int

# subprogram perhitungan 
def HitungNilaiUAS(T1, T2, T3, T4, t1, t2, t3, t4, E):
    # Menghitung prediksi nilai UAS 
    # KAMUS LOKAL 
    #

# Algoritma program utama 
sisa_waktu = float(input("masukkan sisa waktu : "))
t1 = float(input("masukkan durasi untuk modul ke-1: "))
t2 = float(input("masukkan durasi untuk modul ke-2: "))
t3 = float(input("masukkan durasi untuk modul ke-3: "))
t4 = float(input("masukkan durasi untuk modul ke-4: "))

while sisa_waktu > 0:
    print("1. Belajar")
    print("2. Tidur")
    tindakan = int(input("pilih tindakan (1/2)")) 
    
    while tindakan == 1:
    modul = int(input("pilih modul yang ingin dipelajari (1-4): "))
    
