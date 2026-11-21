# NIM/ Nama : Aghneo Amar Ahsan
# Tanggal : 30 September 2026
# Deskripsi : Program ini akan menghitung total biaya listrik yang terbuang 

# Kamus : 
# j1, j2, m1, m2, totalMenit, MenitKerjaNormal, upahPerMenit, pengaliUpahLembur, tunjanganMakan, batasMinimalTunjangan, JamTotalDurasiKerja, MenitTotalDurasiKerja, MenitKerjaLembur : int
# pengaliUpahLembur, TotalUpah : float
j1 = int(input("Masukkan jam masuk : "))
m1 = int(input("Masukkan menit masuk : "))
j2 = int(input("Masukkan jam keluar : "))
m2 = int(input("Masukkan menit masuk : "))

totalMenit = ((j2*60) + m2) - ((j1*60) + m1)

MenitKerjaNormal = int(input("Masukkan batas shift normal (menit) : "))
upahPerMenit = int(input("Masukkan upah per menit : "))
pengaliUpahLembur = float(input("Masukkan pengali upah lembur : "))
tunjanganMakan = int(input("Masukkan tunjangan makan : "))
batasMinimalTunjangan = int(input("Masukkan batas minimal tunjangan (menit) : "))

JamTotalDurasiKerja = int(totalMenit / 60)
MenitTotalDurasiKerja = totalMenit % 60
MenitKerjaLembur = totalMenit - MenitKerjaNormal
TotalUpah = ((totalMenit - MenitKerjaLembur)*upahPerMenit) + (MenitKerjaLembur * upahPerMenit * pengaliUpahLembur) + tunjanganMakan

print("Total durasi kerja : ", JamTotalDurasiKerja," Jam", MenitTotalDurasiKerja, " Menit")
print("Menit kerja normal : ", MenitKerjaNormal)
print("Menit kerja lembur : ", MenitKerjaLembur)
print("Total upah diterima : ", TotalUpah)