# Nama = Jihan Salsabila
# NIM = 15626002

# PROGRAM menghitung skor pin

# KAMUS
pin: str
skor: int

# Definisi fungsi
def menghitung_skor (pin):
    digit=""
    jumlah_digit = 0
    if c in "0123456789":
     if c not in digit:
         digit = digit + c
         jumlah_digit = jumlah_digit + 1
    skor = jumlah_digit * 4

if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
   ada_huruf_besar = True
   if ada_huruf_besar:
       skor+=10
   else:
     # tidak terjadi apa-apa

panjang = 0
if panjang >= 8:
        skor += 15
    elif panjang >= 6:
        skor += 5

def kategori(skor):
    if skor >= 40:
        return "Kuat"
    elif skor >= 20:
        return "Sedang"
    else:
        return "Lemah"

jumlah_kandidat = int(input("Masukkan jumlah kandidat pin (N)"))

pin = input(f"Kandidat PIN ke-{i+1}: ")

print(f"Rekap: Kuat {kuat}, Sedang {sedang}, Lemah {lemah}")
