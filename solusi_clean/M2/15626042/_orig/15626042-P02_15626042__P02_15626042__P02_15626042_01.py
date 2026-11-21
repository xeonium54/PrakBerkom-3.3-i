#Nama : Febrian Yafi Hakim
#NIM : 15626042
#Problem 1

#Jika skor berada pada rentang 0 hingga 100 (inklusif), tampilkan "Skor valid, dapat diinput ke sistem"
#Jika tidak, tampilkan "Skor tidak valid, perlu diperiksa ulang"

skor = int(input("masukkan skor ujian: "))

if (skor >= 0 and skor <= 100):
    print("Skor valid, dapat diinput ke sistem")
else:
    print("Skor tidak valid, perlu periksa ulang")