def hitung_persimpangan_kereta():
    # Meminta input untuk Kereta A
    jenis_a = input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo): ")
    jarak_a = int(input("Masukkan jarak Kereta A (m): "))
    kecepatan_a = int(input("Masukkan kecepatan Kereta A (m/s): "))

    # Meminta input untuk Kereta B
    jenis_b = input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo): ")
    jarak_b = int(input("Masukkan jarak Kereta B (m): "))
    kecepatan_b = int(input("Masukkan kecepatan Kereta B (m/s): "))

    # Menghitung waktu tiba (T_A dan T_B)
    t_a = jarak_a / kecepatan_a
    t_b = jarak_b / kecepatan_b

    # Menghitung selisih waktu tiba tanpa abs() dan tanpa if-else
    selisih_waktu = t_a - t_b
    selisih_waktu = selisih_waktu * ((selisih_waktu >= 0) - (selisih_waktu < 0))

    # Penentuan kondisi jalur aman (selisih >= 30.0)
    aman = selisih_waktu >= 30.0
    konflik = not aman

    # --- JALUR AMAN (selisih >= 30.0) ---
    # Menggunakan ekspresi boolean untuk memilih pesan tanpa if-else
    lebih_cepat_a = t_a < t_b
    pesan_aman_a = f"Jalur aman. Kereta A melintas duluan tanpa henti."
    pesan_aman_b = f"Jalur aman. Kereta B melintas duluan tanpa henti."
    cetak_aman = (lebih_cepat_a * pesan_aman_a) + ((not lebih_cepat_a) * pesan_aman_b)

    # --- KONDISI KONFLIK (selisih < 30.0) ---
    print("Konflik terdeteksi!" * konflik, end="")
    
    prioritas = {"Eksekutif": 3, "Bisnis": 2, "Kargo": 1}
    prio_a = prioritas.get(jenis_a, 0)
    prio_b = prioritas.get(jenis_b, 0)

    # Menentukan pemenang berdasarkan prioritas, waktu, jarak, dan jalur utama
    pemenang_a = (
        (prio_a > prio_b) or
        (prio_a == prio_b and t_a < t_b) or
        (prio_a == prio_b and t_a == t_b and jarak_a < jarak_b) or
        (prio_a == prio_b and t_a == t_b and jarak_a == jarak_b)
    )

    waktu_tunggu_b = (t_a + 40.0) - t_b
    waktu_tunggu_a = (t_b + 40.0) - t_a

    pesan_konflik_a = f" Kereta A diprioritaskan melintas.\nKereta B harus berhenti dan menunggu selama {waktu_tunggu_b:.1f} detik."
    pesan_konflik_b = f" Kereta B diprioritaskan melintas.\nKereta A harus berhenti dan menunggu selama {waktu_tunggu_a:.1f} detik."

    cetak_konflik = (pemenang_a * pesan_konflik_a) + ((not pemenang_a) * pesan_konflik_b)

    # Cetak hasil akhir menggunakan perkalian kondisi boolean (True=1, False=0)
    hasil_akhir = (aman * f"\n{cetak_aman}") + (konflik * f"{cetak_konflik}")
    print(hasil_akhir)

if __name__ == "__main__":
    hitung_persimpangan_kereta()