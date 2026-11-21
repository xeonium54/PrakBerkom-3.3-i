#P03_15626029_02
#Hanif MAhib YN
#15626029
#desc: trailing stop saham tuan MIK

# KAMUS
# p = flost
# d, lim, pric=int

p=float(input("masukkan persentase trailing stop:"))

d=1
pric=int(input("MAsukkan harga saham hari ke-",d ))
sold=False
peak=price

while not sold :
    d+= 1
    prics=int(input("mauskkan harga saham hari ke-",d))
    lim =peak*(1-p/100)
    if prics<=lim:
        sold=True
    elif prics>price:
        peak=prics

print("trailing stop tertrigger pada hari ke",d,"dengan harga",prics)
print("harga puncak:",peak)
print("batas jual (trailing stop",p,"%):",prics)

beda=prics-pric
if beda>=0:
    print("keuntungan :",beda)
else:
    print("kerugian:",beda)