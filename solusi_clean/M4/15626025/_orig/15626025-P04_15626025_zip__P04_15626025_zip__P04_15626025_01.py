# NIM/Nama: 15626025/Maria Amatussyafee Nurjaman
# Tanggal: 11/11/2026
# Deskripsi: manyederhanakan aspect ratio foto

# KAMUS
# l, t : int
# f : int
# i : int
# hasil : int

def fpb(a, b):
    # 
    hasil = 1
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            hasil = i
    return hasil

l = int(input("Masukan lebar foto (piksel): "))
t = int(input("Masukan tinggi foto (piksel): "))

f = fpb(l, t)
print("Aspect ratio disederhanakan menjadi " + str(l // f) + ":" + str(t // f))



