# Nama = Jihan Salsabila
# NIM = 15626002

# PROGRAM mencari keuntungan dan kerugian

# KAMUS
# Batas_Jual = float
# Harga Saham = Intereger
# Harga Puncak = intreger

# ALGORITMA
Persentase_Trailing_Stop = int(input("Masukkan persentase trailing stop:"))
Harga_Saham = int(input("Masukkan harga saham"))

while X>= Batas_Jual:
    Harga_Saham = int(input("Masukkan harga saham:"))
    if Harga_Saham> Harga_Saham:
        Harga_Puncak = Harga_Saham
Batas_Jual = Harga_puncak*1-Persentase_Trailing_Stop/100
Print(f"Maka Batas jualnya sebesar{Batas_Jual}")