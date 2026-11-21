# NIM/Nama : 15626041/Dean Navarro Gratia Plena
# Tanggal : 11 November 2026
# Deskripsi : Sistem skor sederhana untuk PIN e-Wallet

def skor_pin(pin):
    skor = 0
    for d in "0123456789":
        if d in pin:
            skor += 4
    huruf_besar = False
    for c in pin:
     if "A" <= c <= "Z":
        huruf_besar = True
    if huruf_besar == True:
        skor += 10
    panjang = len(pin)
    if panjang >= 8:
       skor += 15
    elif panjang >= 6:
       skor += 5

    for i in range(panjang-1):
       if pin[i].isdigit() and pin[i+1].isdigit():
          selisih = int(pin[i]) - int(pin[i+1])
          if selisih == 1 or selisih == -1:
             skor -= 5
    return skor

def kategori_skor(skor):
   if skor >= 40:
      return "Kuat"
   elif skor >= 20:
      return "Sedang"
   else:
      return "Lemah"

jumlah_pin = int(input("Masukkan jumlah kandidat PIN: "))

jumlahkuat = 0
jumlahsedang = 0 
jumlahlemah = 0

for i in range(1,jumlah_pin + 1):
   pin = input(f"Kandidat PIN ke-{i}: ")
   skor = skor_pin(pin)
   kategori = kategori_skor(skor)
   print(f"PIN ke-{i} skornya {skor}, maka tergolong {kategori}")

   if kategori == "Kuat":
      jumlahkuat =+ 1
   elif kategori == "Sedang":
      jumlahsedang =+ 1
   elif kategori == "Lemah":
      jumlahlemah =+ 1

print(f"Kuat {jumlahkuat}, Sedang {jumlahsedang}, Lemah {jumlahlemah}")

   




    

         