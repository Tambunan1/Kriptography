import tkinter as tk
from tkinter import messagebox

def hitung_nilai():
    try:
        sikap = float(entry_sikap.get())
        tugas = float(entry_tugas.get())
        uts   = float(entry_uts.get())
        uas   = float(entry_uas.get())

        # Hitung total nilai
        total = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)

        # Tentukan nilai huruf & bobot
        if 81 <= total <= 100:
            nilai_huruf, bobot = "A", 4
        elif total >= 76:
            nilai_huruf, bobot = "B+", 3.5
        elif total >= 71:
            nilai_huruf, bobot = "B", 3
        elif total >= 66:
            nilai_huruf, bobot = "C+", 2.5
        elif total >= 56:
            nilai_huruf, bobot = "C", 2
        elif total >= 46:
            nilai_huruf, bobot = "D", 1
        else:
            nilai_huruf, bobot = "E", 0

        # Keterangan lulus / tidak lulus
        keterangan = "Lulus" if total >= 56 else "Tidak Lulus"

        # Tampilkan hasil di Messagebox
        messagebox.showinfo("Hasil Perhitungan", 
                            f"Total Nilai Akhir : {total:.2f}\n"
                            f"Nilai Huruf       : {nilai_huruf} (Bobot {bobot})\n"
                            f"Keterangan        : {keterangan}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid pada semua field!")

# Fungsi keluar program
def keluar():
    root.destroy()

# Buat jendela utama
root = tk.Tk()
root.title("Program Hitung Nilai Akhir Akademik")
root.geometry("400x350")

# Label dan Entry
tk.Label(root, text="Nilai Sikap/Kehadiran (0-100):").pack(pady=5)
entry_sikap = tk.Entry(root)
entry_sikap.pack()

tk.Label(root, text="Nilai Tugas (0-100):").pack(pady=5)
entry_tugas = tk.Entry(root)
entry_tugas.pack()

tk.Label(root, text="Nilai UTS (0-100):").pack(pady=5)
entry_uts = tk.Entry(root)
entry_uts.pack()

tk.Label(root, text="Nilai UAS (0-100):").pack(pady=5)
entry_uas = tk.Entry(root)
entry_uas.pack()


tk.Button(root, text="Hitung Nilai", command=hitung_nilai, bg="lightblue").pack(pady=10)


tk.Button(root, text="Exit", command=keluar, bg="blue", fg="white").pack(pady=5)


root.mainloop()
