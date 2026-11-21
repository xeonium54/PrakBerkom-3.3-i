# Nama/NIM : Nu'man Hanania Fawwaz/15626052
# Tanggal : 14/10/2026
# Deskripsi : Praktikum #2 Analisis kasus (Percabangan)

# Program memvalidasi skor ujian peserta
# Kamus
# Nilai = int
# if (0,100): skor valid
# else : skor tidak valid

# Algoritma
Nilai = int(input('Masukkan nilai peserta: '))
if Nilai in range(0,101):
  print('skor valid, dapat diinput ke sistem')
else :
  print('skor tidak valid, perlu diperiksa ulang')