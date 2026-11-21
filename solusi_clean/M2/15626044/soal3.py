# P03.15626044.02
# NIM : 15662044
# Tanggal : 14 Oktober 2026
# Deskripsi : Problem 3

# Masukkan identitas kereta A
kereta_a = str(input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo): "))
Da = int(input("Masukkan jarak Kereta A (m): "))
Va = int(input("Masukkan kecepatan Kereta A (m/s):  "))

# Masukkan identitas kereta B
kereta_b = str(input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo): "))
Db = int(input("Masukkan jarak Kereta B (m): "))
Vb = int(input("Masukkan kecepatan Kereta B (m/s):  "))

# Menghitung waktu saat tiba (dalam detik)
Ta = Da / Va
Tb = Db / Vb

# Selisih waktu Ta dan Tb
if Ta >= Tb:
    selisih_waktu = Ta - Tb
else:
    selisih_waktu = Tb - Ta

# Menentukan kereta siapa yang akan melintas duluan
if selisih_waktu >= 30:
    if Ta < Tb:
        print("Jalur aman. Kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman. Kereta B melintas duluan tanpa henti.")
else:

# Jika waktu selisih kurang dari 30 menit maka konflik terdeteksi
    print("Konflik terdeteksi!")

if selisih_waktu < 30:
    if kereta_a == "Eksekutif" and kereta_b != "Eksekutif":
        lebih_dulu = "a"
    elif kereta_b == "Eksekutif" and kereta_a != "Eksekutif":
        lebih_dulu = "b"
    elif kereta_a == "Bisnis" and kereta_b == "Kargo":
        lebih_dulu = "a"
    elif kereta_b == "Bisnis" and kereta_a == "Kargo":
        lebih_dulu = "b"
# Apabila jenis kereta sama
else:
    if Ta < Tb:
        lebih_dulu = "a"
    elif Ta > Tb:
        lebih_dulu = "b"
    # Apabila waktu tiba sama
    else:
        if Ta < Tb:
            lebih_dulu = "a"
        elif Ta > Tb:
            lebih_dulu = "b"
        # Apabila jarak sama
        else:
            lebih_dulu = "a"

# Hitung waktu tunggu dan tampilkan siapa yang lebih dulu
if lebih_dulu == "a":
    waktu_tunggu = (Ta + 40.0) - Tb
    print("Kereta A diprioritaskan melintas.")
    print(f"Kereta B harus berhenti dan menunggu selama {waktu_tunggu} detik.")
else:
    waktu_tunggu = (Tb + 40.0) - Ta
    print("Kereta B diprioritaskan melintas.")
    print(f"Kereta A harus berhenti dan menunggu selama {waktu_tunggu} detik.")



