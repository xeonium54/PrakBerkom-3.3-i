# NIM/Nama : 15626050/Yohanes Yoel Christopher Naibaho
# Tanggal : 14-10-2026
# Deskripsi :Memvalidasi skor ujian peserta

# KAMUS
# skor peserta: int 

# Algoritma
skor_peserta = int(input("masukan skor ujian peserta: "))
if skor_peserta >= 0 and skor_peserta <= 100:
    print("skor peserta valid,dapat diiinput ke sistem. ")
else:
    print("skor peserta tidak valid,perlu dipperiksa ulang")



