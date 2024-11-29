# Sistem Pengelolaan Data Penjualan Toko 2024

Sistem Pengelolaan Data Penjualan Toko 2024 adalah sebuah program sederhana yang dirancang untuk membantu pengelolaan produk dalam sebuah toko. Program ini memungkinkan pengguna untuk menambah produk, menampilkan daftar produk, mencari produk berdasarkan nama, dan menghitung total harga produk yang dibeli. Program ini menggunakan berbagai konsep dasar dalam pemrograman Python, seperti **conditional statement**, **looping**, **fungsi**, **manipulasi string**, **struktur data (list, dictionary)**, dan **regular expressions (regex)**.

## Fitur

1. **Tambah Produk**: Menambah produk baru ke dalam daftar dengan nama dan harga produk.
2. **Tampilkan Daftar Produk**: Menampilkan seluruh daftar produk yang telah ditambahkan.
3. **Cari Produk**: Mencari produk berdasarkan nama menggunakan regex (pencarian berbasis pola).
4. **Hitung Total Harga**: Menghitung total harga produk yang dipilih oleh pengguna.
5. **Keluar dari Program**: Menghentikan program dan keluar.

## Prasyarat

- Python 3.x atau versi yang lebih baru.
- Modul `re` (regular expressions) sudah termasuk dalam Python, sehingga tidak perlu menginstal modul tambahan.

## Cara Penggunaan

1. **Menambah Produk**:
    - Pilih opsi **1** untuk menambah produk.
    - Masukkan nama produk dan harga produk.
    - Program akan menambahkan produk tersebut ke dalam daftar produk.

2. **Menampilkan Daftar Produk**:
    - Pilih opsi **2** untuk menampilkan seluruh produk yang ada.
    - Program akan menampilkan produk dengan nama dan harga.

3. **Mencari Produk**:
    - Pilih opsi **3** untuk mencari produk berdasarkan nama.
    - Masukkan kata kunci untuk mencari produk yang sesuai. Program akan menampilkan produk yang mencocokkan pola pencarian.

4. **Menghitung Total Harga**:
    - Pilih opsi **4** untuk menghitung total harga produk yang dipilih.
    - Pilih produk berdasarkan nomor urutnya dan program akan menghitung total harga.

5. **Keluar dari Program**:
    - Pilih opsi **5** untuk keluar dari program.

## Contoh Penggunaan

```
=== Menu Utama ===
1. Tambah Produk
2. Tampilkan Daftar Produk
3. Cari Produk
4. Hitung Total Harga
5. Keluar
Pilih menu (1/2/3/4/5): 1
Masukkan Nama Produk: Sabun
Masukkan Harga Produk: 5000
Produk Sabun berhasil ditambahkan dengan harga 5000.

=== Menu Utama ===
1. Tambah Produk
2. Tampilkan Daftar Produk
3. Cari Produk
4. Hitung Total Harga
5. Keluar
Pilih menu (1/2/3/4/5): 2
No  Nama Produk           Harga     
===================================
1   Sabun                 5000       

=== Menu Utama ===
1. Tambah Produk
2. Tampilkan Daftar Produk
3. Cari Produk
4. Hitung Total Harga
5. Keluar
Pilih menu (1/2/3/4/5): 3
Masukkan nama produk yang ingin dicari: sabun
Hasil Pencarian untuk 'sabun':
No  Nama Produk           Harga     
===================================
1   Sabun                 5000       

=== Menu Utama ===
1. Tambah Produk
2. Tampilkan Daftar Produk
3. Cari Produk
4. Hitung Total Harga
5. Keluar
Pilih menu (1/2/3/4/5): 4
Berapa produk yang ingin Anda hitung totalnya? 1
Pilih nomor produk: 1
Total harga untuk 1 produk adalah 5000.
```

## Struktur Program

- **tambah_produk()**: Fungsi untuk menambah produk baru ke dalam daftar.
- **tampilkan_produk()**: Fungsi untuk menampilkan seluruh daftar produk yang ada.
- **cari_produk()**: Fungsi untuk mencari produk berdasarkan nama dengan menggunakan regular expressions.
- **hitung_total()**: Fungsi untuk menghitung total harga berdasarkan produk yang dipilih oleh pengguna.
- **menu_utama()**: Fungsi utama untuk menampilkan dan mengelola menu serta input dari pengguna.

## Catatan

- Program ini menggunakan **regex** untuk mencari produk berdasarkan kata kunci yang dimasukkan oleh pengguna.
- Jika tidak ada produk yang cocok saat pencarian, program akan memberi pesan bahwa produk tidak ditemukan.
- Program dapat dikembangkan lebih lanjut untuk menambahkan fitur seperti mengupdate harga produk, menghapus produk, dan lain sebagainya.

## Lisensi

MIT License. See LICENSE for more information.
