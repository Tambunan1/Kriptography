# Program Kalkulator Sederhana dengan Operator Aritmatika
# Bagian ini mengambil input a, b, dan operator, kemudian menghitung hasil menggunakan if-elif-else

print("=== Kalkulator Sederhana ===")
try:
    a = float(input("Masukkan nilai a: "))  # Input nilai a dari keyboard
    b = float(input("Masukkan nilai b: "))  # Input nilai b dari keyboard
    operator = input("Masukkan operator (+, -, *, /): ")  # Input operator dari keyboard
    
    if operator == '+':  # Cek jika operator adalah +
        hasil = a + b
        print(f"Hasil: {a} + {b} = {hasil}")
    elif operator == '-':  # Cek jika operator adalah -
        hasil = a - b
        print(f"Hasil: {a} - {b} = {hasil}")
    elif operator == '*':  # Cek jika operator adalah *
        hasil = a * b
        print(f"Hasil: {a} * {b} = {hasil}")
    elif operator == '/':  # Cek jika operator adalah /
        if b != 0:  # Gunakan if untuk memeriksa pembagian oleh nol
            hasil = a / b
            print(f"Hasil: {a} / {b} = {hasil}")
        else:
            print("Error: Pembagian oleh nol tidak diperbolehkan!")
    else:
        print("Operator tidak valid. Gunakan +, -, *, atau /.")
except ValueError:
    print("Error: Masukkan angka yang valid untuk a dan b.")

# Bagian Pengembangan Kode untuk x, y, z
# Di sini, nilai x, y, z diinput dari keyboard, kemudian jalankan logika kondisional yang sama
# Seperti contoh yang diberikan, menggunakan kombinasi operator logika dan perbandingan

print("\n=== Pengembangan Kode untuk x, y, z ===")
try:
    x = float(input("Masukkan nilai x: "))  # Input x dari keyboard
    y = float(input("Masukkan nilai y: "))  # Input y dari keyboard
    z = float(input("Masukkan nilai z: "))  # Input z dari keyboard
    
    # Kondisi 1: Cek jika x berada antara 18 dan 30 (menggunakan and)
    if x >= 18 and x <= 30:
        print("x berada di antara 18 dan 30")
    else:
        print("x tidak berada di antara 18 dan 30")
    
    # Kondisi 2: Cek jika y berada di luar rentang 10 hingga 20 (menggunakan or)
    if y < 10 or y > 20:
        print("y berada di luar rentang 10 hingga 20")
    else:
        print("y berada di dalam rentang 10 hingga 20")
    
    # Kondisi 3: Cek jika z sama dengan 5 (menggunakan ==)
    if z == 5:
        print("z sama dengan 5")
    else:
        print("z tidak sama dengan 5")
    
    # Kondisi 4: Cek jika x tidak sama dengan y (menggunakan !=)
    if x != y:
        print("x tidak sama dengan y")
    else:
        print("x sama dengan y")
    
    # Kondisi 5: Cek jika x lebih besar dari y (menggunakan >)
    if x > y:
        print("x lebih besar dari y")
    else:
        print("x tidak lebih besar dari y")
    
    # Kondisi 6: Cek jika z lebih kecil dari y (menggunakan <)
    if z < y:
        print("z lebih kecil dari y")
    else:
        print("z tidak lebih kecil dari y")
    
    # Kondisi 7: Cek kombinasi (menggunakan and)
    if y >= 15 and z <= 5:
        print("y lebih besar atau sama dengan 15, dan z lebih kecil atau sama dengan 5")
    
except ValueError:
    print("Error: Masukkan angka yang valid untuk x, y, dan z.")
