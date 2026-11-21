# Nama = Jihan Salsabila
# NIM = 15626002

# PROGRAM menentukan kereta yang diprioritaskan

# KAMUS
# Jenis_kereta_api_A: string
# Jarak_Kereta_A: interger
# Kecepatan_kereta_A: interger
# Waktu A: interger
# Jenis_kereta_api_B: string
# Jarak_Kereta_B: interger
# Kecepatan_kereta_B: interger
# Waktu B: interger

# ALGORITMA
Jenis_kereta_api_A=str(input("Masukkan jenis kereta api A(Eksekutif/Bisnis/Kargo):"))
Jarak_Kereta_A=int(input("Masukkan jarak kerta A(m):"))
Kecepatan_kereta_A=int(input("Masukkan kecepatan kereta A:"))
Waktu_A=Jarak_Kereta_A/Kecepatan_kereta_A
Jenis_kereta_api_B=str(input("Masukkan jenis kereta api B(Eksekutif/Bisnis/Kargo):"))
Jarak_Kereta_B=int(input("Masukkan jarak kerta B(m):"))
Kecepatan_kereta_B=int(input("Masukkan kecepatan kereta B:"))
Waktu_B=Jarak_Kereta_B//Kecepatan_kereta_B
if Waktu_A-Waktu_B>=30:
    print(f"Jalur aman.{Jenis_kereta_api_A} atau {Jenis_kereta_api_B} melintas duluan tanpa henti")
elif Waktu_A==Waktu_B:
    if Jenis_kereta_api_A==Eksekutif:
      Kereta_yang_melintas: Waktu_kereta_A
      Kereta_yang_mengalah: Waktu_kereta_B
      print("Kereta A melintas duluan")
    elif Jenis_kereta_api_A==Bisnis:
      if Jenis_kereta_api_B==Eksekutif:
        Kereta_yang_melintas: Waktu_kereta_B
        Kereta_yang_mengalah: Waktu_kereta_A
        print("Kereta B melintas duluan")
      elif Jenis_Kereta_api_A==Eksklusif:
         if Waktu_A>Waktu_B:
           Kereta_yang_melintas: Waktu_kereta_A
           Kereta_yang_mengalah: Waktu_kereta_B
           print("Kereta A melintas duluan")
         elif Waktu_A==Waktu_B:
            if Jarak_Kereta_A<Jarak_Kereta_B:
               Kereta_yang_melintas: Waktu_kereta_A
               Kereta_yang_mengalah: Waktu_kereta_B
               print("Kereta A melintas duluan")
            else:
               Kereta_yang_melintas: Waktu_kereta_A
               Kereta_yang_mengalah: Waktu_kereta_B
               print("Kereta A melintas duluan")
         else:
            Kereta_yang_melintas: Waktu_kereta_B
            Kereta_yang_mengalah: Waktu_kereta_A
            print("Kereta B melintas duluan")
            waktu_tunggu= Kereta_yang_melintas + 40 - Kereta_yang_mengalah
else:
   print("Kereta B melintas duluan")