import os
import hashlib
import base64
import time
import pyfiglet
import termcolor
import sys
from colorama import init, Fore, Back, Style
import random
from pyfiglet import Figlet
from termcolor import colored
from cryptography.fernet import Fernet

KUNCI = b'2jD3-7JZUoR4B5q6QzW9t8vMwVYPeLsTgdTxuYH3J_c='
enkripsi = Fernet(KUNCI)

init(autoreset=True)

PERINGATAN = Fore.YELLOW
KESALAHAN = Fore.RED
INFORMASI = Fore.CYAN
SUKSES = Fore.GREEN
MASUKAN = Fore.MAGENTA
RESET = Style.RESET_ALL
SOROT = Fore.WHITE + Style.BRIGHT

def cetak_teks(teks, warna=Fore.CYAN):
    print(warna + teks + Style.RESET_ALL)

def tampilkan_loading(pesan, durasi=1):
    print(INFORMASI + pesan)

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_header(nama_pengguna=None):
    bersihkan_layar()
    print(PERINGATAN + "✧" * 60)
    f = Figlet(font='slant')
    judul = f.renderText('EyeFox')
    for baris in judul.split('\n'):
        cetak_teks(" " * 10 + baris, Fore.CYAN)
    subjudul = "| GENERATOR PASSWORD AMAN DAN TERENKRIPSI |"
    print(PERINGATAN + "✧" * 60)
    cetak_teks("\n" + " " * ((60 - len(subjudul)) // 2) + subjudul, Fore.LIGHTMAGENTA_EX)
    print(PERINGATAN + "✧" * 60)
    if nama_pengguna:
        salam_pengguna = f"👤 PENGGUNA: {nama_pengguna}"
        print("\n" + SUKSES + " " * ((60 - len(salam_pengguna)) // 2) + salam_pengguna)
    else:
        print("\n" + INFORMASI + " " * 13 + "🔐 BUAT PASSWORD UNIK DAN AMAN")
    print(PERINGATAN + "✧" * 60 + "\n")

def buat_password(nama_pengguna):
    daftar_akun = {
        1: "Facebook",
        2: "Google",
        3: "Instagram",
        4: "Twitter/X",
        5: "LinkedIn",
        6: "GitHub",
        7: "Amazon",
        8: "Microsoft",
        9: "Lainnya"
    }
    print(RESET + INFORMASI + "╔" + "═" * 58 + "╗")
    print(INFORMASI + "║" + " " * 20 + "🏷️  PILIH JENIS WEB" + " " * 20 + "║")
    print(INFORMASI + "╠" + "═" * 58 + "╣")
    for nomor, nama in daftar_akun.items():
        print(INFORMASI + f"║  {PERINGATAN}{nomor}. {SOROT}{nama.ljust(30)}" + " " * 23 + RESET + INFORMASI + "║")
    print(INFORMASI + "╚" + "═" * 58 + "╝")
    while True:
        try:
            pilihan = input(MASUKAN + "\n🎯 MASUKKAN PILIHAN (1-9): " + SOROT).strip()
            if pilihan.isdigit() and 1 <= int(pilihan) <= 9:
                pilihan = int(pilihan)
                break
            cetak_teks("⚠ HARAP MASUKKAN ANGKA ANTARA 1-9!", KESALAHAN)
        except ValueError:
            cetak_teks("⚠ INPUT HARUS BERUPA ANGKA!", KESALAHAN)
    if pilihan == 9:
        while True:
            akun = input(MASUKAN + "\n🔧 MASUKKAN NAMA WEB CUSTOM: " + SOROT).strip().title()
            if akun:
                break
            cetak_teks("⚠ NAMA WEB TIDAK BOLEH KOSONG!", KESALAHAN)
    else:
        akun = daftar_akun[pilihan]
    while True:
        id_angka = input(RESET + MASUKAN + f"\n📊 MASUKKAN ID UNTUK {akun.upper()} (ANGKA): " + SOROT).strip()
        if id_angka.isdigit() and int(id_angka) > 0:
            id_angka = int(id_angka)
            break
        cetak_teks("⚠ ID HARUS BERUPA ANGKA!", KESALAHAN)
    tampilkan_loading("\n🔐 MEMBUAT KATA SANDI...")
    gabungan = f"{nama_pengguna}{akun}{id_angka}".encode('utf-8')
    hash_bytes = hashlib.sha256(gabungan).digest()
    kata_sandi = base64.b64encode(hash_bytes).decode('utf-8')
    kata_sandi = kata_sandi.replace('+', '@').replace('/', '!')[:12]
    print("\n" + SUKSES + "╔" + "═" * 58 + "╗")
    print(SUKSES + "║" + " " * 15 + "🔑 KATA SANDI ANDA" + " " * 25 + "║")
    print(SUKSES + "╠" + "═" * 58 + "╣")
    print(SUKSES + f"║  🏷️ WEB  : {SOROT}{akun.ljust(44)}" + " " * 3 + RESET + SUKSES + "║")
    print(SUKSES + f"║  📊 ID  : {SOROT}{str(id_angka).ljust(44)}" + " " * 3 + RESET + SUKSES + "║")
    print(SUKSES + "╠" + "═" * 58 + "╣")
    print(SUKSES + "║" + " " * 20 + SOROT + f"  {kata_sandi}  " + Style.RESET_ALL + SUKSES + " " * 22 + "║")
    print(SUKSES + "╚" + "═" * 58 + "╝")
    cetak_teks("\n💡 SIMPAN KATA SANDI INI DI TEMPAT AMAN!", PERINGATAN)
    input(MASUKAN + "\n🚀 TEKAN ENTER UNTUK KEMBALI KE MENU UTAMA..." + Style.RESET_ALL)

def utama():
    nama_pengguna = None
    if os.path.exists("username.txt"):
        try:
            with open("username.txt", "rb") as f:
                nama_pengguna_terenkripsi = f.read()
            nama_pengguna = enkripsi.decrypt(nama_pengguna_terenkripsi).decode('utf-8')
            if not nama_pengguna:
                raise ValueError("Username kosong")
        except:
            os.remove("username.txt")
            cetak_teks("⚠ Data pengguna tidak valid. Harap masukkan username baru.", KESALAHAN)
            time.sleep(1)
            nama_pengguna = None
    if nama_pengguna:
        tampilkan_header(nama_pengguna)
    else:
        tampilkan_header()
        while True:
            masukan_nama_pengguna = input(MASUKAN + "👤 MASUKKAN NAMA ANDA: " + SOROT).strip().title()
            if masukan_nama_pengguna:
                nama_pengguna = masukan_nama_pengguna
                nama_pengguna_terenkripsi = enkripsi.encrypt(nama_pengguna.encode())
                with open("username.txt", "wb") as f:
                    f.write(nama_pengguna_terenkripsi)
                break
            cetak_teks("⚠ NAMA TIDAK BOLEH KOSONG!", KESALAHAN)
        tampilkan_header(nama_pengguna)
    while True:
        print(INFORMASI + "\n╔" + "═" * 58 + "╗")
        print(INFORMASI + "║" + " " * 20 + "📋 MENU UTAMA" + " " * 25 + "║")
        print(INFORMASI + "╠" + "═" * 58 + "╣")
        print(INFORMASI + f"║  {PERINGATAN}1. {SOROT}Lihat Kata Sandi{' ' * 37}{RESET}{INFORMASI}║")
        print(INFORMASI + f"║  {PERINGATAN}2. {SOROT}Hapus Data Pengguna{' ' * 34}{RESET}{INFORMASI}║")
        print(INFORMASI + f"║  {PERINGATAN}3. {SOROT}Keluar{' ' * 47}{RESET}{INFORMASI}║")
        print(INFORMASI + "╚" + "═" * 58 + "╝")
        pilihan = input(MASUKAN + "\n🎯 PILIH MENU (1/2/3): " + SOROT).strip()
        if pilihan == '1':
            buat_password(nama_pengguna)
            tampilkan_header(nama_pengguna)
        elif pilihan == '2':
            if os.path.exists("username.txt"):
                konfirmasi = input(KESALAHAN + "⚠ ANDA YAKIN INGIN MENGHAPUS DATA? (y/n): " + SOROT).strip().lower()
                if konfirmasi == 'y':
                    os.remove("username.txt")
                    cetak_teks("\n✅ DATA PENGGUNA BERHASIL DIHAPUS!", SUKSES)
                    time.sleep(1)
                    tampilkan_header()
                    return utama()
            else:
                cetak_teks("\n⚠ TIDAK ADA DATA PENGGUNA YANG TERSIMPAN!", KESALAHAN)
                time.sleep(1)
                tampilkan_header(nama_pengguna)
        elif pilihan == '3':
            cetak_teks(RESET + INFORMASI + "\n💝 TERIMA KASIH TELAH MENGGUNAKAN TOOLS SAYA" + " " * 15, Fore.LIGHTCYAN_EX)
            print(Fore.LIGHTRED_EX + f"\n⏳ PROGRAM KELUAR\n", end="\r")
            break
        else:
            cetak_teks("\n⚠ PILIHAN TIDAK VALID!", KESALAHAN)
            time.sleep(1)
            tampilkan_header(nama_pengguna)

if __name__ == "__main__":
    try:
        utama()
    except KeyboardInterrupt:
        cetak_teks("\n\n⚠ PROGRAM DIHENTIKAN OLEH PENGGUNA!", KESALAHAN)
        time.sleep(1)
