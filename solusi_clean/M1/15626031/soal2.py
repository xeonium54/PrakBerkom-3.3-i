# Alfathir Sangkara Anindya
# 15626031
# program menghitung konsentrasi terakhir dari larutan tersebut

c_pertama=20
v_pertama=200
c_kedua=30
v_kedua=150
c_ketiga=50
v_ketiga=150


c_pertama=float(input("masukan konsentrasi larutan pertama (persen):"))
v_pertama=float(input("masukan volume larutan pertama (ml):"))


c_kedua=float(input("masukan konsentrasi larutan kedua (persen):"))
v_kedua=float(input("masukan volume larutan kedua (ml):"))

c_ketiga=float(input("masukan konsentrasi larutan ketiga (persen):"))
v_ketiga=float(input("masukan volume larutan ketiga (ml):"))

akhir=(c_pertama*v_pertama+c_kedua*v_kedua+c_ketiga*v_ketiga)/(v_pertama + v_kedua + v_ketiga)
print(f"Konsentrasi akhir larutan campuran adalah {akhir :2f}persen") 