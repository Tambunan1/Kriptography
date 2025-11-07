import tkinter as tk
from tkinter import messagebox, scrolledtext

# === CLASS VigenereCipher (PBO) ===
class VigenereCipher:
    def __init__(self, key):  # ← benar: __init__
        self.key = key.upper()

    def _generate_key(self, text):
        key = self.key
        if len(key) < len(text):
            key = (key * (len(text) // len(key) + 1))[:len(text)]
        return key

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        key = self._generate_key(plaintext)
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

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        key = self._generate_key(ciphertext)
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


# === CLASS GUI ===
class VigenereApp:
    def __init__(self, root):  # ← benar: __init__
        self.root = root
        self.root.title("Program Vigenere Cipher (GUI + PBO)")
        self.root.geometry("600x500")
        self.root.config(bg="#da9aff")

        # Judul
        tk.Label(root, text="Vigenère Cipher", font=("Arial", 20, "bold"), bg="#e6f0ff").pack(pady=10)

        # Input key
        tk.Label(root, text="Key:", bg="#f5dcff", font=("Arial", 12)).pack()
        self.key_entry = tk.Entry(root, width=40)
        self.key_entry.pack(pady=5)

        # Input text
        tk.Label(root, text="Teks:", bg="#f5dcff", font=("Arial", 12)).pack()
        self.text_entry = tk.Entry(root, width=40)
        self.text_entry.pack(pady=5)

        # Tombol
        btn_frame = tk.Frame(root, bg="#da9aff")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Enkripsi", bg="#4CAF50", fg="white", width=12, command=self.encrypt).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Dekripsi", bg="#2196F3", fg="white", width=12, command=self.decrypt).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Bersihkan", bg="#ff1100", fg="white", width=12, command=self.clear).grid(row=0, column=2, padx=10)

        # Output hasil
        tk.Label(root, text="Hasil:", bg="#e6f0ff", font=("Arial", 12)).pack()
        self.result_entry = tk.Entry(root, width=50, font=("Consolas", 11))
        self.result_entry.pack(pady=5)

        # Area proses
        tk.Label(root, text="Detail Proses:", bg="#fefefe", font=("Arial", 12)).pack()
        self.process_text = scrolledtext.ScrolledText(root, width=70, height=12, font=("Consolas", 10))
        self.process_text.pack(pady=5)

    def encrypt(self):
        key = self.key_entry.get()
        text = self.text_entry.get()
        if not key or not text:
            messagebox.showwarning("Peringatan", "Masukkan key dan teks terlebih dahulu!")
            return
        cipher = VigenereCipher(key)
        hasil, proses = cipher.encrypt(text)
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, hasil)
        self.process_text.delete(1.0, tk.END)
        self.process_text.insert(tk.END, proses)

    def decrypt(self):
        key = self.key_entry.get()
        text = self.text_entry.get()
        if not key or not text:
            messagebox.showwarning("Peringatan", "Masukkan key dan teks terlebih dahulu!")
            return
        cipher = VigenereCipher(key)
        hasil, proses = cipher.decrypt(text)
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, hasil)
        self.process_text.delete(1.0, tk.END)
        self.process_text.insert(tk.END, proses)

    def clear(self):
        self.key_entry.delete(0, tk.END)
        self.text_entry.delete(0, tk.END)
        self.result_entry.delete(0, tk.END)
        self.process_text.delete(1.0, tk.END)


# === PROGRAM UTAMA ===
if __name__ == "__main__":  # ← benar: __name__ dan __main__
    root = tk.Tk()
    app = VigenereApp(root)
    root.mainloop()
