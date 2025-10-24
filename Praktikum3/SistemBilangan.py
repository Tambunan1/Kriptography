print("\n\n Program Konversi Bilangan (Biner, Oktal, Hexadesimal \n")

def konversi_biner():
    print("\n=== Konversi Bilangan Biner ke Desimal & Hexadesimal ===")
    biner = input("Masukkan bilangan biner: ")
    if all(bit in '01' for bit in biner):
        desimal = int(biner, 2)
        hexa = hex(desimal)[2:].upper()
        print(f"Desimal     : {desimal}")
        print(f"Hexadesimal : {hexa}")
    else:
        print("Input tidak valid! Hanya boleh berisi angka 0 dan 1.")


def konversi_oktal():
    print("\n=== Konversi Bilangan Oktal ke Desimal, Biner & Hexadesimal ===")
    oktal = input("Masukkan bilangan oktal: ")
    if all(digit in '01234567' for digit in oktal):
        desimal = int(oktal, 8)
        biner = bin(desimal)[2:]
        hexa = hex(desimal)[2:].upper()
        print(f"Desimal     : {desimal}")
        print(f"Biner       : {biner}")
        print(f"Hexadesimal : {hexa}")
    else:
        print("Input tidak valid! Bilangan oktal hanya boleh berisi angka 0–7.")


def konversi_hexa():
    print("\n=== Konversi Bilangan Hexadesimal ke Desimal, Biner & Oktal ===")
    hexa = input("Masukkan bilangan hexadesimal: ").upper()
    if all(digit in '0123456789ABCDEF' for digit in hexa):
        desimal = int(hexa, 16)
        biner = bin(desimal)[2:]
        oktal = oct(desimal)[2:]
        print(f"Desimal : {desimal}")
        print(f"Biner   : {biner}")
        print(f"Oktal   : {oktal}")
    else:
        print("Input tidak valid! Bilangan hex hanya boleh berisi 0–9 dan A–F.")



# Menu Utama Program

while True:
    
    print("\n   PROGRAM KONVERSI BILANGAN  \n")
    print("1. Biner ke Desimal & Hexadesimal")
    print("2. Oktal ke Desimal, Biner & Hexadesimal")
    print("3. Hexadesimal ke Desimal, Biner & Oktal")
    print("4. Keluar \n")
    
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        konversi_biner()
    elif pilihan == "2":
        konversi_oktal()
    elif pilihan == "3":
        konversi_hexa()
    elif pilihan == "4":
        print("Thankyou")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih antara 1–4.")
