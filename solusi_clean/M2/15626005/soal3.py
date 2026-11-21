# NIM/Nama : 15626005/Addien Maulana Bima
# Tanggal : 14 Oktober 2026
# Deskripsi : Program analisis waktu tunggu kereta dan kereta prioritas

kereta_A = input("Masukkan jenis kereta A : ")
jarak_A = float(input("Masukkan jarak kereta A (m) : "))
kec_A = float(input("Masukkan kecepatan kereta A (m/s) : "))
kereta_B = input("Masukkan jenis kereta B : ")
jarak_B = float(input("Masukkan jarak kereta B (m) : "))
kec_B = float(input("Masukkan kecepatan kereta B (m/s) : "))

T_A = jarak_A/kec_A
T_B = jarak_B/kec_B
selisih_waktu = T_A-T_B if T_A>=T_B else T_B - T_A
if selisih_waktu>=30:
    if T_A<T_B:
        print("Jalur aman. Kereta A melintas duluan tanpa henti.")
    else : 
        print("Jalur aman. Kereta B melintas duluan tanpa henti.")
else :
    print("Konflik kereta terdeteksi.")
    if kereta_A=="Eksekutif":
        p_a = 3
    elif kereta_A=="Bisnis":
        p_a = 2
    else :
        p_a = 1
    if kereta_B=="Eksekutif":
        p_b = 3
    elif kereta_B=="Bisnis":
        p_b = 2
    else :
        p_b = 1
    if p_a!=p_b:
        pemenang = 'A' if p_a>p_b else 'B'
    elif T_A != T_B:
        pemenang = 'A' if T_A<T_B else 'B'
    elif jarak_A!=jarak_B:
        pemenang = 'A' if jarak_A<jarak_B else 'B'
    else : 
        pemenang = 'A'
    kalah = 'B' if pemenang=='A' else 'B'
    t_pemenang = T_A if pemenang=='A' else T_B
    t_kalah = T_B if pemenang=='A' else T_A
    waktu_tunggu = (t_pemenang+40)-t_kalah
    print(f"Kereta {pemenang} diprioritaskan melintas.")
    print(f"Kereta {kalah} harus menunggu selama waktu tunggu {waktu_tunggu}")

