# Nama : Alfathir Sangkara Anindya
# NIM : 15626031
# Tanggal :11/11/2026
# Deskripsi : program Prediksi Nilai UAS

N = float(input("Masukkan sisa waktu: "))

t = []
for i in range(4):
    a = float(input("Masukkan durasi untuk modul ke-{}: ".format(i+1)))
    while a <= 0:
        print("Durasi harus lebih dari 0")
        a = float(input("Masukkan durasi untuk modul ke-{}: ".format(i+1)))
    t.append(a)

T = [0, 0, 0, 0]
E = 100

while N > 0:

    if E <= 0:
        print("Energi habis, Tuan Ky harus tidur")
        E = E + N * 12.5
        if E > 100:
            E = 100
        N = 0

    else:
        print("1. Belajar")
        print("2. Tidur")

        pilih = int(input("Pilih tindakan (1/2): "))

        while pilih != 1 and pilih != 2:
            print("Pilihan tidak tersedia!")
            pilih = int(input("Pilih tindakan (1/2): "))

        if pilih == 1:
            modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))

            while modul < 1 or modul > 4:
                print("Modul tidak tersedia!")
                modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))

            lama = float(input("Masukkan durasi belajar: "))

            while lama <= 0:
                print("Durasi harus lebih dari 0")
                lama = float(input("Masukkan durasi belajar: "))

            if lama > N:
                lama = N

            if lama > E / 5:
                lama = E / 5

            T[modul-1] = T[modul-1] + lama

            E = E - lama * 5
            N = N - lama

            print("Energi sekarang:", E)
            print("Sisa waktu:", N)

        else:
            E = E + N * 12.5

            if E > 100:
                E = 100

            print("Tuan Ky tidur selama", N, "jam")
            print("Energi sekarang:", E)

            N = 0

jumlah = 0

for i in range(4):
    if T[i] > t[i]:
        T[i] = t[i]

    jumlah = jumlah + T[i] / t[i]

S = (jumlah / 4) * ((100**2 - (100-E)**2) / 100)

print(" ")
print("Durasi belajar modul 1:", T[0])
print("Durasi belajar modul 2:", T[1])
print("Durasi belajar modul 3:", T[2])
print("Durasi belajar modul 4:", T[3])
print("Energi akhir:", E)
print("Prediksi nilai UAS:", S)
