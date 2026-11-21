# NIM/Nama : 15626012/Muhammad Dzaky Nouvaldi
# Tanggal: 14 Oktober 2026
# Deskripsi: Program menentukan prioritas kereta di stasiun

#KAMUS
# kereta_a, kereta_b : str
# jarak_kereta_a, kecepatan_kereta_a : int
# jarak_kereta_b, kecepatan_kereta_b : int
# waktu_tiba_a, waktu_tiba_b : float
# selisih_waktu_tiba : float
# prioritas_a, prioritas_b : int
# kereta_a_prioritas = boolean
# waktu_tunggu : float


kereta_a  = str(input('Masukkan jenis kereta A (Eksekutif/Bisnis/Kargo): '))
jarak_kereta_a = int(input('Masukkan jarak kereta A (m): '))
kecepatan_kereta_a = int(input('Masukkan kecepatan kereta A (m/s): '))


kereta_b  = str(input('Masukkan jenis kereta B (Eksekutif/Bisnis/Kargo): '))
jarak_kereta_b = int(input('Masukkan jarak kereta B (m): '))
kecepatan_kereta_b = int(input('Masukkan kecepatan kereta B (m/s): '))

waktu_tiba_a = float(jarak_kereta_a / kecepatan_kereta_a)
waktu_tiba_b = float(jarak_kereta_b / kecepatan_kereta_b)  


if waktu_tiba_a >= waktu_tiba_b:
    selisih_waktu_tiba = waktu_tiba_a - waktu_tiba_b
else:
    selisih_waktu_tiba = waktu_tiba_b - waktu_tiba_a

if selisih_waktu_tiba >= 30.0:


    if waktu_tiba_a <= waktu_tiba_b:
        print('Jalur aman, kereta A melintas terlebih dahulu')
    else: 
        print('Jalur aman, kereta B melintas terlebih dahulu') 
else: 
    if kereta_a == 'Eksekutif':
        prioritas_a = 3
    elif kereta_a == 'Bisnis':
        prioritas_a = 2
    else:
        prioritas_a = 1

    if kereta_b == 'Eksekutif':
        prioritas_b = 3
    elif kereta_b == 'Bisnis':
        prioritas_b = 2
    else:
        prioritas_b = 1


kereta_a_prioritas = False 
if prioritas_a > prioritas_b:
    kereta_a_prioritas = True
elif prioritas_a < prioritas_b:
    kereta_a_prioritas = False
else:
    if waktu_tiba_a <= waktu_tiba_b:
        kereta_a_prioritas = True
    elif waktu_tiba_b < waktu_tiba_a:
        kereta_a_prioritas = False
    else:
        if jarak_kereta_a < jarak_kereta_b:
            kereta_a_prioritas = True
        elif jarak_kereta_b < jarak_kereta_a:
            kereta_a_prioritas = False
        else:
            kereta_a_prioritas = True



if kereta_a_prioritas:
    waktu_tunggu = (waktu_tiba_a + 40.0) - waktu_tiba_b
    print('konflik ditemukan, kereta A dulu')
    print(f'kereta B harus menunggu selama {waktu_tunggu:.2f} detik')
else:
    waktu_tunggu = (waktu_tiba_b + 40.0) - waktu_tiba_a
    print('konflik ditemukan, kereta B dulu')
    print(f'kereta A harus menunggu selama {waktu_tunggu:.2f} detik')