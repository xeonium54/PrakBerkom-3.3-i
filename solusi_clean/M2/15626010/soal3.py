# NIM/Nama : 15626010/Faiz Abdurrahman
# Tanggal : 14/10/2026
# Deskripsi : Program ini berfungsi untuk mengatur lalu lintas dan mencegah tabrakan dua kereta di persimpangan rel tunggal secara otomatis.

# input informasi kereta A
jenis_A = input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo): ")
jarak_A = int(input("Masukkan jarak kereta A (m): "))
kec_A = int(input("Masukkan kecepatan kereta A (m/s): "))

# input informasi kereta B
jenis_B = input("Masukkan jenis kereta B (Eksekutif/Bisnis/Kargo): ")
jarak_B = int(input("Masukkan jarak kereta B(m): "))
kec_B  = int(input("Masukkan kecepatan Kereta B (m/s): "))

# Menghitung waktu tiba (T=D/V)
t_A = jarak_A / kec_A
t_B = jarak_B / kec_B

# menghitung selisih waktu
if t_A > t_B:
    selisih = t_A - t_B
else:
    selisih = t_B - t_A

# aturan persimpangan
if selisih >= 30.0:
    if t_A < t_B:
        print("Jalur aman. Kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman. Kereta B melintas duluan tanpa henti.")
else:
    prio_map = {"Eksekutif": 3, "Bisnis": 2, "Kargo": 1}
    prio_A = prio_map[jenis_A]
    prio_B = prio_map[jenis_B]

# menentukan prioritas jalan
if prio_A > prio_B:
    a_prioritas = True
elif prio_B > prio_A:
    a_prioritas = False
else:
    if t_A < t_B:
        a_prioritas = True
    elif t_B < t_A:
        a_prioritas = False
    else:
        if jarak_A < jarak_B:
            a_prioritas = True
        elif jarak_B < jarak_A:
            a_prioritas = True
        else:
            a_prioritas = True

# hasil konflik & perhitungan waktu tunggu
print("Konflik terdeteksi!", end=" ")
if a_prioritas:
    waktu_tunggu = (t_A + 40.0) - t_B
    print("Kereta A diprioritaskan melintas.")
    print(f"Kereta B harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")
else:
    waktu_tunggu=(t_B + 40.0) - t_A
    print("Kereta B diprioritaskan melintas.")
    print(f"Kereta A harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")