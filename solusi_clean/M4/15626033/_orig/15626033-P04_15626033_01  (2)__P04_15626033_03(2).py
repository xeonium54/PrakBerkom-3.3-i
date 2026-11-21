# NIM = 15626033
# Nama = Farah Ghiza HUmairoh 
# Tanggal = 11 nov 2026
# Deskripsi = pendekatan simulasi SKS
# Kamus = 1. a : integer, b : integer

def fungsi_tidur(M, energi_sekarang):
    """menghitung energi setelah tidur selama M jam (maksimal 100)"""
    energi_baru = energi_sekarang + (M * 12,5)
    if energi_baru > 100.0:
        energi_baru = 100.0
    return energi_baru
def fungsi_belajar(durasi, sisa_waktu, energi_sekarang): 
    """memproses durasi belajar dan pemotongan berdasarkan sisa waktu dan energi"""
    if durasi > sisa_waktu:
        durasi = sisa_waktu

    energi_dibutuhkan = durasi * 5.0
    if energi_dibutuhkan > energi_sekarang:
        durasi_riil = energi_sekarang / 5.0
        energi_baru = 0.0
    else:
        durasi_riil = durasi
        energi_baru = energi_sekarang - energi_dibutuhkan
    return durasi_rill, energi_baru

def hitung_prediksi_nilai(T1, T2, T3, T4, t1, t2, t3, t4, E):
    """Menghitung nilai UAS berdasarkan total durasi belajar dan sisa energi"""
    v1 = T1 if T1 < t1 else t1
    v2 = T2 if T2 < t2 else t2
    v3 = T3 if T3 < t3 else t3
    v4 = T4 if T4 < t4 else t4
    
    komponen_modul = ((v1/t1) + (v2/t2) + (v3/t3) + (v4/t4)) / 4.0
    komponen_energi = (100.0**2 - (100.0 - E)**2) / 100.0
    
    skor = komponen_modul * komponen_energi
    return skor
