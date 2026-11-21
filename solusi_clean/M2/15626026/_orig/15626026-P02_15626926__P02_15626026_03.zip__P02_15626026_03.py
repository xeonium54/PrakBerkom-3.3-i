# NIM / NAMA : MUTHI'AH AZKA NIAMILLAH
# TANGGAL : RABU, 14/10/2026
# DESKRIPSI : PROBLEM 3

# input 
jenis_A = input("masukkan jenis kereta A (Eksekutif/Bisnis/Argo): ")
D_A = int(input("masukkan jarak kereta A: "))
V_A = int(input("masukkan kecepatan kereta A: "))
jenis_B = input("masukkan jenis kereta B (Eksekutif/Bisnis/Argo): ")
D_B = int(input("masukkan jarak kereta B: "))
V_B = int(input("masukkan kecepatan kereta B: "))

# hitung waktu
T_A = D_A / V_A
T_B = D_B / V_B

# hitung selisih waktu
if T_A > T_B:
    selisih_waktu = T_A - T_B
else:
    selisih_waktu = T_B - T_A

# jika kasus aman
if selisih_waktu >= 30:
    if T_A < T_B:
        print("jalur aman, kereta A melintas duluan tanpa henti")
    else:
        print("jalur aman, kereta B melintas duluan tanpa henti")

# jika kasus tidak aman
    if jenis_A == "eksekutif": prioritas_A = 3
    elif jenis_A == "bisnis": prioritas_A = 2
    else: prioritas_A = 1

    if jenis_B == "eksekutif": prioritas_B = 3
    elif jenis_B == "bisnis": prioritas_B = 2
    else: prioritas_B = 1

# menentukan kereta prioritas
if prioritas_A > prioritas_B:
    prioritas = 'A'
elif prioritas_B > prioritas_A:
    prioritas = 'B'
else: # jika jenis kelas nya sama
    if T_A < T_B:
        prioritas = 'A'
    elif T_A > T_B:
    else: 
        # jika waktu nya sama
        if D_A < D_B:
            prioriras = 'A'
        elif D_A > D_B:
            prioritas = 'B'
        else: # jika semua sama
            prioritas_A

# output
if prioritas == 'A':
    waktu_tunggu = (T_A + 40) - T_B
    print("konflik terdeteksi! kereta A diprioritaskan melintas")
    print("kereta B harus berhenti dan menunggu selama {waktu_tunggu} detik")
else:
    waktu_tunggu = (T_B + 40) - T_A
    print("konflik terdeteksi! kereta B diprioritaskan melintas")
    print("kereta A harus berhenti dan menunggu selama {waktu_tunggu} detik")