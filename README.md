# Pertemuan 12 - File I/O dan Error Handling

**Nama:** Siti Rohmah  
**NIM:** 2225250203  
**Kelas:** 3A

## Tujuan

Praktikum ini bertujuan untuk memahami cara membaca, memvalidasi, mengolah, dan menulis data menggunakan file dalam Python. Selain itu, praktikum ini melatih kemampuan menangani kesalahan menggunakan `FileNotFoundError` dan `ValueError` agar program tetap berjalan ketika menemukan masalah pada file atau data input.

## Format File Input

File input yang digunakan adalah `data/nilai.txt` dengan format:

```text
NIM,nilai
A001,85
A002,78
A003,92
A004,60
A005,abc
```

Keterangan:
- `NIM` merupakan identitas mahasiswa.
- `nilai` merupakan nilai mahasiswa dalam bentuk angka.
- Setiap baris berisi NIM dan nilai yang dipisahkan dengan tanda koma.
- Baris dengan nilai yang bukan angka akan dilaporkan dan dilewati oleh program.

## Cara Menjalankan

Jalankan program melalui terminal dari direktori utama proyek menggunakan perintah berikut:

```bash
python3 tugas/rekap_nilai_file.py
```

Program akan membaca data dari `data/nilai.txt`, memvalidasi setiap baris, menghitung rekap nilai, menentukan status kelulusan, dan menyimpan hasilnya ke `data/hasil_rekap.txt`.

Mahasiswa dengan nilai minimal 60 dinyatakan lulus.

## Error yang Ditangani

### 1. FileNotFoundError

Kesalahan ini terjadi ketika file input tidak ditemukan pada lokasi yang ditentukan. Program menangani kesalahan tersebut dengan menampilkan pesan bahwa file tidak ditemukan dan mengembalikan data kosong sehingga program tidak berhenti secara tiba-tiba.

### 2. ValueError

Kesalahan ini terjadi ketika nilai yang seharusnya berupa angka berisi teks atau data yang tidak dapat dikonversi menjadi angka, misalnya `abc`. Program menampilkan pesan kesalahan pada baris terkait dan melewati data yang tidak valid agar data mahasiswa lainnya tetap dapat diproses.

Program juga memvalidasi format baris, memastikan NIM dan nama tidak kosong, serta memeriksa agar nilai berada pada rentang 0 sampai 100.

## Test Case

| No. | Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | Semua data valid | Semua data diproses dan rekap dihitung dengan benar | Seluruh data valid direkap dan hasil disimpan ke file output | Berhasil jika sesuai hasil pengujian |
| 2 | File `nilai.txt` tidak tersedia | Pesan file tidak ditemukan dan program tidak crash | Pesan kesalahan ditampilkan dan program tetap berjalan | Berhasil jika sesuai hasil pengujian |
| 3 | Nilai berisi teks, misalnya `A005,abc` | Baris invalid dilaporkan dan dilewati, data lainnya tetap diproses | Data dengan nilai bukan angka dilewati | Berhasil jika sesuai hasil pengujian |
| 4 | Terdapat baris kosong | Baris kosong dilewati | Baris kosong tidak dimasukkan ke dalam rekap | Berhasil jika sesuai hasil pengujian |
| 5 | Nilai mahasiswa adalah 60 | Mahasiswa dinyatakan lulus | Status kelulusan menjadi Lulus | Berhasil jika sesuai hasil pengujian |

Catatan: Status pengujian akhir perlu disesuaikan dengan hasil eksekusi program yang sebenarnya.

## Refleksi

Salah satu kesalahan yang ditemukan dalam pengolahan file adalah `ValueError`, yaitu ketika program mencoba mengubah teks yang bukan angka menjadi tipe data numerik. Contohnya adalah nilai `abc` pada data mahasiswa. Jika tidak ditangani, kesalahan tersebut dapat menghentikan program.

Untuk mengatasinya, program menggunakan `try-except` saat mengonversi nilai menjadi angka. Jika terjadi `ValueError`, program menampilkan pesan kesalahan dan melewati baris yang bermasalah. Dengan demikian, data mahasiswa lain yang valid tetap dapat diproses dan hasil rekap dapat dibuat tanpa terganggu oleh satu baris yang salah.