# Sistem Pengelolaan Data Penjualan Toko 2024
"""
Materi yang digunakan:
1. Conditional Statement
2. Looping
3. Function
4. String Manipulation
5. Data Type Collections (List, Dict)
6. Regular Expressions (Regex)
"""

import re  # Modul untuk Regex

# Variabel utama untuk menyimpan data produk
data_produk = []

# Fungsi untuk menambah produk ke daftar
def tambah_produk():
    """
    Fungsi untuk menambah data produk ke dalam daftar.
    Input:
        - Nama produk (string)
        - Harga produk (integer)
    Validasi:
        - Nama produk tidak boleh kosong
        - Harga harus berupa angka positif
    Output:
        - Data produk ditambahkan ke daftar `data_produk`.
    """
    print("\n=== Tambah Produk ===")
    while True:
        nama_produk = input("Masukkan Nama Produk: ").strip()
        if nama_produk:
            break
        print("Nama produk tidak boleh kosong!")

    while True:
        try:
            harga_produk = int(input("Masukkan Harga Produk: "))
            if harga_produk > 0:
                break
        except ValueError:
            pass
        print("Harga harus berupa angka positif!")

    data_produk.append({"nama": nama_produk.capitalize(), "harga": harga_produk})
    print(f"Produk {nama_produk} berhasil ditambahkan dengan harga {harga_produk}.\n")


# Fungsi untuk menampilkan daftar produk
def tampilkan_produk():
    """
    Fungsi untuk menampilkan daftar produk yang sudah ditambahkan.
    Proses:
        - Menampilkan data dalam format tabel (No, Nama, Harga)
    Output:
        - Tabel produk, atau pesan jika daftar kosong.
    """
    print("\n=== Daftar Produk ===")
    if not data_produk:
        print("Belum ada produk yang ditambahkan.")
        return
    print(f"{'No':<4} {'Nama Produk':<20} {'Harga':<10}")
    print("=" * 35)
    for i, produk in enumerate(data_produk, start=1):
        print(f"{i:<4} {produk['nama']:<20} {produk['harga']:<10}")
    print()


# Fungsi untuk mencari produk berdasarkan nama
def cari_produk():
    """
    Fungsi untuk mencari produk berdasarkan nama menggunakan Regex.
    Input:
        - Nama produk yang dicari (string)
    Proses:
        - Memfilter produk yang sesuai dengan pola
    Output:
        - Menampilkan daftar produk yang cocok, atau pesan jika tidak ada.
    """
    print("\n=== Cari Produk ===")
    keyword = input("Masukkan nama produk yang ingin dicari: ").strip()
    pattern = re.compile(f".*{keyword}.*", re.IGNORECASE)
    hasil_cari = [p for p in data_produk if pattern.match(p['nama'])]

    if not hasil_cari:
        print(f"Tidak ada produk yang cocok dengan kata kunci '{keyword}'.")
        return

    print(f"\nHasil Pencarian untuk '{keyword}':")
    print(f"{'No':<4} {'Nama Produk':<20} {'Harga':<10}")
    print("=" * 35)
    for i, produk in enumerate(hasil_cari, start=1):
        print(f"{i:<4} {produk['nama']:<20} {produk['harga']:<10}")
    print()


# Fungsi untuk menghitung total harga dari beberapa produk
def hitung_total():
    """
    Fungsi untuk menghitung total harga produk berdasarkan pilihan pengguna.
    Proses:
        - Meminta jumlah produk yang ingin dibeli
        - Menghitung total harga berdasarkan pilihan
    Output:
        - Total harga atau pesan jika daftar kosong.
    """
    print("\n=== Hitung Total Harga ===")
    if not data_produk:
        print("Belum ada produk yang tersedia untuk dihitung.")
        return

    total_harga = 0
    tampilkan_produk()
    jumlah = int(input("Berapa produk yang ingin Anda hitung totalnya? "))
    for _ in range(jumlah):
        indeks = int(input("Pilih nomor produk: ")) - 1
        if 0 <= indeks < len(data_produk):
            total_harga += data_produk[indeks]['harga']
        else:
            print("Nomor produk tidak valid.")

    print(f"Total harga untuk {jumlah} produk adalah {total_harga}.\n")


# Menu utama
def menu_utama():
    """
    Fungsi untuk menampilkan dan mengelola menu utama program.
    Proses:
        - Menampilkan pilihan menu (tambah produk, tampilkan produk, cari produk, hitung total, keluar)
        - Memproses input pengguna dan memanggil fungsi yang sesuai
        - Memberikan opsi untuk keluar dari program
    """
    while True:
        print("\n=== Menu Utama ===")
        print("1. Tambah Produk")
        print("2. Tampilkan Daftar Produk")
        print("3. Cari Produk")
        print("4. Hitung Total Harga")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            tampilkan_produk()
        elif pilihan == "3":
            cari_produk()
        elif pilihan == "4":
            hitung_total()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi!")


# Menjalankan program
menu_utama()
