#15626008/Arya Satya Anggara
30 September 2026
Praktikum ini bertujuan untuk menghitung biaya listrik yang terbuang berdasarkan daya lampu, lama lampu menyala, dan tarif listrik per kWh. Perhitungan dilakukan dengan menentukan energi listrik yang digunakan, kemudian mengalikannya dengan tarif listrik untuk mendapatkan total biaya.

w = float(input("Masukkan daya lampu (watt): "))
... j = float(input("Masukkan lama lampu menyala (jam): "))
... r = float(input("Masukkan tarif listrik (rupiah per kWh): "))
...
... energi = (w * j) / 1000
... biaya = energi * r
...
... if biaya.is_integer():
...     print(f"Biaya listrik yang terbuang adalah Rp{int(biaya)}")
... else:
...     print(f"Biaya listrik yang terbuang adalah Rp{biaya:.2f}")
...
Masukkan daya lampu (watt): 65
Masukkan lama lampu menyala (jam): 20
Masukkan tarif listrik (rupiah per kWh): 1500
Biaya listrik yang terbuang adalah Rp1950
>>>
>>>
>>> w = float(input("Masukkan daya lampu (watt): "))
... j = float(input("Masukkan lama lampu menyala (jam): "))
... r = float(input("Masukkan tarif listrik (rupiah per kWh): "))
...
... energi = (w * j) / 1000
... biaya = energi * r
...
... if biaya.is_integer():
...     print(f"Biaya listrik yang terbuang adalah Rp{int(biaya)}")
... else:
...     print(f"Biaya listrik yang terbuang adalah Rp{biaya:.2f}")
...
Masukkan daya lampu (watt): 100
Masukkan lama lampu menyala (jam): 48
Masukkan tarif listrik (rupiah per kWh): 1450
Biaya listrik yang terbuang adalah Rp6960
>>>
>>>
>>> w = float(input("Masukkan daya lampu (watt): "))
... j = float(input("Masukkan lama lampu menyala (jam): "))
... r = float(input("Masukkan tarif listrik (rupiah per kWh): "))
...
... energi = (w * j) / 1000
... biaya = energi * r
...
... if biaya.is_integer():
...     print(f"Biaya listrik yang terbuang adalah Rp{int(biaya)}")
... else:
...     print(f"Biaya listrik yang terbuang adalah Rp{biaya:.2f}")
...
Masukkan daya lampu (watt): 45
Masukkan lama lampu menyala (jam): 35.5
Masukkan tarif listrik (rupiah per kWh): 1699
Biaya listrik yang terbuang adalah Rp2714.15