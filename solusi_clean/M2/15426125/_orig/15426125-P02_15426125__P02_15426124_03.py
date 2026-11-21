nama: Nailini Kaylara Madhani
nim: 15426125
tanggal: 14 Oktober 2026



jenis_A = input("Masukkan jenis kereta A (eksekutif/bisnis/kargo): ")
DA = int(input("Masukkan jarak kereta A (meter): "))
VA = int(input("Masukkan kecepatan kereta A (m/s): "))

jenis_B = input("Masukkan jenis kereta B (eksekutif/bisnis/kargo): ")
DB = int(input("Masukkan jarak kereta B (m): "))
VB = int(input("Masukkan kecepatan kereta B (m/s)"))

#waktu tiba
Waktu_A = DA / VA
Waktu_B = DB/ VB

if Waktu_A >= Waktu_B:
    selisih = Waktu_A - Waktu_B
else:
    selisih = Waktu_B - Waktu_A

    if selisih >= 30.0:
        if Waktu_A < Waktu_B:
        print("Jalur aman. Kereta A melintas duluan tanpa henti." )
        else: print("Jalur aman. Kereta B melintas duluan tanpa henti.")

        
        if jenis_A == "eksekutif": prio_A = 3
        elif jenis A == "bisnis": prio_A = 2
        else: prio_B = 1

        if prio_A > prio_B:
            pemenang = "A"
        elif prio_B > prio_A:
            pemenang = "B"
        else:
            if jarak_A < jarak_B:
                pemenang = "A"
            elif jarak_B < jarak_A:
                pemenang = "B"
            else: jika jarak juga sama, kereta A di jalur utama
            pemenang = "A"

    if pemenang == "A":
        print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
        waktu_tunggu = (Waktu_A + 40.0) - Waktu_B
        print(f"Kereta B harud berhenti dan menunggu selama {waktu_tunggu:.1f} detik. ")
    else:
        print("Konflik terdeteksi! Kereta B diprioritaskan melintas. ")
        waktu_tunggu = (Waktu_B + 40.0) - Waktu_A
        print(f"Kereta A harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")

