# NIM/Nama : 15626004
# Tanggal : 10/14/2026
# Deskripsi : Program pengatur perjalanan kereta api di stasiun berkom

# KAMUS
#

# Algoritma
jenis_A = input("jenis kereta A: ")
jarak_A= int("jarak kereta A: ")
kecepatan_A = int("kecepatan kereta A: ")

jenis_B = input("jenis kereta B: ")
jarak_B= int("jarak kereta B: ")
kecepatan_B = int("kecepatan kereta B: ")

ta = jarak_A / kecepatan_A
tb = jarak_B / kecepatan_B

selisih = ta-tb

if selisih >= 30:
    if ta < tb:
        print("jalur aman, kereta A melintas pertama tanpa harus berhenti")
    else:
        print("jalur aman, kereta B melintas pertama tanpa harus berhenti")
else:
    prio_A = 3 
    if jenis_A == "eksekutif"
    else
    prio_B = 3 
    if jenis_B == "eksekutif"



