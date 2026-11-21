# NIM/Nama : 15626050/Yohanes Yoel Christopher Naibaho
# Tanggal : 30-9-2026
# Deskripsi : Menghitung Total Biaya Listrik Akibat Lampu Yang Menyala

# KAMUS
# Watt,Jam,Tarif, = float 
# Biaya = float

# ALGORITMA
Watt = float(input("Masukkan Daya Lampu: "))
Jam = float(input("Masukkan Lama Lampu Menyala: "))
Tarif = float(input("Masukkkan Tarif Listrik(Rupiah/Kwh): "))
Biaya = (((Watt*Jam)/(1000)) * (Tarif))
print("Biaya yang harus dibayarkan", Biaya ,"Rupiah")
