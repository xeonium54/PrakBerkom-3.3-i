#15626039/Khalif Aufar A
#11 November 2026
#No 1, Menghitung ukuran foto

#Kamus
#lebar,tinggi,faktor,rl,rt,a,b = int
#hl = str

def fpb(a,b):
    while b!=0:
        a,b = b, a%b
    return a
def main():
 lebar = int(input("Masukkan lebar foto (Px):"))
 tinggi = int(input("Masukkan tinggi foto (Px):"))

 faktor = fpb(lebar,tinggi)

 rl = lebar // faktor
 rt = tinggi // faktor

 hl = str(rl) + ":" + str(rt)

 print("Aspect ratio disederhanakan menjadi:" + hl)
main()