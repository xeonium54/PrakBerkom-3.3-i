# NIM/Nama :15626023/Andre Partogi N Butarbutar
# Tanggal :14/10/2026
# Deskripsi :Percabangan

jenis_A = input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo):")
Jarak_A = float(input("Masukkan jarak Kereta A (m):"))
Kecepatan_A = float(input("Masukkan kecepatan Kereta A (m/s):"))

jenis_B = input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo):")
Jarak_B = float(input("Masukkan jarak Kereta B (m):"))
Kecepatan_B = float(input("Masukkan kecepatan Kereta B (m/s):"))

t_A = Jarak_A / Kecepatan_A
t_B = Jarak_B / Kecepatan_B

if t_A >= t_B :
    selisih = t_A - t_B
else :
    selisih = t_B - t_A

if selisih >= 30 :
    print("Jalur aman")
    if t_A <= t_B :
        print ("Kereta A diprioritaskan melintas duluan tanpa henti")
    else :
        print("Kereta B diprioritaskan melintas duluan tanpa henti")
else:
    print(" Konflik terdeteksi!")

if jenis_A == "Eksekutif" :
    Prioritas_A = 3
elif jenis_A == "Bisnis" :
    Prioritas_A = 2
else :
    Prioritas_A = 1

if jenis_B == "Eksekutif" :
    Prioritas_B = 3
elif jenis_B == "Bisnis" :
    Prioritas_B = 2
else :
    Prioritas_B = 1

if Prioritas_A > Prioritas_B :
    print("Kereta A diprioritaskan melintas")
    waktu_tunggu = (t_A + 40) - t_B
    print(f"Kereta B harus berhenti dan menunggu selama{waktu_tunggu:.1f} detik ")
elif Prioritas_B > Prioritas_A :
    print("Kereta B diprioritaskan melintas")
    waktu_tunggu = (t_A + 40) - t_B
    print(f"Kereta A harus berhenti dan menunggu selama{waktu_tunggu:.1f} detik ")
else :
    if t_A < t_B :
        print("Kereta A diprioritaskan melintas")
        waktu_tunggu = (t_A + 40) - t_B
        print(f"Kereta B harus berhenti dan menunggu selama{waktu_tunggu:.1f} detik ")
    elif  t_B < t_A:
        print("Kereta B diprioritaskan melintas")
        waktu_tunggu = (t_A + 40) - t_B
        print(f"Kereta A harus berhenti dan menunggu selama{waktu_tunggu:.1f} detik ")
    else:
        if Jarak_A < Jarak_B :
            print("Kereta A diprioritaskan melintas")
            waktu_tunggu = (t_A + 40) - t_B
            print(f"Kereta B harus berhenti dan menunggu selama{waktu_tunggu:.1f} detik ")
        elif Jarak_B < Jarak_A :
            print("Kereta B diprioritaskan melintas")
            waktu_tunggu = (t_A + 40) - t_B
            print(f"Kereta A harus berhenti dan menunggu selama{waktu_tunggu:.1f} detik ")
        else:
            print("Kereta A diprioritaskan melintas")
            waktu_tunggu = (t_A + 40) - t_B
            print(f"Kereta B harus berhenti dan menunggu selama{waktu_tunggu:.1f} detik ")

        
        