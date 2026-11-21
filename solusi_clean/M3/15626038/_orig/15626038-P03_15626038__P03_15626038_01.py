# NIM/Nama : 15626038 / Keysha Hana Putri
# Tanggal : Rabu, 28 Oktober 2026
# Deskripsi : Program ini digunakan untuk membantu Tuan Mik dalam mengelola keuangannya

#KAMUS:
# S : int
# N : int

#ALGORITMA
S = int(input('Masukkan saldo awal (Rp): '))
N = int(input('Masukkan jumlah transaksi (N):  '))
tabel = [1 for transaksi in range(N+1)]
for transaksi in range(1,N+1):
    tabel[transaksi] = int(input('Masukkan nilai transaksi ke-' + str(transaksi) + ': '))

# Kak, Pak, Bu, atau siapapun yang mengoreksi praktikum ini, saya ucapkan mohon maaf karena saya belum menguasai modul 3 dan masih jauh dari kata siap, sehingga program yang saya kumpulkan hanya bisa seadanya seperti ini. Saya akan belajar dari kesalahan ini dan berusaha lebih baik lagi di praktikum selanjutnya. Terima kasih.