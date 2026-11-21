Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> daya = float(input("Masukkan daya lampu (watt): "))
Masukkan daya lampu (watt): 65
>>> lama = float(input("Masukkan lama lampu menyala (jam): "))
Masukkan lama lampu menyala (jam): 20
>>> tarif = float(input("Masukkan tarif listrik (rupiah per kWh):"))
Masukkan tarif listrik (rupiah per kWh):1500
>>> energi = (w * j) / 1000
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    energi = (w * j) / 1000
NameError: name 'w' is not defined
>>> energi = (daya * lama) / 1000
>>> biaya = energi * tarif
>>> print(f"Biaya listrik yang terbuang adalah Rp{biaya:g}")
Biaya listrik yang terbuang adalah Rp1950
