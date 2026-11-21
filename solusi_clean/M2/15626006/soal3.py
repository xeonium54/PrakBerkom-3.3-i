# NIM/Nama : 15626006/Maria Zeysta Kamelia Rumanti
# Tanggal : 14 Oktober 2026
# Deskripsi : Program untuk menentukan kereta yang diprioritaskan melintas serta waktu tunggu bagi kereta yang harus mengalah.

# Input kereta A
jenis_A = input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo): ")
jarak_A = int(input("Masukkan jarak Kereta A (m): "))
kecepatan_A = int(input("Masukkan kecepatan Kereta A (m/s): "))

# Input kereta B
jenis_B = input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo): ")
jarak_B = int(input("Masukkan jarak Kereta B (m): "))
kecepatan_B = int(input("Masukkan kecepatan Keret B (m/s): "))

# Hitung waktu tiba
tA = jarak_A / kecepatan_A
tB = jarak_B / kecepatan_B

# Hitung selisih waktu
if tA > tB:
    selisih = tA - tB
else:
    selisih = tB - tA

# Aturan persimpangan rel
if selisih >= 30.0:
    if tA < tB:
        print("Jalur aman. Kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman. Kereta B melintas duluan tanpa henti.")
else: 
    prioritas_A = 3 if jenis_A == "Eksekutif" else (2 if jenis_A == "Bisnis" else 1)
    prioritas_B = 3 if jenis_B == "Eksekutif" else (2 if jenis_B == "Bisnis" else 1)

    prioritas = 0

    if prioritas_A > prioritas_B:
        prioritas = "A"
    elif prioritas_B > prioritas_A:
        prioritas = "B"
    else:
        # Jika kedua kereta jenisnya sama
        if tA < tB:
            prioritas = "A"
        elif tB < tA:
            prioritas = "B"
        else:
            # Jika waktu tiba persis sama
            if jarak_A < jarak_B:
                prioritas = "A"
            elif jarak_B < jarak_A:
                prioritas = "B"
            else:
                # Jika jarak juga persis sama
                prioritas = "A"

# Hitung waktu tunggu kereta yang mengalah
if prioritas == "A":
    waktu_tunggu = (tA + 40.0) - tB
    print("Kereta A diprioritaskan melintas duluan.")
    print(f"Waktu tunggu Kereta A: {waktu_tunggu:.1f} detik.")
else:
    waktu_tunggu = (tB + 40.0) - tA
    print("Kereta B diprioritaskan melintas duluan.")
    print(f"Waktu tunggu Kereta B: {waktu_tunggu:.1f} detik")