# NIM/Nama  : 15626047/Jeremia Arista Matthew Sugiarto
# Tanggal   : 11 November 2026
# Deskripsi : Menghitung skor kekuatan PIn dan banyaknya tiap kategori

#Kamus
N=int

#Menghitung skor
def hitung_skor_dan_kategori(pin) :
    skor = 0

    #Poin digit unik
    digit_unik=[]
    for char in pin:
        if char >='0' and char<= '9':
            if char not in digit_unik:
                digit_unik.append(char)
    skor += len(digit_unik)*4

    #HurufBesar
    kapital = False
    for char in pin:
        if 'A' <= char <= 'Z':
            kapital = True
            break
    if kapital:
        skor += 10

    #Panjang Pin 
    n= len(pin)
    if n>=8 :
        skor += 15
    elif 6 <= n <= 7 :
        skor += 5

    #Digit urutan
    for i in range(len(pin)-1):
        c1= pin[i]
        c2= pin[i+1]
        if ('0' <= c1 <= '9') and ('0' <= c2 <= '9'):
            val1= int(c1)
            val2= int(c2)
            if abs(val1-val2) == 1:
                skor -=5

    #Menentukan kategori
    if skor >= 40:
        kategori = "Kuat"
    elif 20<= skor < 40:
        kategori = "Sedang"
    else:
        kategori = "Lemah"

    return skor, kategori

#Algoritma UI
N= int (input("Masukkan jumlah kandidat PIN (N):"))
kuat_count=0
sedang_count=0
lemah_count=0

for i in range(1,N+1):
    pin = input(f"Kandidat PIN ke-{i}: ")
    skor, kategori = hitung_skor_dan_kategori(pin)
    print(f"PIN ke-{i} skornya {skor}, tergolong {kategori}.")
    if kategori == "Kuat":
        kuat_count +=1
    elif kategori == "Sedang":
        sedang_count +=1
    else:
        lemah_count +=1

print (f"Rekap: Kuat {kuat_count}, Sedang {sedang_count}, Lemah {lemah_count}")