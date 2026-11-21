#NIM/Nama : 15626027/Muhammad Faiz Dhiaul Haq
#Tanggal : 14 Oktober 2026
#Deskripsi : Membuat program Pengatur perjalanan kereta api di persimpangan tunggal

#Kamus:
#jenis_A dan jenis_B : string (Jenis Kelas kereta A dan B)
#d_A dan d_B : integer (jarak kereta ke persimpangan)
#v_A dan v_B : integer (Kecepatan kereta A dan B)
#t_A dan t_B : float (waktu tiba kereta A dan B di persimpanagn  T= d/v)
#selisih t : float (Selisih waktu tiba antara kedua kereta)
#prioritas : integer (Eksekutif kemudian bisnis kemudian kargo)
#t_tunggu : float (lama waktu tunggu kereta yang mengalah)

#Input Variabel kereta A
jenis_A = input("Masukkan jenis kereta A (Eksekutif/Bisnis/Kargo): ")
d_A = int(input("Masukkan jarak kereta A (meter): "))
v_A = int(input("Masukkan kecepatan kereta A (meter/sekon):"))

#Input Variabel kereta B
jenis_B = input("Masukkan jenis kereta B (Eksekutif/Bisnis/Kargo): ")
d_B = int(input("Masukkan jarak kereta B (meter): "))
v_B = int(input("Masukkan kecepatan kereta B (meter/sekon): "))

#waktu tiba
t_A = d_A / v_A
t_B = d_B / v_B

#selisih waktu tiba
if t_A >= t_B:
    selisih = t_A - t_B
else:
    selisih = t_B - t_A

#selisih waktu aman (>= 30 detik)
if selisih >= 30.0:
    if t_A < t_B:
        print("Jalur aman, kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman, kereta B melintas duluan tanpa henti.")

#selisih waktu kurang dari 30 detik
else: 
    peta_prioritas = {"Eksekutif": 3, "Bisnis": 2, "Kargo": 1}
p_A = peta_prioritas[jenis_A]
p_B = peta_prioritas[jenis_B]

if p_A > p_B:
    kereta_prioritas = 'A'
elif p_B > p_A:
    kereta_prioritas = 'B'
else:
    if t_A < t_B:
        kereta_prioritas = 'A'
    elif t_B < t_A:
        kereta_prioritas = 'B'
    else:
        if d_A < d_B:
            kereta_prioritas = 'A'
        elif d_B < d_A:
            kereta_prioritas = 'B'
        else:
            kereta_prioritas = 'A'

if kereta_prioritas == 'A':
    kereta_mengalah = 'B'
    t_tunggu = (t_A + 40.0) - t_B
else:
    kereta_mengalah = 'A'
    t_tunggu = (t_B + 40.0) - t_A

print(f"konflik terdeteksi! kereta {kereta_prioritas} diprioritaskan melintas.")
print(f"kereta {kereta_mengalah} harus berhenti dan menunggu selama {t_tunggu: .1f} detik")
