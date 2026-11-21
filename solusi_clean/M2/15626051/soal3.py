# NIM/Nama : 15626051/Rafa Davlin Ginting Suka
# Tanggal  : 14 Oktober 2026
# Deskripsi: perhitungan prioritas dua kereta

JA = input("Masukan jenis Kereta A (Eksekutif/Bisnis/Kargo): ")
MA = int(input("masukan jarak kereta A dalam Meter: "))
KA = int(input("masukan kecepatan kereta A dalam m/s: "))
JB = input("Masukan jenis Kereta B (Eksekutif/Bisnis/Kargo): ")
MB = int(input("masukan jarak kereta B dalam Meter: "))
KB = int(input("masukan kecepatan kereta B dalam m/s: "))

WA = MA/KA
WB = MB/KB

if (WA >= WB):
    selisih = WA-WB
else:
    selisih = WB-WA

if (selisih >= 30):
    if (WA < WB ):
        print("jalur aman. kereta A melintas dahulu tanpa berhenti")
    else:
        print("jalur aman. kereta B melintas dahalu tanpa berhenti")

else:
    if(JA == "Eksekutif"):
        PA= 30
    elif(JA == "Bisnis"):
        PA = 20
    else:
        PA = 10


    if(JB == "Eksekutif"):
        PB= 30
    elif(JB == "Bisnis"):
        PB = 20
    else:
        PB = 10

    if(PA>PB):
        prioritas = "A"
    elif(PB>PA):
        prioritas = "B"
    else:
        if(WA < WB ):
         prioritas = "A"
        elif(WA>WB):
            prioritas = "B"
        else:
            if(MA > MB):
                prioritas = "B"
            else:
                prioritas = "A"
    print("kereta"+prioritas+ "di prioritaskan melintas")
    if (prioritas == "A"):
        waktu_tunggu = (WA + 40)- WB
        print(f"kereta B harus berhenti dan menunggu selama {waktu_tunggu:.1f}detik")
    else:
        waktu_tunggu = (WB + 40)- WA
        print(f"kereta A harus berhenti dan menunggu selama {waktu_tunggu:.1f}detik")