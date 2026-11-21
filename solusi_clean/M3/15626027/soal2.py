#NIM/Nama : 15626027/Muhammad Faiz Dhiaul Haq
#Tanggal : Rabu, 28 Oktober 2026
#Deskripsi : Mensimulasikan strategi Trailing Stop Saham Pak Mik 

persen = float(input("Masukkan persentase Traling Stop: "))

harga_awal = float(input("Masukkan harga saham hari ke-1: "))
harga = harga_awal
puncak = harga_awal
hari = 1

while True:
    harga = float(input(f"Masukkan harga saham hari ke-{hari + 1}: "))
    hari += 1

    if harga > puncak:
        puncak = harga

    batas_jual = puncak * (1 - persen / 100)

    if harga <= batas_jual:
        print(f"Trailing stop ter-trigger pada hari ke -{hari} dengan harga Rp{harga:.0f}")
        break

print(f"Harga puncak: Rp{puncak:.0f}")
print(f"Batas Jual (Traling Stop {persen:g}%): Rp{batas_jual:.2f}")
print(f"Keuntungan atau kerugian : Rp {harga - harga_awal:.0f}")
