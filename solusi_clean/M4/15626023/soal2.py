# NIM/Nama :15626023/Andre Partogi Nathanael Butarbutar
# Tanggal :11/11/2026
# Deskripsi :Menghitung skor dan kategori N kandidat PIN , lalu menampilkan rekap

#pin tidak mungin berisi $  jadi $ dipakai sebagai penanda akhir
def hitung_panjang(teks):
    s = teks + "$"
    i = 0 
    while (s [i] != "$"): # maju terus sampai nemu penanda
        i += 1
    return i 

# mengembalikan -1 kalau c bukan digit
def nilai_digit(c):
    angka = "0123456789"
    for d in range (10):
        if (c == angka[d]):
            return d
    return -1

# fungsi c apakah c huruf besar
def huruf_besar(c):
    besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # syaratnya
    for i in range(26):
        if (c == besar[i]):
            return True
    return False

