# NIM/Nama : Naila Rahmah Zhafirah
# Tanggal : Rabu, 30 September 2026
# Deskripsi : Menghitung konsentrasi akhir larutan campuran

data = {"konsentrasi1": 0,
        "volume1": 0,
        "konsentrasi2": 0,
        "volume2":  0,
        "konsentrasi3": 0,
        "volume3": 0,
        "konsentrasi_akhir": 0}


data["konsentrasi1"] = int(input("Masukkan konsentrasi pertama (persen): "))
data["volume1"] = int(input("Masukkan volume pertama (ml): "))

data["konsentrasi2"] = int(input("Masukkan konsentrasi kedua (persen): "))
data["volume2"] = int(input("Masukkan volume kedua (ml): "))

data["konsentrasi3"] = int(input("Masukkan konsentrasi ketiga (persen): "))
data["volume3"] = int(input("Masukkan volume ketiga (ml): "))

data["konsentrasi_akhir"] = ((data["konsentrasi1"] * data["volume1"]) + (data["konsentrasi2"] * data["volume2"]) + (data["konsentrasi3"] * data["volume3"])) / (data["volume1"] + data["volume2"] + data["volume3"])

print(Konsentrasi akhir larutan campuran adalah"), data[konsentrasi_akhir]. "persen")