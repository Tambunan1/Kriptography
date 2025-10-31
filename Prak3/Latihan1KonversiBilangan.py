import tkinter as tk
from tkinter import ttk, messagebox

# ===============================
# Program Konversi Bilangan
# ===============================

# Warna tema lilac
BG_LILAC = "#E6E6FA"
FG_PURPLE = "#4B0082"
BTN_COLOR = "#D8BFD8"
ENTRY_BG = "#F8F8FF"

root = tk.Tk()
root.title(" Konversi Bilangan ")
root.geometry("420x400")
root.configure(bg=BG_LILAC)

# Judul
title = tk.Label(root, text=" Konversi Bilangan ", font=("Segoe UI", 16, "bold"), fg=FG_PURPLE, bg=BG_LILAC)
title.pack(pady=15)

# Frame utama
frame = tk.Frame(root, bg=BG_LILAC)
frame.pack(pady=10)

# Label dan Entry
label_input = tk.Label(frame, text="Masukkan Nilai:", font=("Segoe UI", 11), bg=BG_LILAC, fg=FG_PURPLE)
label_input.grid(row=0, column=0, padx=5, pady=5, sticky="e")

entry_value = tk.Entry(frame, font=("Segoe UI", 11), width=20, bg=ENTRY_BG)
entry_value.grid(row=0, column=1, padx=5, pady=5)

# Dropdown menu untuk memilih jenis konversi
label_jenis = tk.Label(frame, text="Jenis Bilangan:", font=("Segoe UI", 11), bg=BG_LILAC, fg=FG_PURPLE)
label_jenis.grid(row=1, column=0, padx=5, pady=5, sticky="e")

jenis_options = ["Desimal", "Biner", "Oktal", "Heksadesimal"]
combo_jenis = ttk.Combobox(frame, values=jenis_options, font=("Segoe UI", 11), width=17)
combo_jenis.current(0)
combo_jenis.grid(row=1, column=1, padx=5, pady=5)

# Hasil konversi
result_label = tk.Label(root, text="Hasil Konversi:", font=("Segoe UI", 12, "bold"), bg=BG_LILAC, fg=FG_PURPLE)
result_label.pack(pady=10)

text_result = tk.Text(root, height=6, width=42, font=("Consolas", 10), bg=ENTRY_BG, fg=FG_PURPLE, wrap="word")
text_result.pack(pady=5)

# Fungsi konversi
def konversi():
    nilai = entry_value.get()
    jenis = combo_jenis.get()

    if not nilai:
        messagebox.showwarning("Peringatan", "Masukkan nilai terlebih dahulu!")
        return

    try:
        text_result.delete("1.0", tk.END)

        if jenis == "Desimal":
            desimal = int(nilai)
        elif jenis == "Biner":
            desimal = int(nilai, 2)
        elif jenis == "Oktal":
            desimal = int(nilai, 8)
        elif jenis == "Heksadesimal":
            desimal = int(nilai, 16)
        else:
            messagebox.showerror("Error", "Jenis bilangan tidak dikenal.")
            return

        hasil = f"""
Desimal      : {desimal}
Biner        : {bin(desimal)[2:]}
Oktal        : {oct(desimal)[2:]}
Heksadesimal : {hex(desimal)[2:].upper()}
"""
        text_result.insert(tk.END, hasil.strip())

    except ValueError:
        messagebox.showerror("Error", "Nilai yang dimasukkan tidak sesuai dengan jenis bilangan.")

# Tombol konversi
btn_convert = tk.Button(root, text="Konversi", command=konversi, bg=BTN_COLOR, fg=FG_PURPLE,
                        font=("Segoe UI", 11, "bold"), width=12)
btn_convert.pack(pady=10)

# Tombol keluar
btn_exit = tk.Button(root, text="Keluar", command=root.destroy, bg="#C8A2C8", fg="white",
                     font=("Segoe UI", 11, "bold"), width=12)
btn_exit.pack(pady=5)

# Jalankan GUI
root.mainloop()
