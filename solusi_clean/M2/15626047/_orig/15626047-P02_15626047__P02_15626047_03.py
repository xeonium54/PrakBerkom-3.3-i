# NIM / NAMA : 15626047 / JEREMIA ARISTA MATTHEW
# Tanggal: 14 Oktober 2026
# Deskripsi : Sistem Pengatur perjalanan kereta api

#Kamus
#jenis_A= str
#jenis_B= str
#jarak_A= int
#jarak_B= int
#speed_A= int
#speed_B= int
#TA= float
#TB= float

#KERETA A
jenis_A= str (input("Masukkan jenis Kereta A(Eksekutif/Bisnis/Kargo):"))
jarak_A= int (input("Masukkan jarak Kereta A (m):"))
speed_A= int (input("Masukkan kecepatan Kereta A (m/s):"))

#KERETA B
jenis_B= str (input("Masukkan jenis Kereta B(Eksekutif/Bisnis/Kargo):"))
jarak_B= int (input("Masukkan jarak Kereta B (m):"))
speed_B= int (input("Masukkan kecepatan Kereta B (m/s):"))

#Waktu tiba
TA= jarak_A/speed_A
TB= jarak_B/speed_B

#Selisih waktu tiba
if TA > TB:
    selisih= TA-TB

else :
    selisih = TB-TA

#Keamanan persimpangan
if selisih >= 30 :
    if TA<TB:
        print ("Jalur aman, kereta A melaju duluan tanpa berhenti")
    else :
        print ("Jalur aman, kereta B melaju duluan tanpa berhenti")

else :
    #Prioritas jenis kereta
        #Menentukan tingkat prioritas
        prio_map= {"Ekseskutif":3, "Bisnis": 2, "Kargo": 1}
        prio_A= prio_map[jenis_A]
        prio_B= prio_map[jenis_B]

        if prio_A > prio_B :
             prioritas = "A"
        elif prio_B > prio_A :
             prioritas = "B"
        else :
            if TA < TB :
                  prioritas = "A"
            elif TA > TB :
                  prioritas= "B"
            else :
                if jarak_A < jarak_B:
                 prioritas = "A"
                elif jarak_B < jarak_A:
                 prioritas= "B"
                else :
                    prioritas= "A"

if prioritas== "A":
     tunggu= (TA+40)-TB
     print ("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
     print (f"Kereta B harus berhenti dan menunggu selama {tunggu} detik")

else :
     tunggu= (TB+40)-TA
     print ("Konflik terdeteksi! Kereta B diprioritaskan melintas.")
     print (f"Kereta A harus berhenti dan menunggu selama {tunggu} detik")