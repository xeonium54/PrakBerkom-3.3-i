# NIM/Nama : 15626052/Nu'man Hanania Fawwaz
# Tanggal : 11/11/2026
# Deskripsi : Subprogram

# Program PrediksiNilaiUas
# Kamus
# Sisa_waktu : int
# durasi_modul : int
# pilih_tindakan (1/2) : int
# pilih_modul_yg_tersedia (1-4) : int
# durasi_modul : int

# Algoritma
def S(T,t,E):
  for i in range (1,5):
    S = T[i]/t[i]/4 * 100*100 - (100-E)*(100-E)/100
    return S
s = int(input('masukkan sisa waktu: '))
for i in range (1,5):
  T = int(input(f'masukkan durasi untuk modul ke{i}: '))
print('1. Belajar')
print('2. Tidur')
p = int(input('masukkan pilihan tindakan (1/2): '))
if p == 1 or p == 2:
  q = int(input('pilih modul yang ingin dipelajari (1-4): '))
  t = int(input('masukkan durasi belajar: '))
else :
  r = (f'pilihan tidak tersedia! Pilih tindakan (1/2): ')
if t > 1:
  E = 12.5
elif t = 1:
  E = 5
else :
  E = 0
print(f'Prediksi nilai UAS: {S(T,t,E)}')

# Cuman segini doang ngertinya :(