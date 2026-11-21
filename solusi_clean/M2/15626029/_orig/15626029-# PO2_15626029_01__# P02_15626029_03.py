# P02_15626029_03
# HANIF MAHIB YN/15626029
# Desc : Program kereta prioritas dan waktu tunggu

#KAMUS
# vA,vB,tA, tB, rA,rB, tw= float
#jenisA,jenisB=string

jenisA = str(input("Jenis kereta A"))
jenisB=str(input("Jenis kereta B"))
rA=float(input("Jarak kereta A (m): "))
rB=float(input("Jarak kereta B(m): "))
vA=float(input("kec A (m/s) ; " ))
vB=float(input("kec B(m/s): "))

tA=rA/rA
tB=rB/vB

if jenisA=="Bisnis" and jenisB=="Eksekutif":
    tw=tA-tB
    if tw<0:
        tw= tw1 = tB-tA 
        if tw1<30:
            print("Potensi konflik") and tw =tw+tA
        else:
            print("Jalur aman")
            
if jenisA=="Bisnis" and jenisB=="Kargo":
    tw=tA-tB
    if tw<0:
        tw= tw1 = tB-tA 
        if tw1<30:
            print("Potensi konflik")
        else:
            print("Jalur aman")
            
if jenisA=="Eksekutif" and jenisB=="Kargo":
    tw=tA-tB
    if tw<0:
        tw= tw1 = tB-tA 
        if tw1<30:
            print("Potensi konflik") and tw = tw+tA
        else:
            print("Jalur aman")
            
if jenisA=="Kargo" and jenisB=="Eksekutif":
    tw=tB-tA
    if tw<0:
        tw = tw2 = tA-tB 
        if tw2<30:
            print("Potensi konflik") and tw=tw+tB
        else:
            print("Jalur aman")
            
if jenisA=="Eksekutif" and jenisB=="Bisnis":
    tw=tB-tA
    if tw<0:
        tw= tw2 = tA-tB 
        if tw2<30:
            print("Potensi konflik") and tw=tw+tB
        else:
            print("Jalur aman")
            
if jenisA=="Kargo" and jenisB=="Bisnis":
    tw=tB-tA
    if tw<0:
        tw= tw2 = tB-tA 
        if tw2<30:
            print("Potensi konflik") and tw=tw+tB
        else:
            print("Jalur aman")

if jenisA == jenisB:
 tw = tA-tB
 if tw>0:
     tw =tw3=tB-tA
     if tw3>30:
         print("Jalur aman")
     else:
         print("Potensi konflik") and tA-tB

print("Kereta harus menunggu",tw)
        
