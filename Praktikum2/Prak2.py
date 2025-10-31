import operator

# Definisi dictionary untuk operasi matematika
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

while True:
    jawab = input("Apakah Anda ingin memulai operasi perhitungan? (y/n): ").lower()
    
    if jawab != 'y':
        break  # Keluar dari loop jika jawaban bukan 'y'
    
    try:
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        operator_input = input("Masukkan operator (+, -, *, /): ")
        
        # Lakukan operasi menggunakan dictionary
        hasil = ops[operator_input](a, b)
        
        print(f"Hasil dari {a} {operator_input} {b} = {hasil}")
    except KeyError:
        print("Operator tidak valid. Silakan masukkan salah satu dari: +, -, *, /")
    except ZeroDivisionError:
        print("Pembagian dengan nol tidak diperbolehkan.")
    except ValueError:
        print("Input nilai a atau b harus berupa angka. Silakan coba lagi.")

print("Program selesai. Terima kasih!")
