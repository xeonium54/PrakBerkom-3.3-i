# NIM/NAMA : 15626004/Nirmala Rahma Maulida
# Tanggal : 30 September 2026
# Deksripsi : Pada program ini tuan mik dibantu oleh python untuk menghitung biaya listrik yang terbuang dengan mengimput setiap nilai yang diketahui.

# Biaya listrik

# KAMUS
# p, b , c : int 

# proses 
p = int(input("masukkan daya lampu (watt): "))
b = int(input("masukkan lama lampu menyala (jam): "))
c = int(input("masukkan tarif listrik (rupiah per kWh): "))

energi = p * b / 1000
biaya = energi * c

# output
print("biaya listrik yang terbuang", biaya) 