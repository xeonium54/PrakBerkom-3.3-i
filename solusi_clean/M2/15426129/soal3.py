# PROGRAM Deteksi Konflik dan Penghitung Prioritas Kereta
# Deskripsi: User memasukkan jenis, jarak, dan kecepatan masing-masing kereta A dan B; sistem mendeteksi apabila ada konflik atau tidak dan apa yang harus dilakukan.

# KAMUS
# jenis_a : string
# jarak_a : int
# v_a : int
# jenis_b : string
# jarak_b : int
# v_b : int
# selisih : int

# ALGORITMA
jenis_a = str(input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo): "))
jarak_a = int(input("Masukkan jarak Kereta A (m): "))
v_a = int(input("Masukkan kecepatan Kereta A (m/s): "))
jenis_b = str(input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo): "))
jarak_b = int(input("Masukkan jarak Kereta B (m): "))
v_b = int(input("Masukkan kecepatan Kereta B (m/s): "))

t_a = jarak_a / v_a
t_b = jarak_b / v_b
selisih = 0
prioritas_a = 0
prioritas_b = 0
waktutunggu = 0

if t_a > t_b:
    selisih = t_a - t_b
else:
    selisih = t_b - t_a

if jenis_a == "Eksekutif":
    prioritas_a = 3
elif jenis_a == "Bisnis":
    prioritas_a = 2
else:
    prioritas_a = 1

if jenis_b == "Eksekutif":
    prioritas_b = 3
elif jenis_b == "Bisnis":
    prioritas_b = 2
else:
    prioritas_b = 1

if selisih >= 30:
    if v_a >= v_b:
        print("Jalur aman. Kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman. Kereta B melintas duluan tanpa henti.")
elif selisih < 30:
    if prioritas_a == prioritas_b:
        if t_a > t_b:
            print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
            waktutunggu = (t_a + 40) - t_b
            print("Kereta B harus berhenti dan menunggu selama", waktutunggu, "detik.")
        elif t_b > t_a:
            print("Konflik terdeteksi! Kereta B diprioritaskan melintas.")
            waktutunggu = (t_b + 40) - t_a
            print("Kereta A harus berhenti dan menunggu selama", waktutunggu, "detik.")
        elif t_a == t_b:
            if jarak_a > jarak_b:
                print("Konflik terdeteksi! Kereta B diprioritaskan melintas.")
                waktutunggu = (t_b + 40) - t_a
                print("Kereta A harus berhenti dan menunggu selama", waktutunggu, "detik.")
            elif jarak_b > jarak_a:
                print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
                waktutunggu = (t_a + 40) - t_b
                print("Kereta B harus berhenti dan menunggu selama", waktutunggu, "detik.")
            elif jarak_a == jarak_b:
                print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
                waktutunggu = (t_a + 40) - t_b
                print("Kereta B harus berhenti dan menunggu selama", waktutunggu, "detik.")
            else:
                print("Ada kesalahan")
    elif prioritas_a > prioritas_b:
            print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
            waktutunggu = (t_a + 40) - t_b
            print("Kereta B harus berhenti dan menunggu selama", waktutunggu, "detik.")
    elif prioritas_b > prioritas_a:
            print("Konflik terdeteksi! Kereta B diprioritaskan melintas.")
            waktutunggu = (t_b + 40) - t_a
            print("Kereta A harus berhenti dan menunggu selama", waktutunggu, "detik.")
    else:
        print("Ada kesalahan")
else:
    print("Ada kesalahan")
    