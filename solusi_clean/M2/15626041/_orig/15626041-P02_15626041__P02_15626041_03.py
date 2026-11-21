# NIM/Nama : 15626041/Dean Navarro Gratia Plena
# Tanggal : 14 Oktober 2026
# Deskripsi : 

jeniskeretaA = input("Masukkan jenis kereta A (eksekutif/kargo/bisnis): ")
jarakkeretaA = int(input("Masukkan jarak kereta A (m): "))
vkeretaA = int(input("Masukkan kecepatan kereta A (m/s): "))

jeniskeretaB = input("Masukkan jenis kereta B (eksekutif/kargo/bisnis): ")
jarakkeretaB = int(input("Masukkan jarak kereta B (m): "))
vkeretaB = int(input("Masukkan kecepatan kereta B (m/s): "))

if jeniskeretaA=="eksekutif":
 kelasA=3
elif jeniskeretaA=="bisnis":
 kelasA=2
elif jeniskeretaA=="kargo":
 kelasA=1

if jeniskeretaB=="eksekutif":
 kelasB=3
elif jeniskeretaB=="bisnis":
 kelasB=2
elif jeniskeretaB=="kargo":
 kelasB=1

tA = jarakkeretaA/vkeretaA
tB = jarakkeretaB/vkeretaB

waktuperselisihan = tA-tB
if waktuperselisihan<0:
 mutlakperselisihan=waktuperselisihan*-1
else:
 mutlakperselisihan=waktuperselisihan*1


if mutlakperselisihan>30.0:
 if tA<tB:
  print("Jalur aman, Kereta A melintas lebih dahulu tanpa henti")
 elif ta>tB:
  print("Jalur aman, Kereta B melintas lebih dahulu tanpa henti")
elif waktuperselisihan<30.0:
 if kelasA>kelasB:
  waktutunggu = (tA+40)-tB
  print("Konflik terdeteksi, Kereta A diprioritaskan melintas.")
  print(f"Kereta B harus berhenti dan menunggu selama {waktutunggu} detik")
 elif kelasA<kelasB:
  waktutunggu = (tB+40)-tA
  print("Konflik terdeteksi, Kereta B diprioritaskan melintas.")
  print(f"Kereta A harus berhenti dan menunggu selama {waktutunggu} detik")
 elif kelasA==kelasB and jarakkeretaA<jarakkeretaB:
  waktutunggu = (tA+40)-tB
  print("Konflik terdeteksi, Kereta A diprioritaskan melintas.")
  print(f"Kereta B harus berhenti dan menunggu selama {waktutunggu} detik")
 elif kelasA==kelasB and jarakkeretaA>jarakkeretaB:
  waktutunggu = (tB+40)-tA
  print("Konflik terdeteksi, Kereta B diprioritaskan melintas.")
  print(f"Kereta A harus berhenti dan menunggu selama {waktutunggu} detik")
 elif kelasA==kelasB and jarakkeretaA==jarakkeretaB:
  waktutunggu = (tA+40)-tB
  print("Konflik terdeteksi, Kereta A diprioritaskan melintas.")
  print(f"Kereta B harus berhenti dan menunggu selama {waktutunggu} detik")
