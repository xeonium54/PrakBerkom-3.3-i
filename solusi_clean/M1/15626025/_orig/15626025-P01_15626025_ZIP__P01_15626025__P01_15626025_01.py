# NIM/Nama : 15626025/Maria Amatussyafee Nurjaman
# Tanggal : 30 September 2026
# Deskripsi : Menghitung total biaya listrik yang terbuang 

# PROGRAM : Problem 1

# KAMUS 
# daya lampu, lama lampu menyala, tarif listrik : integer
# energi, biaya : integer

#ALGORITMA 
daya_lampu = int(input("Masukan daya lampu (watt): "))
lama_lampu_menyala = int(input("Masukan lama lampu menyala (jam): "))
tarif_listrik = int(input("Masukan tarif listrik (rupiah per kwh): "))

energi = ((daya_lampu * lama_lampu_menyala) / 1000)
biaya = energi * tarif_listrik

print(f"Total biaya listrik yang terbuang adalah {biaya} rupiah")