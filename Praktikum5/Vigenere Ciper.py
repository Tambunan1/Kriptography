import tkinter as tk
from tkinter import messagebox, scrolledtext

# === FUNGSI-FUNGSI VIGENERE CIPHER ===
def generate_key(text, key):
    key = key.upper()
    if len(key) < len(text):
        key = (key * (len(text) // len(key) + 1))[:len(text)]
    return key

def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = generate_key(plaintext, key)
    ciphertext = ""
    proses = "=== PROSES ENKRIPSI ===\n"
    for p, k in zip(plaintext, key):
        if p.isalpha():
            e = (ord(p) + ord(k) - 2 * ord('A')) % 26
            c = chr(e + ord('A'))
            ciphertext += c
            proses += f"{p} + {k} -> {c}\n"
        else:
            ciphertext += p
    proses += "========================"
    return ciphertext, proses

def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = generate_key(ciphertext, key)
    plaintext = ""
    proses = "=== PROSES DEKRIPSI ===\n"
    for c, k in zip(ciphertext, key):
        if c.isalpha():
            d = (ord(c) - ord(k) + 26) % 26
            p = chr(d + ord('A'))
            plaintext += p
            proses += f"{c} - {k} -> {p}\n"
        else:
            plaintext += c
    proses += "========================"
    return plaintext, proses


# === FUNGSI UNTUK GUI ===
def proses_enkripsi():
    key = key_entry.get()
    text = text_entry.get()
    if not key or not text:
        messagebox.showwarning("Peringatan", "Masukkan key dan teks terlebih dahulu!")
        return
    hasil, proses = encrypt(text, key)
    result_entry.delete(0, tk.END)
    result_entry.insert(0, hasil)
    process_text.delete(1.0, tk.END)
    process_text.insert(tk.END, proses)

def proses_dekripsi():
    key = key_entry.get()
    text = text_entry.get()
    if not key or not text:
        messagebox.showwarning("Peringatan", "Masukkan key dan teks terlebih dahulu!")
        return
    hasil, proses = decrypt(text, key)
    result_entry.delete(0, tk.END)
    result_entry.insert(0, hasil)
    process_text.delete(1.0, tk.END)
    process_text.insert(tk.END, proses)

def bersihkan():
    key_entry.delete(0, tk.END)
    text_entry.delete(0, tk.END)
    result_entry.delete(0, tk.END)
    process_text.delete(1.0, tk.END)


# === GUI UTAMA ===
root = tk.Tk()
root.title("Program Vigenere Cipher (GUI Tanpa OOP)")
root.geometry("600x500")
root.config(bg="#dfc5ff")

# Judul
tk.Label(root, text="Vigenère Cipher", font=("Arial", 20, "bold"), bg="#e6f0ff").pack(pady=10)

# Input key
tk.Label(root, text="Key:", bg="#e6cbff", font=("Arial", 12)).pack()
key_entry = tk.Entry(root, width=40)
key_entry.pack(pady=5)

# Input text
tk.Label(root, text="Teks:", bg="#d7c4ff", font=("Arial", 12)).pack()
text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=5)

# Tombol
btn_frame = tk.Frame(root, bg="#dfd5ff")
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Enkripsi", bg="#4CAF50", fg="white", width=12, command=proses_enkripsi).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Dekripsi", bg="#2196F3", fg="white", width=12, command=proses_dekripsi).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Bersihkan", bg="#f91313", fg="white", width=12, command=bersihkan).grid(row=0, column=2, padx=10)

# Output hasil
tk.Label(root, text="Hasil:", bg="#e6f0ff", font=("Arial", 12)).pack()
result_entry = tk.Entry(root, width=50, font=("Consolas", 11))
result_entry.pack(pady=5)

# Area proses
tk.Label(root, text="Detail Proses:", bg="#e6f0ff", font=("Arial", 12)).pack()
process_text = scrolledtext.ScrolledText(root, width=70, height=12, font=("Consolas", 10))
process_text.pack(pady=5)

# Jalankan GUI
root.mainloop()