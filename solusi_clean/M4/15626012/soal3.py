# NIM/Nama : 15626012/Muhammad Dzaky Nouvaldi
# Tanggal: 11 November 2026
# Deskripsi: Program dari hasil omon-omon Tuan Ky yang katanya mau lock-in

#KAMUS
# prediksi_nilai : float
# mendapat_tindakan : int
# mendapat_modul : int 
# sisa_waktu : float 
# t1, t2, t3, t4, T1, T2, T3, T4 : float 
# energi : float 
# durasi, energi_dibutuhkan, energi_belajar, energi_tambahan : float
# nilai uas : float 
# tindakan, modul : int 
# harus_tidur : boolean 

def prediksi_nilai(t1, t2, t3, t4, T1, T2, T3, T4, energi):

    #
    T1_usable = T1 if T1 <= t1 else t1
    T2_usable = T2 if T2 <= t2 else t2
    T3_usable = T3 if T3 <= t3 else t3 
    T4_usable = T4 if T4 <= t4 else t4


print(f'aduh tuan ky 😓')