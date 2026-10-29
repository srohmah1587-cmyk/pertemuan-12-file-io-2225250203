def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                # Melewati baris kosong
                if not baris:
                    continue

                bagian = baris.split(",")

                # Memastikan format terdiri dari NIM, nama, nilai
                if len(bagian) != 3:
                    print(f"Baris {nomor_baris} tidak valid: format salah")
                    continue

                nim, nama, nilai = bagian

                try:
                    nilai = float(nilai)
                except ValueError:
                    print(f"Baris {nomor_baris} tidak valid: nilai bukan angka")
                    continue

                if not nim.strip() or not nama.strip():
                    print(f"Baris {nomor_baris} tidak valid: NIM/nama kosong")
                    continue

                if nilai < 0 or nilai > 100:
                    print(f"Baris {nomor_baris} tidak valid: nilai di luar 0-100")
                    continue

                data.append({
                    "nim": nim.strip(),
                    "nama": nama.strip(),
                    "nilai": nilai
                })

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return data


def tulis_rekap(nama_file, data):
    import os

    folder = os.path.dirname(nama_file)
    if folder:
        os.makedirs(folder, exist_ok=True)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("REKAP NILAI MAHASISWA\n")
        file.write("=====================\n")

        if not data:
            file.write("Tidak ada data valid untuk direkap.\n")
            print("Tidak ada data valid untuk direkap.")
            return

        total = 0
        jumlah_lulus = 0

        for mahasiswa in data:
            nilai = mahasiswa["nilai"]
            total += nilai

            # Nilai 60 termasuk lulus
            if nilai >= 60:
                status = "Lulus"
                jumlah_lulus += 1
            else:
                status = "Tidak Lulus"

            file.write(
                f"{mahasiswa['nim']}, "
                f"{mahasiswa['nama']}, "
                f"{nilai:g}, {status}\n"
            )

        rata_rata = total / len(data)

        file.write("\nRINGKASAN\n")
        file.write(f"Jumlah mahasiswa: {len(data)}\n")
        file.write(f"Rata-rata nilai: {rata_rata:.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")
        file.write(f"Jumlah tidak lulus: {len(data) - jumlah_lulus}\n")

    print(f"Rekap berhasil disimpan ke {nama_file}")


# Alur utama
input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data_mahasiswa = baca_data(input_file)
tulis_rekap(output_file, data_mahasiswa)