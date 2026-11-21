# NIM/Nama  : Vidia Nurafifa
# Tanggal   : Rabu, 14/10/2026
# Deskripsi : Pengatur perjalanan kereta

# ada persimpangan rel tunggal, kereta A dan Kereta B menuju titik persimpangan
# jenis kereta = jnk 
# jarak kereta = jrk
# kecepatan kereta = kck
# waktu = w
# prioritas = p
# waktu tunggu = wt 

jnka = input("Masukkan jenis kereta A (Eksekutif/Bisnis/Kargo): ") 
jrka = float(input("Masukkan jarak kereta A (m): "))
kcka = float(input("Masukkan kecepatan kereta A (m/s): "))
jnkb = input("Masukkan jenis kereta B (Eksekutif/Bisnis/Kargo): ") 
jrkb = float(input("Masukkan jarak kereta B (m): "))
kckb = float(input("Masukkan kecepatan kereta B (m/s): "))

wa = jrka / kcka
wb = jrkb / kckb

if wa >= wb:
    selisih = wa - wb
else:
    selisih = wb - wa
    
if selisih >= 30:
    if wa < wb:
        print("Jalur aman. Kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman. Kereta B melintas duluan tanpa henti.") 
else:
    if jnka == "Eksekutif":
        pa = 3
    elif jnka == "Bisnis":
        pa = 2
    elif jnka == "Kargo":
        pa = 1
    else:
        exit()
        
    if jnkb == "Eksekutif":
        pb = 3
    elif jnkb == "Bisnis":
        pb = 2
    elif jnkb == "Kargo":
        pb = 1
    else:
        exit()

if pa > pb:
    a_win = True
elif pb > pa:
    a_win = False
else:
    if wa < wb:
        a_win = True
    elif wb < wa:
        a_win = False
    else:
        if jrka < jrkb:
            a_win = True
        elif jrkb < jrka:
            a_win = False
        else:
            a_win = True
            
if a_win:
    wt = (wa+40) - wb
    print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
    print(f"Kereta B harus berhenti dan menunggu selama {wt} detik")
else:
    wt = (wb+40) - wa
    print("Konflik terdeteksi! Kereta B diprioritaskan melintas.")
    print(f"Kereta A harus berhenti dan menunggu selama {wt} detik")