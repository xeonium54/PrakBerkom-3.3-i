# Nama = Jihan Salsabila
# NIM = 15626002

# Program MencariKonsentrasiLarutanTotal
# Mencari Konsentrasi total berdasarkan volume dan konsentrasi

# KAMUS
# volume larutan 1 : integer
# volume larutan 2 : integer
# volume larutan 3 : integer
# Konsentrasi larutan 1 : integer
# Konsentrasi larutan 2 : integer
# Konsentrasi larutan 3 : integer

# ALGORITMA
Volume_Larutan1 = int(input("Masukkan volume larutan 1(ml):"))
Konsentrasi_Larutan1 = int(input("Masukkan konsentrasi larutan 1(persen):"))
Volume_Larutan2 = int(input("Masukkan volume larutan 2(ml):"))
Konsentrasi_Larutan2 = int(input("Masukkan konsentrasi larutan 2(persen):"))
Volume_Larutan3 = int(input("Masukkan volume larutan 3(ml):"))
Konsentrasi_Larutan3 = int(input("Masukkan konsentrasi larutan 3(persen):"))

Konsentrasi_Akhir = (Konsentrasi_Larutan1*Volume_Larutan1)+(Konsentrasi_Larutan2*Volume_Larutan2)+(Konsentrasi_Larutan3*Volume_Larutan3)/(Volume_Larutan1 + Volume_Larutan2 + Volume_Larutan3)
print(f"Konstentrasi akhir larutan campuran adalah {Konsentrasi_Akhir}")

