# NIM/Nama : 15626010/Faiz Abdurrahman
# Tanggal : 28/10/2026
# Deskripsi : Program ini mensimulasikan strategi investasi trailing stop pada pergerakan saham harian menggunakan konsep array untuk mencatat riwayat harga dan perulangan yang berjalan dinamis hingga kondisi trigger terpenuhi.

def main():
    persen_ts = float(input("Masukkan persentase trailing stop: "))

    harga_saham = []
    hari = 1

    # meminta input harga hari pertama
    h_pertama = float(input(f"Masukkan harga saham hari ke-{hari}: "))
    harga_saham.append(h_pertama)

    harga_beli = h_pertama
    puncak = h_pertama

    trigger = False
    harga_jual = 0
    hari_trigger = 0

    while not trigger:
        hari += 1
        h_hari_ini = float(input(f"Masukkan harga saham hari ke-{hari}: "))
        harga_saham.append(h_hari_ini)

        # perbarui puncak jika menemukan harga yang lebih tinggi
        if h_hari_ini > puncak:
            puncak = h_hari_ini

        # Hitung batas jual berdasarkan puncak saat ini
        batas_jual = puncak * (1 - persen_ts/100)

        # cek apakah trailing stop ter-trigger (harga hari ini turun mencapai atau di bawah batas jual)
        if h_hari_ini <= batas_jual:
            trigger = True
            harga_jual = h_hari_ini
            hari_trigger = hari

    keuntungan = harga_jual - harga_beli

    print(f"Trailing stop ter-trigger pada hari ke-{hari_trigger} dengan harga Rp{harga_jual}")
    print(f"Harga puncak: Rp{puncak}")
    print(f"Batas jual (trailing stop {persen_ts}%): Rp{batas_jual}")
    print(f"Keuangan : Rp{keuntungan}")

if __name__ == "__main__":
    main()