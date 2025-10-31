def hitung_nilai():
    print("=== Program Hitung Nilai Akhir Akademik ===")
    
    # Input nilai
    sikap = float(input("Masukkan nilai Sikap/Kehadiran (0-100): "))
    tugas = float(input("Masukkan nilai Tugas (0-100): "))
    uts   = float(input("Masukkan nilai UTS (0-100): "))
    uas   = float(input("Masukkan nilai UAS (0-100): "))
    
    # Bobot sesuai ketentuan
    total = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)
    
    # Tentukan nilai huruf
    if total >= 81 and total <= 100:
        nilai_huruf = "A"
        bobot = 4
    elif total >= 76:
        nilai_huruf = "B+"
        bobot = 3.5
    elif total >= 71:
        nilai_huruf = "B"
        bobot = 3
    elif total >= 66:
        nilai_huruf = "C+"
        bobot = 2.5
    elif total >= 56:
        nilai_huruf = "C"
        bobot = 2
    elif total >= 46:
        nilai_huruf = "D"
        bobot = 1
    else:
        nilai_huruf = "E"
        bobot = 0
    
    # Tentukan keterangan lulus / tidak lulus
    if total >= 56:
        keterangan = "Lulus"
    else:
        keterangan = "Tidak Lulus"
    
    # Output
    print("\n=== Hasil Perhitungan ===")
    print(f"Total Nilai Akhir : {total:.2f}")
    print(f"Nilai Huruf       : {nilai_huruf} (Bobot {bobot})")
    print(f"Keterangan        : {keterangan}")


# Jalankan program
if __name__ == "__main__":
    hitung_nilai()
