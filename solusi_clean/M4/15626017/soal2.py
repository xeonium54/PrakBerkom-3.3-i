# NIM/Nama       : 15626017/Naura Vira Vania Ramadhani 
# Tanggal        : 11 November 2026
# Deskripsi      : Menghitung skor kekuatan PIN dan merekap kategorinya

def hitung_skor_pin(pin: str) -> int:
    skor = 0
    
    digit_unik = set()
    for char in pin:
        if '0' <= char <= '9':
            digit_unik.add(char)
    skor += len(digit_unik) * 4
    
    ada_huruf_besar = False
    for char in pin:
        if 'A' <= char <= 'Z':
            ada_huruf_besar = True
            break
    if ada_huruf_besar:
        skor += 10
        
    panjang = len(pin)
    if panjang >= 8:
        skor += 15
    elif 6 <= panjang <= 7:
        skor += 5
        
    for i in range(len(pin) - 1):
        c1 = pin[i]
        c2 = pin[i+1]
        if '0' <= c1 <= '9' and '0' <= c2 <= '9':
            if abs(int(c1) - int(c2)) == 1:
                skor -= 5
                
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
        
        if kategori == "Kuat":
            rekap_kuat += 1
        elif kategori == "Sedang":
            rekap_sedang += 1
        else:
            rekap_lemah += 1
            
        print(f"PIN ke-{i} skornya {skor}, tergolong {kategori}.")
        
    print(f"Rekap: Kuat {rekap_kuat}, Sedang {rekap_sedang}, Lemah {rekap_lemah}")

if __name__ == "__main__":
    main()