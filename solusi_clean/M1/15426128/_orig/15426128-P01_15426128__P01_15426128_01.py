# Nim/Nama : 15426128/Fathir Sulihansyah
# Tanggal  : 30 September 2026
# Deskripsi: Tuan Mik mencari total listrik yang terbuang

# w = daya lampu (dalam Watt)
# j = durasi nyala lampu (dalam jam)
# r = tarif listrik (dalam rupiah)
# w*j/1000 {Untuk mencari energi yang terbuang}
# energi_kwh*r {untuk mencari biaya listrik yang terbuang}

w = float(input("Masukkan daya lampu (Watt): "))
j = float(input("Masukkan durasi lampu menyala (jam): "))
r = float(input("Masukkan tarif listrik(rupiah/Kwh): "))

energi_kwh = (w*j)/1000
total_biaya = energi_kwh * r
print(f"Total biaya listrik yang terbuang adalah: Rp {total_biaya: .2f} ")

    