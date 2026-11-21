#NIM/Nama   :Febrian Yafi Hakim 15626042 
#Tanggal    :30 September 2026
#Deskripsi  : Menghitung total biaya listrik yang terbuang akibat lampu menyala

#Disclaimer saya belum tau bagaimana format penulisan kamus yang baik dan benar...

#Input 
#Menggunakan float(input)) untuk memasukan data/angkanya
daya = float(input("masukkan daya lampu (watt): "))
lamanya = float(input("masukkan lamanya lampu menyala (jam): "))
tarif = float(input("masukkan tarif listrik (rupiah per kWh):"))

#Prosess
#menggunakan energi_kwh dan biaya sebagai variabel rumus
energi_kwh = (daya * lamanya) / 1000
biaya = energi_kwh * tarif

#Output
#untuk menampilkan hasil perhitungan menggunakan syntax print
#menggunakan float untuk menghitung biaya akhir karena ada test case yang menggunakan desimal
print(f"biaya lsitrik yang terbuang adalah Rp{float(biaya)}")