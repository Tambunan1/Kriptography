import tkinter as tk
from tkinter import messagebox

# ================== PROGRAM ARITMATIKA ==================
def form_aritmatika():
    win = tk.Toplevel(root)
    win.title("Aritmatika dengan Python")
    win.geometry("400x300")
    win.configure(bg="#C8A2C8")

    tk.Label(win, text="Masukkan Angka 1:", bg="#C8A2C8").pack(pady=5)
    angka1_entry = tk.Entry(win)
    angka1_entry.pack()

    tk.Label(win, text="Masukkan Angka 2:", bg="#C8A2C8").pack(pady=5)
    angka2_entry = tk.Entry(win)
    angka2_entry.pack()

    def proses():
        try:
            a = float(angka1_entry.get())
            b = float(angka2_entry.get())
            hasil = (
                f"Penjumlahan: {a+b}\n"
                f"Pengurangan: {a-b}\n"
                f"Perkalian: {a*b}\n"
                f"Pembagian: {a/b if b!=0 else 'Error (b=0)'}"
            )
            messagebox.showinfo("Hasil Aritmatika", hasil)
        except ValueError:
            messagebox.showerror("Error", "Input harus angka!")

    tk.Button(win, text="Hitung", command=proses, bg="lightblue").pack(pady=10)

# ================== PROGRAM KALKULATOR ==================
def form_kalkulator():
    win = tk.Toplevel(root)
    win.title("Kalkulator Sederhana")
    win.geometry("400x300")
    win.configure(bg="#C8A2C8")

    tk.Label(win, text="Masukkan Angka 1:", bg="#C8A2C8").pack(pady=5)
    angka1_entry = tk.Entry(win)
    angka1_entry.pack()

    tk.Label(win, text="Masukkan Angka 2:", bg="#C8A2C8").pack(pady=5)
    angka2_entry = tk.Entry(win)
    angka2_entry.pack()

    tk.Label(win, text="Operator (+, -, *, /):", bg="#C8A2C8").pack(pady=5)
    operator_entry = tk.Entry(win)
    operator_entry.pack()

    def hitung():
        try:
            a = float(angka1_entry.get())
            b = float(angka2_entry.get())
            op = operator_entry.get()

            if op == '+':
                hasil = a + b
            elif op == '-':
                hasil = a - b
            elif op == '*':
                hasil = a * b
            elif op == '/':
                hasil = "Error (b=0)" if b == 0 else a / b
            else:
                messagebox.showwarning("Error", "Operator tidak valid!")
                return

            messagebox.showinfo("Hasil Kalkulator", f"Hasil: {hasil}")
        except ValueError:
            messagebox.showerror("Error", "Input harus angka!")

    tk.Button(win, text="Hitung", command=hitung, bg="lightblue").pack(pady=10)

# ================== PROGRAM NILAI AKADEMIK ==================
def form_nilai():
    win = tk.Toplevel(root)
    win.title("Hitung Nilai Akhir Akademik")
    win.geometry("400x350")
    win.configure(bg="#C8A2C8")

    tk.Label(win, text="Nilai Sikap/Kehadiran (0-100):", bg="#C8A2C8").pack(pady=5)
    entry_sikap = tk.Entry(win)
    entry_sikap.pack()

    tk.Label(win, text="Nilai Tugas (0-100):", bg="#C8A2C8").pack(pady=5)
    entry_tugas = tk.Entry(win)
    entry_tugas.pack()

    tk.Label(win, text="Nilai UTS (0-100):", bg="#C8A2C8").pack(pady=5)
    entry_uts = tk.Entry(win)
    entry_uts.pack()

    tk.Label(win, text="Nilai UAS (0-100):", bg="#C8A2C8").pack(pady=5)
    entry_uas = tk.Entry(win)
    entry_uas.pack()

    def hitung_nilai():
        try:
            sikap = float(entry_sikap.get())
            tugas = float(entry_tugas.get())
            uts   = float(entry_uts.get())
            uas   = float(entry_uas.get())

            total = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)

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

            keterangan = "Lulus" if total >= 56 else "Tidak Lulus"

            messagebox.showinfo("Hasil Perhitungan",
                                f"Total Nilai Akhir : {total:.2f}\n"
                                f"Nilai Huruf       : {nilai_huruf} (Bobot {bobot})\n"
                                f"Keterangan        : {keterangan}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid pada semua field!")

    tk.Button(win, text="Hitung Nilai", command=hitung_nilai, bg="lightblue").pack(pady=15)


# ================== MENU UTAMA ==================
root = tk.Tk()
root.title("Menu Utama Program")
root.geometry("400x300")
root.configure(bg="#C8A2C8")

tk.Label(root, text="=== MENU UTAMA ===", font=("Arial", 14, "bold"), bg="#C8A2C8").pack(pady=20)

tk.Button(root, text="Program Aritmatika", command=form_aritmatika, bg="lightblue").pack(pady=10)
tk.Button(root, text="Kalkulator Sederhana", command=form_kalkulator, bg="lightblue").pack(pady=10)
tk.Button(root, text="Hitung Nilai Akademik", command=form_nilai, bg="lightblue").pack(pady=10)

# Tombol Exit
tk.Button(root, text="Exit", command=root.destroy, bg="blue", fg="white").pack(pady=20)

root.mainloop()
