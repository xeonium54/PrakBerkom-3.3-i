# NIM/Nama : 15626041/Dean Navarro Gratia Plena
# Tanggal : 30 September 2026
# Deskripsi : Menghitung konsentrasi akhir campuran

kons_larutan_1 = int(input("Masukkan konsentrasi larutan pertama (persen):"))
vol_larutan_1 = int(input("Masukkan volume larutan pertama (ml):"))
kons_larutan_2 = int(input("Masukkan konsentrasi larutan kedua (persen):"))
vol_larutan_2 = int(input("Masukkan volume larutan kedua (ml):"))
kons_larutan_3 = int(input("Masukkan konsentrasi larutan ketiga (persen):"))
vol_larutan_3 = int(input("Masukkan volume larutan ketiga (ml):"))

bagian_atas = (kons_larutan_1*vol_larutan_1)+(kons_larutan_2*vol_larutan_2)+(kons_larutan_3*vol_larutan_3)
bagian_bawah = vol_larutan_1+vol_larutan_2+vol_larutan_3

konsentrasi_akhir = bagian_atas/bagian_bawah

print(f'Konsentrasi akhir larutan campuran {konsentrasi_akhir} persen')