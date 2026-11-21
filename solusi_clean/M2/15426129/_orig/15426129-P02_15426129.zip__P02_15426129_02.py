# NIM/Nama : 15426129/Kirani Rizky Aulia Khairunissa
# Tanggal : Rabu, 14 Oktober 2026

# PROGRAM Total Parkir Kompeng Mall
# Deskripsi: User memasukkan durasi parkir, jenis mobil (listrik/tidak), waktu parkir (akhir pekan/tidak); sistem menghitung total parkir.

# KAMUS
# durasi : integer
# tarif : integer
# listrik (y/n) : char
# akhirpekan (y/n) : char
# total : string

# ALGORITMA
durasi = int(input("Masukkan durasi parkir (jam): "))
listrik = str(input("Apakah mobil listrik (y/n): "))
akhirpekan = str(input("Apakah akhir pekan (y/n): "))
tarifflat = 5000
tarif2jam = 0
tarifover2jam = 0
tarifover6jam = 0
totalsementara = 0
total = 0

if -1 < durasi < 2:
    totalsementara = tarifflat
elif durasi == 2:
    tarif2jam = tarifflat
    totalsementara = tarif2jam
elif 2 < durasi <= 6:
    tarif2jam = tarifflat
    tarifover2jam = 3000
    totalsementara = (tarif2jam) + ((durasi - 2) * tarifover2jam)
elif durasi > 6:
    tarif2jam = tarifflat
    tarifover2jam = 3000
    tarifover6jam = 2000
    durasiatasenam = durasi - 6
    durasienamkebawah = durasi - (durasiatasenam)
    totalsementara = (tarif2jam) + ((durasienamkebawah - 2) * tarifover2jam) + ((durasiatasenam) * tarifover6jam)
else:
    print("Ada kesalahan")


if listrik == "y":
    if durasi > 2:
        if akhirpekan == "y":
            total = (totalsementara - 5000) * 1.2
        elif akhirpekan == "n":
            total = totalsementara - 5000
        else:
            print("Ada kesalahan")
    else:
        total = totalsementara
elif listrik == "n":
    if durasi > 2:
        if akhirpekan == "y":
            total = (totalsementara) * 1.2
        elif akhirpekan == "n":
            total = totalsementara
        else:
            print("Ada kesalahan")
    else:
        total = totalsementara
else:
    print("Ada kesalahan")

total = str(total)
print("Total tarif parkir adalah Rp" + total)