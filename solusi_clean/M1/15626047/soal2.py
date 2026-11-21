# NIM/Nama  : 15626047 / Jeremia Arista Matthew Sugiarto
# Tanggal   : 30 September 2026
# Deskripsi : Menghitung konsentrasi akhir larutan

#Kamus
#V1,V2,V3= Volume larutan
#C1,C2,C3= Konsentrasi larutan

#Input
C1=int(input("Masukan konsentrasi larutan pertama (persen):"))
V1=int(input("Masukan volume larutan pertama (mL):"))
C2=int(input("Masukan konsentrasi larutan kedua (persen):"))
V2=int(input("Masukan volume larutan kedua (mL):"))
C3=int(input("Masukan konsentrasi larutan ketiga (persen):"))
V3=int(input("Masukan volume larutan ketiga (mL):"))

#Algoritma
Cfinal=float(C1*V1+C2*V2+C3*V3)/(V1+V2+V3)

#Output
print(f"Konsentrasi akhir campuran larutan adalah {Cfinal} persen")