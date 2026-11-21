Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> c1 = float(input("Masukkan konsentrasi larutan pertama (persen): "))
Masukkan konsentrasi larutan pertama (persen): 20
>>> v1 = float(input("Masukkan volume larutan pertama (ml): "))
Masukkan volume larutan pertama (ml): 200
>>> c2 = float(input("Masukkan konsentrasi larutan kedua (persen): "))
Masukkan konsentrasi larutan kedua (persen): 30
>>> v2 = float(input("Masukkan volume larutan kedua (ml): "))
Masukkan volume larutan kedua (ml): 150
>>> c3 = float(input("Masukkan konsentrasi larutan ketiga (persen): "))
Masukkan konsentrasi larutan ketiga (persen): 50
>>> v3 = float(input("Masukkan volume larutan ketiga (ml): "))
Masukkan volume larutan ketiga (ml): 150
>>> c_akhir = (c1 * v1 + c2 * v2 + c3 * v3) / (v1 + v2 + v3)
>>> print(f"Konsentrasi akhir larutan campuran adalah {c_akhir:.2f} persen")
Konsentrasi akhir larutan campuran adalah 32.00 persen
