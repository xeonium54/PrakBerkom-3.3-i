# Nama: Siti Nawa Aulia
# NIM: 15626048
# Deskripsi: Membuat subprogram untuk menghitung skor suatu PIN dan menentukan kategorinya berdasarkan skor tersebut

# Kamus: 
# N: int
# i: int
# pin: str
# skor: int
# kategori: str
# kuat: int 
# sedang: int 
# lemah: int

# Algoritma

def hitung_skor (pin):
    skor = 0
    digit = set()
    
    # digit berbeda
    for karakter in pin:
        if karakter.isdigit():
            digit.add(karakter)
            
    skor = skor + len(digit)*4
    
    # bonus berbeda
    for karakter in pin:
        if karakter.isupper():
            skor = skor + 10
            break 
        
    