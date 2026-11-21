#NIM/Nama : 15626027/Muhammad Faiz Dhiaul Haq
#Tanggal : 11 November 2026
# Deskripsi : Program menghitung skor pin

def hitung_skor_pin (pin):
  skor = 0

  # hitung digit berbeda (0-9)
  digit_unik = set()
  ada_huruf_besar = False

  for char in pin:
    if char.isdigit():
      digit_unik.add(char)
    if char.isupper():
      ada_huruf_besar = True

  skor += len(digit_unik) * 4

  #Bonus Huruf besar
  if ada_huruf_besar:
    skor += 10

  #Bonus Panjang pin
  panjang = len(pin)
  if panjang >= 8:
    skor += 15
  elif 6 <= panjang <= 7:
    skor += 5
  
  penalti = 0
  for i in range(panjang - 1):
    if pin [i].isdigit() and pin [i+1].isdigit():
      selisih = int(pin[i]) - int(pin[i+1])
      if selisih == 1:
      penalti += 5
    
  skor -= penalti
  return skor

def tentukan_kategori(skor):
    if skor >= 40:
        return "kuat"
    elif 20 <= skor < 40:
        return "Sedang"
    else:
        return "Lemah"

def main():
  n = int(inut("Masukkan Jumlah Kandidat PIN (N): "))
  rekap = {"Kuat": 0, "Sedang": 0, "Lemah": 0}

  for i in range(1, n + 1):
      pin = input(f"Kandidat PIN ke -{i}: ")
      skor = hitung_skor_pin
      kategori = tentukan_kategori (skor)

      rekap[kategori] += 1

      print(f"PIN ke-{i} skornya {skor}, tergolog {kategori}.")
