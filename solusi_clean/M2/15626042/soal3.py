#Nama : Febrian Yafi Hakim
#NIM : 15626042
#Problem 3

jenis_A = input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo): ")
jarak_A = int(input("Masukkan jarak Kereta A (m): "))
kecepatan_A = int(input("Masukkan kecepatan Kereta A (m/s): "))

jenis_B = input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo): ")
jarak_B = int(input("Masukkan jarak Kereta B (m): "))
kecepatan_B = int(input("Masukkan kecepatan Kereta B (m/s): "))

TA = jarak_A / kecepatan_A
TB = jarak_B / kecepatan_B

if TA > TB:
    selisih = TA - TB
else:
    selisih = TB - TA


if selisih >= 30.0:
    if TA < TB:
        print("Jalur aman. Kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman. Kereta B melintas duluan tanpa henti.")
else:
    prio_A = 0
    if jenis_A == "Eksekutif":
        prio_A = 3
    elif jenis_A == "Bisnis":
        prio_A = 2
    elif jenis_A == "Kargo":
        prio_A = 1
        
    prio_B = 0
    if jenis_B == "Eksekutif":
        prio_B = 3
    elif jenis_B == "Bisnis":
        prio_B = 2
    elif jenis_B == "Kargo":
        prio_B = 1
    pemenang = ""
    
    if prio_A > prio_B:
        pemenang = "A"
    elif prio_B > prio_A:
        pemenang = "B"
    else: # Jika jenis kereta sama
        if TA < TB:
            pemenang = "A"
        elif TB < TA:
            pemenang = "B"
        else: # Jika waktu tiba persis sama
            if jarak_A < jarak_B:
                pemenang = "A"
            elif jarak_B < jarak_A:
                pemenang = "B"
            else: # Jika jarak juga persis sama
                pemenang = "A"
    if pemenang == "A":
        waktu_tunggu = (TA + 40.0) - TB
        print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
        print(f"Kereta B harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")
    else:
        waktu_tunggu = (TB + 40.0) - TA
        print("Konflik terdeteksi! Kereta B diprioritaskan melintas.")
        print(f"Kereta A harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")