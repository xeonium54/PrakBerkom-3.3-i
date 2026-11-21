# NIM = 15626033 
# Tanggal = 14 oktober 2026
# deskripsi = kereta yang diprioritaskan melintas

prioritas_kelas = {"eksekutif": 3, "bisnis": 2, "kargo": 1}

#kereta A
print("== input data kereta A ===")
jenis_A = input("jenis kereta A (eksekutif/bisnis/kargo): ").strip()
jarak_A = float(input("jarak kereta A ke persimpangan (meter): "))
kecepatan_A = float(input("kecepatan kereta A (m/s): "))

#kereta B
print("\n=== input data kereta B ===")
jenis_B = input("jenis kereta B (eksekutif/bisnis/kargo): ").strip()
jarak_B = float(input("jarak kereta B ke persimpangan (meter): "))
kecepatan_B = float(input("kecepatan kereta B (m/s): "))

waktu_A = jarak_A / kecepatan_A
waktu_B = jarak_B / kecepatan_B

kereta = {
    "A": {"nama": "kereta A", "jenis": jenis_A, "jarak": jarak_A, "kecepatan": kecepatan_A, "waktu": waktu_A},
    "B": {"nama": "kereta B", "jenis": jenis_B, "jarak": jarak_B, "kecepatan": kecepatan_B, "waktu": waktu_B}
}

selisih_waktu = waktu_A - waktu_B
if selisih_waktu < 0:
    selisih_waktu = -selisih_waktu 

print("\n=== hasil analisi jalur ===")
if selisih_waktu >= 30.0:
    if waktu_A < waktu_B:
        print("jalur aman. [kereta A] melintas duluan tanpa henti.")
    else: 
        print("jalur aman. [kereta B] melintas duluan tanpa henti.")

else:
    print("terjadi potensi konflik jalur!")
    kereta_prioritas = None
    if prioritas_kelas[jenis_A] > prioritas_kelas[jenis_B]:
        kereta_prioritas = "A"
    elif prioritas_kelas[jenis_B] > prioritas_kelas[jenis_A]:
        kereta_prioritas = "B"
    else:
        if waktu_A < waktu_B:
            kereta_prioritas = "A"
        elif waktu_B < waktu_A:
            kereta_prioritas = "B"
        else:
            if jarak_A < jarak_B:
                kereta_prioritas = "A"
            elif waktu_B < jarak_A:
                kereta_prioritas = "B"
            else:
                kereta_prioritas = "A" 

kereta_mengalah = "B" if kereta_prioritas == "A" else "A"
waktu_menunggu = (kereta[kereta_prioritas]["waktu_tiba"] + 40.0) - kereta[kereta_mengalah]["waktu_tiba"]

print(f"kereta diprioritaskan melintas: {kereta[kereta_prioritas]['nama']}")
print(f"kereta yang harus mengalah: {kereta[kereta_mengalah]['nama']}")
print(f"waktu tunggu {kereta[kereta_mengalah]['nama']}: {waktu_tunggu:.2f} detik")
        

