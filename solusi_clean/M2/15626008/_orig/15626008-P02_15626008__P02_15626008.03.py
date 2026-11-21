# NIM/NAMA : Arya Satya Anggara
# Tanggal : 14 Oktober 2026
# Deskripsi : Program ini dibuat untuk menentukan kereta mana yang berhak melintas lebih dahulu di persimpangan rel berdasarkan waktu tiba, jenis kereta, dan jarak ke persimpangan. Jika selisih waktu tiba minimal 30 detik, jalur dinyatakan aman. Jika kurang dari 30 detik, program menentukan kereta yang diprioritaskan dan menghitung waktu tunggu kereta lainnya. Program menggunakan percabangan if-elif-else tanpa menggunakan fungsi abs()

jenisA = input("Masukkan jenis Kereta A: ")
DA = int(input("Masukkan jarak Kereta A: "))
VA = int(input("Masukkan kecepatan Kereta A: "))

jenisB = input("Masukkan jenis Kereta B: ")
DB = int(input("Masukkan jarak Kereta B: "))
VB = int(input("Masukkan kecepatan Kereta B: "))

TA = DA / VA
TB = DB / VB

if TA > TB:
    selisih = TA - TB
else:
    selisih = TB - TA

if selisih >= 30:
    if TA < TB:
        print("Jalur aman, Kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman, Kereta B melintas duluan tanpa henti.")
else:
    if jenisA == jenisB:
        if TA < TB:
            prioritas = "A"
        elif TB < TA:
            prioritas = "B"
        elif DA < DB:
            prioritas = "A"
        elif DB < DA:
            prioritas = "B"
        else:
            prioritas = "A"
    elif jenisA == "eksekutif":
        prioritas = "A"
    elif jenisB == "eksekutif":
        prioritas = "B"
    elif jenisA == "bisnis":
        prioritas = "A"
    else:
        prioritas = "B"

    if prioritas == "A":
        waktu_tunggu = TA + 40.0 - TB
        print("Terjadi potensi konflik jalur.")
        print("Kereta A melintas duluan.")
        print("Kereta B harus berhenti.")
        print(f"Kereta B harus berhenti dan menunggu selama: {waktu_tunggu:.1f} detik")
    else:
        waktu_tunggu = TB + 40.0 - TA
        print("Terjadi potensi konflik jalur.")
        print("Kereta B melintas duluan.")
        print("Kereta A harus berhenti.")
        print(f"Kereta A harus berhenti dan menunggu selama: {waktu_tunggu:.1f} detik")