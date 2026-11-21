# NIM/Nama  : 15626024 / Akbar Muhammad Al Ghifari
# Tanggal   : 14 October 2026
# Deskripsi : Program yang mengecek 

# Kamus


# Algoritma
JenisA = str(input("Masukkan jenis Kereta A ( Eksekutif/Bisnis/Kargo): "))
JarakA = int(input("Masukkan jarak kereta A (m): "))
SpeedA = int(input("Masukkan kecepatan kereta A (m/s): "))
JenisB = str(input("Masukkan jenis Kereta B( Eksekutif/Bisnis/Kargo): "))
JarakB = int(input("Masukkan jarak kereta B (m): "))
SpeedB = int(input("Masukkan kecepatan kereta B (m/s): "))
PrioA = int
PrioB = int
Prio = str
wktu = int
Ta = float((JarakA/SpeedA))
Tb = float((JarakB/SpeedB))
GapAB = float((Ta-Tb))

if (GapAB < 0):
    GapAB = float(GapAB*(-1))
else:
   GapAB = float(GapAB)

if (GapAB >= 30.00):
    if (Ta<Tb):
        print("Jalur aman. Kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman. Kereta B melintas duluan tanpa henti.")
else:
    if JenisA == "Eksekutif":
        PrioA = 3
    elif JenisA == "Bisnis":
        PrioA == 2
    else:
        PrioA == 1

    if JenisB == "Eksekutif":
            PrioB = 3
    elif JenisB == "Bisnis":
            PrioB == 2
    else:
        PrioB == 1

if PrioA > PrioB:
     Prio = "A"
elif PrioB > PrioA:
     Prio = "B"
else:
    if Ta < Tb:
          Prio = "A"
    elif Tb < Ta:
          Prio = "B"
    else:
        if JarakA < JarakB:
            prio = "A"
        elif JarakB < JarakA:
            prio = "B"
        else:
             prio = "A"

if (prio == str("A")):
     wktu = (Ta + 40.00) -Tb
     print(f"Konflik terdeteksi ! Kereta a diprioritaskan melintas. Kereta B harus berhenti dan menunggu selama {wktu:.1f} detik.")
else:
     wktu = (Tb + 40.00) -Ta
     print(f"Konflik terdeteksi ! Kereta B diprioritaskan melintas. Kereta A harus berhenti dan menunggu selama {wktu:.1f} detik.")