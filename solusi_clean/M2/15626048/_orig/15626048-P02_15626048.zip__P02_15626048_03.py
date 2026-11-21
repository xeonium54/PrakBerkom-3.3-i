# Nim: 15626048
# Tanggal: 14 Oktober 2026
# Deskripsi: Program untuk lintasan kereta api

# Kamus
# jenis: string
# DA, DB, VA, VB: int
# TA, TB: float
# tunggu: float
# prioritas: string

# Algoritma
jenisA = input("Jenis kereta A:")
DA = int(input("Jarak kereta A dalam (m):"))
VA = int(input("Kecepatan kereta A dalam (m/s):"))

jenisB = input("Jenis kereta B:")
DA = int(input("Jarak kereta B dalam (m):"))
VA = int(input("Kecepatan kereta B dalam (m/s):"))

TA = DA/VA
TB = DB/VB

# Selisis waktu
if TA >= TB:
    selisih = TA-TB
else:
    selisih = TB-TA

if selisih >=30:
    
    if TA > TB:
        print("Jalur aman, kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman, kereta B melintas duluan tanpa henti.")
        
else:
    
    if jenisA == jenisB:
        
        if TA < TB:
            prioritas = "A"
        elif TB < TA:
            prioritas = "B"
        else:
            
        if DA < DB:
            prioritas = "A"
        elif DB < DA:
            prioritas = "B"
        else:
            prioritas = "A"
            
else:
    
    if jenisA == "Eksekutif":
        prioritas = "A"
    elif jenisB == "Eksekutif":
        prioritas = "B"
    elif jenisA == "Bisnis":
        prioritas = "A"
    else:
        prioritas = "B"


# Menghitung waktu tunggu
if prioritas =="A":
    waktu_tunggu = (TA + 40.0)-TB
    print("Kereta A diprioritaskan melintas")
    print(f"Kereta B menunggu selama")

