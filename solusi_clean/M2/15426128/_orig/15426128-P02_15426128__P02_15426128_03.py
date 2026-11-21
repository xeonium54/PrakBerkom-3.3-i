# NIM/Nama : 15426128/Fathir Sulihansyah 
# Tanggal  : 14 Oktober 2026
# Deskripsi: Program pengatur perjalanan kereta api di stasiun berkom

# Kamus koding :
# jenis_A, jenis_B : (String) Menyatakan jenis kereta
# D_A, D_B : (Interger) Jarak kereta ke persimpangan
# V_A, V_B: (Interger) Kecepatan tempuh kereta
# T_A, T_B: (Float) Waktu tiba masing masing kereta di persimpangan
# selisih: (Float) Selisih waktu tiba kedua kereta
# waktu_tunggu: (Float) Durasi waktu tunggu bagi kereta yang harus mengalah

jenis_A = input("Masukkan jenis kereta A(Eksekutif/Bisnis/Kargo): ")
D_A = int(input("Masukkan jarak kereta A(m): "))
V_A = int(input("Masukkan kecepatan kereta A(m/s): "))

jenis_B = input("Masukkan jenis kereta B(Eksekutif/Bisnis/Kargo): ")
D_B = int(input("Masukkan jarak kereta B(m): "))
V_B = int(input("Masukkan kecepatan kereta B(m/s): "))

T_A = D_A/V_A
T_B = D_B/V_B

diff = T_A - T_B
if diff < 0:
    selisih = -diff
else:
    selisih = diff    

if selisih >= 30.0:
    if T_A < T_B:
        print(f"Jalur aman. Kereta A melintas duluan tanpa henti.")
    else:
        print(f"Jalur aman. Kereta B melintas duluan tanpa henti.")
 
else:
    if jenis_A == "Eksekutif":
        prio_A = 3
    elif jenis_A == "Bisnis": 
        prio_A = 2           
    else:
        prio_A = 1
    
    if jenis_B == "Eksekutif":
        prio_B = 3
    elif jenis_B == "Bisnis": 
        prio_B = 2           
    else :
         prio_B = 1
    
    if prio_A > prio_B:
        prio_kereta = "Kereta A"
        mengalah = "Kereta B"
        t_prio = T_A
        t_mengalah = T_B
    elif prio_B > prio_A:
        prio_kereta = "Kereta B"
        mengalah = "Kereta A"
        t_prio = T_B
        t_mengalah = T_A  
    else :
        if T_A > T_B:
            prio_kereta = "Kereta A"
            mengalah = "Kereta B"
            t_prio = T_A
            t_mengalah = T_B
        elif T_B > T_A:
            prio_kereta = "Kereta B"
            mengalah = "Kereta A"
            t_prio = T_B
            t_mengalah = T_A      
        else:
           if D_A > D_B:
                prio_kereta = "Kereta A"
                mengalah = "Kereta B"
                t_prio = T_A
                t_mengalah = T_B
           elif D_B > D_A:
                prio_kereta = "Kereta B"
                mengalah = "Kereta A"
                t_prio = T_B
                t_mengalah = T_A  
           else:
                prio_kereta = "Kereta A"
                mengalah = "Kereta B"
                t_prio = T_A
                t_mengalah = T_B

waktu_tunggu = (t_prio + 40.0)- t_mengalah

print (f"Konflik terdeteksi! {prio_kereta} diprioritaskan melintas.")
print (f"{mengalah} harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")