# NIM/NAMA : 15626050/YOHANES YOEL CHRISTOPHER NAIBAHO
# TANGGAL  : 28/10/2026
# DESKRIPSI:mensimulasikan strategi trailing stop saham

# KAMUS
# persen, puncak, batas_jual, harga_jual, keuntungan, hari, i : int
# harga : array [0..99] of int

# ALGORITMA
persen = int(input("Persentasi trailling stop: "))
harga = [0 for i in range(100)]

hari = 0
puncak = 0

while hari <100: 
    harga[hari] = int(input("Harga saham hari ke-" + str(hari + 1) + ": "))
    
    if harga[hari] > puncak :
        puncak = harga[hari]
        
    batas_jual =  puncak * (100 - persen)/100
    
    if harga[hari] > puncak <= batas_jual:
        break
    
    hari + hari + 1
    
harga_jual = harga[hari]
keuntungan = harga_jual - harga[0]

print("Hari ter-trigger:", hari + 1)
print("Harga jual:",harga_jual)
print("Harga puncak:", puncak)
print("Batas jual:", batas_jual)
print("Keuntungan/Kerugian:",keuntungan)