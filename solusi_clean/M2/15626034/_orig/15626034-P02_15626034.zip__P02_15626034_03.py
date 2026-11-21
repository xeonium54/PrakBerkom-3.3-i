#NIM/NAMA : 15626034/Ahmad Zaky 
#Tanggal : 14/10/2026
#Deskripsi :Program Menentukan kereta yang di priotitaskan melintas serta waktu tuggu bagi kereta yang harus mengalah

#kamus
    #A : integer
    #B : integer
DA = int
DB = int
VA = int
VB = int

def atur_perjalanan_kereta():
     jenis_A = input("Masukkan jenis kereta A (eksekutif/bisnis/kargo): ")
     DA = int(input("Masukkan jarak kereta A dari persimpangan (meter): "))
     VA = int(input("Masukkan kecepatan kereta A (m/s): "))
     jenis_B = input("Masukkan jenis kereta B (eksekutif/bisnis/kargo): ")   
     DB = int(input("Masukkan jarak kereta B dari persimpangan (meter): "))  
     VB = int(input("Masukkan kecepatan kereta B (m/s): "))  
     
TA = DA/VA
TB = DB/VB

selisih_TA_TB = (TA - TB) if TA >= TB else (TB - TA)

print(f"Waktu tiba Kereta A: {TA:.1f} detik")
print(f"Waktu tiba Kereta B: {TB:.1f} detik")
print("-"*40)

if selisih_TA_TB >= 30 :
    print("Jalur aman. Tidak ada risiko tabrakan di persimpangan.")
    if TA < TB:
        print("Kereta A melintas duluan tanpa henti.")
    else: 
        print("Kereta B melintas duluan tanpa henti.") 
    

print("Jalur berpotensi tabrakan. Perlu pengaturan prioritas melintas.")
bobot_prioritas = {'eksekutif': 3, 'bisnis': 2, 'kargo': 1}
prioritas_A = bobot_prioritas.get(jenis_A. lower(), 0)
prioritas_B = bobot_prioritas.get(jenis_B.lower(), 0)

if prioritas_A > prioritas_B:
        kereta_prioritas = "A"
        kereta_mengalah = "B"
        T_prioritas, T_mengalah = TA, TB
elif prioritas_B > prioritas_A:
        kereta_prioritas = "B"
        kereta_mengalah = "A"
        T_prioritas, T_mengalah = TB, TA
else:
        if TA < TB:
            kereta_prioritas = "A"
            kereta_mengalah = "B"
            T_prioritas, T_mengalah = TA, TB
        elif TB < TA:
            kereta_prioritas = "B"
            kereta_mengalah = "A"
            T_prioritas, T_mengalah = TB, TA
        else:
            if DA < DB:
                  kereta_prioritas = "A"
                  kereta_mengalah = "B"
                  T_prioritas, T_mengalah = TA, TB 
            elif DB < DA:
                    kereta_prioritas = "B"
                    kereta_mengalah = "A"
                    T_prioritas, T_mengalah = TB, TA   
            else :
                   kereta_prioritas = "A"
                   kereta_mengalah = "B"
                   T_prioritas, T_mengalah = TA, TB

waktu_tunggu = T_prioritas + 40 - T_mengalah
print(f"Kereta yang di prioritaskan melintas: Kereta {kereta_prioritas}")
print(f"Kereta yang harus mengalah: Kereta {kereta_mengalah}")
print(f"Waktu tunggu bagi kereta yang mengalah: {waktu_tunggu:.1f} detik")

if __name__ == "__main__":
    atur_perjalanan_kereta()
    
    