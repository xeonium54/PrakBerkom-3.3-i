# NIM/Nama : 15626038/Keysha Hana Putri
# Tanggal : Rabu, 11/11/2026
# Deskripsi : Program ini digunakan untuk menghitung skor dan kategori dari N kandidat PIN, serta menampilkan rekap banyaknya PIN pada tiap kategori.

#KAMUS
# N,kandidat : int
# kategori : str

#ALGORITMA
N = int(input("Masukkan jumlah kandidat PIN (N): "))
kandidat = [0 for in range(N)]
for i in range(N):
    kandidat[i] = int(input("Kandidat PIN ke-" + str(i) + ": "))