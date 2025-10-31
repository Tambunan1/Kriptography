# 1. If Tunggal (If Sederhana)
temperature = 30
if temperature > 25:
    print("Cuaca panas, nyalakan AC")

# Penjelasan: Kode ini memeriksa satu kondisi sederhana.

# 2. If dengan Else
password = "12345"
if password == "secret":
    print("Akses diterima")
else:
    print("Akses ditolak")

# Penjelasan: Kode ini memeriksa kondisi dan memberikan respons alternatif.

# 3. If-Elif-Else
nilai = 85
if nilai >= 90:
    print("Anda mendapat nilai A")
elif nilai >= 80:
    print("Anda mendapat nilai B")
elif nilai >= 70:
    print("Anda mendapat nilai C")
else:
    print("Perbaiki Nilai")  # Perbaikan: Ejaan yang benar untuk pesan

# Penjelasan: Kode ini mengecek beberapa kondisi bertingkat.

# 4. If Bersarang (Nested If)
number = 10
if number > 0:
    print("Angka positif")
    if number % 2 == 0:
        print("Angka genap")
    else:
        print("Angka ganjil")
else:
    print("Angka negatif")

# Penjelasan: Ini menunjukkan if di dalam if untuk pemeriksaan lebih lanjut.

# 5. If Dengan Operator Logika (And, Or, Not)
#   - Bagian And
umur = 20
tinggi = 160
if umur >= 18 and tinggi >= 155:
    print("Anda memenuhi syarat")
else:
    print("Anda tidak memenuhi syarat")

#   - Bagian Or (Tambahan baru)
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Ini adalah akhir pekan.")
else:
    print("Ini adalah hari kerja.")

#   - Bagian Not (Tambahan baru)
is_logged_in = False
if not is_logged_in:
    print("Silakan masuk untuk melanjutkan.")
else:
    print("Selamat datang kembali!")

# Penjelasan: Bagian ini menunjukkan penggunaan operator logika:
#   - 'and' untuk memeriksa kedua kondisi.
#   - 'or' untuk memeriksa salah satu kondisi.
#   - 'not' untuk membalikkan kondisi.

# 6. If Dengan Input
username = input("Masukkan nama pengguna: ")
if username == "admin":
    print("Selamat datang, admin!")
else:
    print(f"Selamat datang, {username}!")

# Penjelasan: Kode ini menggunakan input() untuk interaksi pengguna.
