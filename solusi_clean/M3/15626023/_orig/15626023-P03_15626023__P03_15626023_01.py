# NIM/Nama :15626023/Andre Partogi Nathanael Butarbutar
# Tanggal :28/10/2026
# Deskripsi :Program pemantau saldo e wallet tuan mik

saldo_awal = int(input("Masukkan saldo awal (Rp):")) #input saldo 
N = int(input("Masukkan jumlah transaksi (N):")) #input jumlah transaksi

saldo = saldo_awal #agar kode membaca saldo awal sebagai saldo dulu agar nantinya variabel saldo bs diubah
transaksi_negatif_pertama = -1 # sebagai syarat  tanda belum pernah negatif
total_pemasukan = 0 #total uang masuk dan uang keluar
total_pengeluaran = 0 #total uang masuk dan uang keluar

#loop untuk setiap transaksi
for i in range (1, N + 1) :
    nilai_transaksi = int(input(f"Masukkan nilai transaksi ke-{i} :"))
    saldo += nilai_transaksi
  
    print(f"Saldo setelah transaksi ke -{i} : Rp{saldo}.")  #mencatat saldo setelah transaksi
    if saldo < 0 and transaksi_negatif_pertama == -1 : #mengecek apakah saldo pertama negatif
        transaksi_negatif_pertama == i
    if nilai_transaksi > 0 : #memisahkan pemasukan dan pengeluaran
        total_pemasukan += nilai_transaksi
    else : 
        total_pengeluaran += nilai_transaksi #memisahkan pemasukan dan pengeluaran
#menampilkan hasil  pengecekan saldo negatif      
if transaksi_negatif_pertama != -1 :
    print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{transaksi_negatif_pertama}")
else :
    print(f"Saldo Tuan Mik tidak pernah negatif selama {N} transaksi ")
#menampilkan total pemasukan dan pengurangan
print(f"Total pemasukan: Rp{total_pemasukan} Total pengeluaran : Rp{total_pengeluaran}")
_