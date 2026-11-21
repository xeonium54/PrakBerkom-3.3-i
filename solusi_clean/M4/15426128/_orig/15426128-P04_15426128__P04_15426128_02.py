# NIM/Nama               : 15426128/Fathir Sulihansyah 
# Tanggal                : 11 November 2026
# Deskripsi              : Program untuk menghitung skor kekuatan PIN dan memberikan rekap kategorinya.

# Kamus Koding
# Spesifikasi Subprogram:
# hitung_skor_pin(pin: str) -> int
#   {Menhitung skor total keamanan suatu string PIN berdasarkan kriteria digit unik, 
#    huruf kapital, panjang PIN, dan penalti digit berurutan}
#
# tentukan_kategori(skor: int) -> str
#   {Menentukan kategori PIN ("Kuat", "Sedang", atau "Lemah") berdasarkan skor akhirnya}
#
# Variabel Utama (main):
# n                       : int   {Jumlah kandidat PIN yang akan dievaluasi}
# rekap_kuat, rekap_sedang,
# rekap_lemah             : int   {Penghitung (counter) jumlah PIN pada tiap kategori}
# pin                     : str   {String input kandidat PIN ke-i}
# skor                    : int   {Skor PIN yang dihitung}
# kategori                : str   {Kategori kekuatan PIN}

def hitung_skor_pin(pin: str) -> int:
    skor = 0
    
    # 1. Hitung digit unik (0-9)
    digit_unik = set()
    for char in pin:
        if '0' <= char <= '9':
            digit_unik.add(char)
    skor += len(digit_unik) * 4
    
    # 2. Cek minimal satu huruf besar
    ada_huruf_besar = False
    for char in pin:
        if 'A' <= char <= 'Z':
            ada_huruf_besar = True
            break
    if ada_huruf_besar:
        skor += 10
        
    # 3. Poin dari panjang PIN
    panjang = len(pin)
    if panjang >= 8:
        skor += 15
    elif 6 <= panjang <= 7:
        skor += 5
        
    # 4. Penalti digit berurutan bersebelahan dengan selisih tepat 1
    penalti = 0
    for i in range(len(pin) - 1):
        c1 = pin[i]
        c2 = pin[i+1]
        if '0' <= c1 <= '9' and '0' <= c2 <= '9':
            if abs(ord(c1) - ord(c2)) == 1:
                penalti += 5
    skor -= penalti
    
    return skor

def tentukan_kategori(skor: int) -> str:
    if skor >= 40:
        return "Kuat"
    elif skor >= 20:
        return "Sedang"
    else:
        return "Lemah"

def main():
    n = int(input("Masukkan jumlah kandidat PIN (N): "))
    
    rekap_kuat = 0
    rekap_sedang = 0
    rekap_lemah = 0
    
    for i in range(1, n + 1):
        pin = input(f"Kandidat PIN ke-{i}: ")
        skor = hitung_skor_pin(pin)
        kategori = tentukan_kategori(skor)
        
        print(f"PIN ke-{i} skornya {skor}, tergolong {kategori}.")
        
        if kategori == "Kuat":
            rekap_kuat += 1
        elif kategori == "Sedang":
            rekap_sedang += 1
        else:
            rekap_lemah += 1
            
    print(f"Rekap: Kuat {rekap_kuat}, Sedang {rekap_sedang}, Lemah {rekap_lemah}")

if __name__ == "__main__":
    main()
