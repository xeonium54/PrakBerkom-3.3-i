# NIM/Nama : 15626012/Muhammad Dzaky Nouvaldi
# Tanggal: 11 November 2026
# Deskripsi: Program PIN

# KAMUS
# total_skor_pin  : int 
# pilihan_kategori : str 
# n, kuat, sedang, lemah : int 
# pin, kategori : str

def total_skor_pin(pin):
    # KAMUS 
    # skor, pen, i, d1, d2, panjang
    # digit_terlihat : list of char 
    # char, c1, c2 : char 
    # kapital : boolean 

    skor = 0

    #
    digit_terlihat = []
    for char in pin:
        if '0' <= char <= '9': 
            if char not in digit_terlihat:
                digit_terlihat.append(char)
    skor += len(digit_terlihat) * 4 

    
    #
    kapital = False 
    for char in pin:
        if 'A' <= char <= 'Z':
            kapital = True 
            skor += 10


    # 
    panjang = len(pin)
    if panjang >= 8:
        skor += 15
    elif 6 <= panjang <= 7:
        skor += 5
    else:
        skor += 0 


    #
    pen = 0 
    for i in range(len(pin) -1):
        c1 = pin[i]
        c2 = pin[i+1]
        if ('0' <= c1 <= '9') and ('0' <= c2 <= '9'):
            d1 = int(c1)
            d2 = int(c2)
            if abs(d1 - d2) == 1:
                pen += 5

    skor -= pen 
    return skor


def pilihan_kategori(skor):

    if skor >= 40:
        return 'kuat'
    elif skor >= 20:
        return 'sedang'
    else: 
        return 'lemah'



n = int(input('masukkan pin yang akan dicoba: '))

kuat = 0
sedang = 0
lemah = 0

for i in range(1, n+1):
    pin = input(f'masukkan pin ke-{i}: ')
    skor = total_skor_pin(pin)
    kategori = pilihan_kategori(skor)

    if kategori == 'kuat':
        kuat += 1
    elif kategori == 'sedang':
        sedang += 1
    else:
        lemah += 1



    print(f'pin ke-{i} skornya {skor}, masuk kategori {kategori}')

print (f'kuat {kuat}, sedang {sedang}, lemah {lemah}')



