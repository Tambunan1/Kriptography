# ==========================
# Program: Kalkulator Hybrid
# Tugas Praktikum 2
#Elsahday Tambunan
#230840038
# ==========================

print("=== KALKULATOR HYBRID ===")
print("Masukkan ekspresi matematika (contoh: 4+4-3 atau 5 - 3 * 4)")
print("Gunakan operator: +  -  *  /  ** (pangkat)")
print("===========================")

# Input ekspresi dari pengguna
ekspresi = input("Masukkan ekspresi: ")

# Hilangkan spasi agar bisa memproses ekspresi tanpa error
ekspresi_bersih = ekspresi.replace(" ", "")

try:
    # Evaluasi ekspresi menggunakan eval()
    hasil = eval(ekspresi_bersih)
    
    # Tampilkan hasil
    print("===========================")
    print(f"Input Ekspresi  : {ekspresi}")
    print(f"Hasil Diproses  : {ekspresi_bersih}")
    print(f"Output (Hasil)  : {hasil}")
    print("===========================")

except Exception as e:
    print("Terjadi kesalahan dalam perhitungan:", e)
