# NIM/Nama: Maria Amatussyafee Nurjaman
# Tanggal: 14/10/2026
# Deskripsi: Program menentukan kereta yang lewat duluan

# KAMUS 
# x, v, y, k : integer
# a, b, k : string

a = str(input("Masukan jenis Kereta A (Eksekutif/Bisnis/Kargo): "))
x = int(input("Masukan jarak Kereta A (m): "))
v = int(input("Masukan keceoatan Kereta A (m/s): "))
b = str(input("Masukan jenis Kereta B (Eksekutif/Bisnis/Kargo): "))
y = int(input("Masukan jarak Kereta B (m): "))
k = int(input("Masukan keceoatan Kereta B (m/s): "))

t_a = x / v
t_b = y / k
selisih = t_a - t_b
if selisih < 0:
    selisih = -selisih
p = {"Eksekutif": 3, "Bisnis": 2, "Kargo": 1}
p_a = p[a]
p_b = p[b]

if selisih >= 30.0:
    if t_a < t_b:
        print("Jalur aman, Kereta A melintas duluan tanpa henti")
    else:
        print("Jalur aman, Kereta B melintas duluan tanpa henti")
else:
    if p_a != p_b:
        a_menang = p_a > p_b
    elif t_a != t_b:
        a_menang = t_a < t_b
    elif x != y:
        a_menang = x < y
    else:
        a_menang = True

if a_menang:
    t = (t_a + 40.0) - t_b
    print("Kereta A diprioritaskan melintas duluan")
    print(f"Kereta B harus menunggu selama {t} detik")
else:
    t = (t_b + 40.0) - t_a
    print("Kereta B diprioritaskan melintas duluan")
    print(f"Kereta A harus menunggu selama {t} detik")
