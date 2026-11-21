{
  "metadata": {
    "kernelspec": {
      "display_name": "Python (Pyodide)",
      "language": "python",
      "name": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "bedf82f7-c15c-4830-994d-a40398b2fed0",
      "cell_type": "code",
      "source": "# NIM/NAMA  : 15626049 Hisyam Fithroturrohim\n# TANGGAL   : 30 September 2026\n# DESKRIPSI : Praktikum Berpikir Komputasional soal 3 (penghitung upah lembur)\n\nj1 = int(input(\"Masukkan jam masuk : \" ))\nm1 = int(input(\"Masukkan menit masuk : \"))\nj2 = int(input(\"Masukkan jam keluar : \"))\nm2 = int(input(\"Masukkan menit keluar : \"))\nN = int(input(\"Masukkan batas shift normal (menit) : \"))\nU = float(input(\"Masukkan upah per menit : \"))\nL = float(input(\"Masukkan pengali upah lembur : \"))\nM = float(input(\"Masukkan tunjangan makan (Rp) : \"))\nT = int(input(\"Masukkan batas minimal tunjangan (menit) : \"))\n\n\ndurasi_kerja = (j2 * 60 + m2) - (j1 * 60 + m1)\njam_kerja = durasi_kerja // 60\nmenit_kerja = durasi_kerja % 60\n\ndurasi_kerja > N ; menit_lembur = durasi_kerja - N\n\nbool = menit_lembur < T, M == 0\n\ntotal_upah = (N * U) + (menit_lembur * 1000 * L) + M\n\nprint(f\"Total durasi kerja : {jam_kerja} jam {menit_kerja} menit\")\nprint(f\"Menit kerja normal : {N} menit\")\nprint(f\"Menit kerja lembur : {menit_lembur} menit\")\nprint(f\"Tunjangan makan : Rp{M}\")\nprint(f\"Total upah diterima Rp{total_upah}\")",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdin",
          "text": "Masukkan jam masuk :  13\nMasukkan menit masuk :  0\nMasukkan jam keluar :  16\nMasukkan menit keluar :  30\nMasukkan batas shift normal (menit) :  300\nMasukkan upah per menit :  1250.5\nMasukkan pengali upah lembur :  1.75\nMasukkan tunjangan makan (Rp) :  30000\nMasukkan batas minimal tunjangan (menit) :  240\n"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Total durasi kerja : 3 jam 30 menit\nMenit kerja normal : 300 menit\nMenit kerja lembur : -90 menit\nTunjangan makan : Rp30000.0\nTotal upah diterima Rp247650.0\n"
        }
      ],
      "execution_count": 25
    },
    {
      "id": "3c0616cd-bbb6-4b08-b884-2aa367e3f8cd",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}