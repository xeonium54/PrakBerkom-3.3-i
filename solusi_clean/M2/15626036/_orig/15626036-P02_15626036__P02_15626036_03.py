#NIM/Nama : Aghneo Amar Ahsan
#Tanggal : 14 Oktober 2026
#Deskripsi :

#Kamus 

jenisKeretaA = str(input("Masukkan jenis kereta A (Eksekutif/Bisnis/Kargo): "))
jarakKeretaA = int(input("Masukkan jarak kereta A: "))
kecepatanKeretaA = int(input("Masukkan kecepatan kereta A: "))

waktuKeretaA = jarakKeretaA / kecepatanKeretaA
if jenisKeretaA == "Eksekutif": 
    skalaPrioritasA = 3
elif jenisKeretaA == "Bisnis":
    skalaPrioritasA = 2
elif jenisKeretaA == "Kargo": 
    skalaPrioritasA = 1

jenisKeretaB = str(input("Masukkan jenis kereta B (Eksekutif/Bisnis/Kargo): "))
jarakKeretaB = int(input("Masukkan jarak kereta B: "))
kecepatanKeretaB = int(input("Masukkan kecepatan kereta B: "))

waktuKeretaB = jarakKeretaB / kecepatanKeretaB
if jenisKeretaB == "Eksekutif": 
    skalaPrioritasB = 3
elif jenisKeretaB == "Bisnis":
    skalaPrioritasB = 2
elif jenisKeretaB == "Kargo": 
    skalaPrioritasB = 1

selisih = waktuKeretaA - waktuKeretaB
if selisih < 0:
    selisih = selisih * (-1)
elif selisih >= 0:
    selisih = selisih

if selisih >= 30:
    if waktuKeretaA < waktuKeretaB: 
        print("Jalur Aman. Kereta A melintas duluan tanpa henti!!!")
    elif waktuKeretaA > waktuKeretaB: 
        print("Jalur Aman. Kereta B melintas duluan tanpa henti!!!")

elif selisih < 30:
    if skalaPrioritasA > skalaPrioritasB: 
        waktuTunggu = (waktuKeretaA + 40) - waktuKeretaB
        print("Konflik terdeteksi kereta A diprioritaskan!!!")
        print(f"Kereta B berhenti dan menunggu selama {waktuTunggu} detik")
    elif skalaPrioritasA < skalaPrioritasB: 
        waktuTunggu = (waktuKeretaB + 40) - waktuKeretaA
        print("Konflik terdeteksi kereta B diprioritaskan!!!")
        print(f"Kereta A berhenti dan menunggu selama {waktuTunggu} detik")
    elif skalaPrioritasA == skalaPrioritasB: 
        if waktuKeretaA < waktuKeretaB:
            waktuTunggu = (waktuKeretaA + 40) - waktuKeretaB
            print("Konflik terdeteksi kereta A diprioritaskan!!!")
            print(f"Kereta B berhenti dan menunggu selama {waktuTunggu} detik") 
        elif waktuKeretaA > waktuKeretaB:
            waktuTunggu = (waktuKeretaB + 40) - waktuKeretaA
            print("Konflik terdeteksi kereta B diprioritaskan!!!")
            print(f"Kereta A berhenti dan menunggu selama {waktuTunggu} detik") 
        elif waktuKeretaA == waktuKeretaB:
             if jarakKeretaA < jarakKeretaB:
                waktuTunggu = (waktuKeretaA + 40) - waktuKeretaB
                print("Konflik terdeteksi kereta A diprioritaskan!!!")
                print(f"Kereta B berhenti dan menunggu selama {waktuTunggu} detik") 
             elif jarakKeretaA > jarakKeretaB:
                waktuTunggu = (waktuKeretaB + 40) - waktuKeretaA
                print("Konflik terdeteksi kereta B diprioritaskan!!!")
                print(f"Kereta A berhenti dan menunggu selama {waktuTunggu} detik") 
             elif jarakKeretaA == jarakKeretaB:
                waktuTunggu = (waktuKeretaA + 40) - waktuKeretaB
                print("Konflik terdeteksi kereta A diprioritaskan!!!")
                print(f"Kereta B berhenti dan menunggu selama {waktuTunggu} detik")      
            