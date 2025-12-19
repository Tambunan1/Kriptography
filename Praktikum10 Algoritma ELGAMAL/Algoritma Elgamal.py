import tkinter as tk
from tkinter import messagebox

def mod_inverse(a, p):
    return pow(a, p - 2, p)   # Fermat Little Theorem

def encrypt_text():
    try:
        p = int(entry_p.get())
        g = int(entry_g.get())
        x = int(entry_x.get())
        k = int(entry_k.get())
        plaintext = entry_plain.get()

        if plaintext == "":
            raise ValueError("Plaintext kosong")

        y = pow(g, x, p)
        a = pow(g, k, p)

        cipher = []
        debug = "=== PROSES ENKRIPSI ELGAMAL ===\n"
        debug += f"p = {p}\n"
        debug += f"g = {g}\n"
        debug += f"x = {x}\n"
        debug += f"y = g^x mod p = {y}\n"
        debug += f"k = {k}\n"
        debug += f"a = g^k mod p = {a}\n\n"

        for ch in plaintext:
            m = ord(ch)
            if m >= p:
                raise ValueError("Gunakan p > nilai ASCII")

            b = (pow(y, k, p) * m) % p
            cipher.append((a, b))

            debug += f"Huruf '{ch}' → ASCII {m} → (a,b)=({a},{b})\n"

        # TAMPILKAN CIPHERTEXT (BISA DISALIN)
        text_cipher.config(state="normal")
        text_cipher.delete("1.0", tk.END)
        text_cipher.insert(tk.END, str(cipher))
        text_cipher.config(state="disabled")

        # TAMPILKAN DEBUG
        text_output.config(state="normal")
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, debug)
        text_output.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_text():
    try:
        p = int(entry_p.get())
        x = int(entry_x.get())

        cipher_text = text_cipher.get("1.0", tk.END).strip()
        cipher_pairs = eval(cipher_text)

        plaintext = ""
        debug = "=== PROSES DEKRIPSI ELGAMAL ===\n\n"

        for a, b in cipher_pairs:
            s = pow(a, x, p)
            s_inv = mod_inverse(s, p)
            m = (b * s_inv) % p
            plaintext += chr(m)

            debug += f"(a,b)=({a},{b})\n"
            debug += f"s = a^x mod p = {s}\n"
            debug += f"s⁻¹ = {s_inv}\n"
            debug += f"m = {m} → '{chr(m)}'\n\n"

        debug += f"PLAINTEXT HASIL: {plaintext}"

        text_output.config(state="normal")
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, debug)
        text_output.config(state="disabled")

    except Exception:
        messagebox.showerror("Error", "Ciphertext tidak valid")

root = tk.Tk()
root.title("ElGamal Encryption & Decryption (Text)")
root.geometry("800x700")
root.configure(bg="#E6CCFF")   # Lilac

label_style = {"bg": "#E6CCFF", "fg": "#4B0082", "font": ("Segoe UI", 10, "bold")}
button_style = {"bg": "#C8A2C8", "fg": "white", "font": ("Segoe UI", 10, "bold")}

tk.Label(root, text="PARAMETER ELGAMAL",
         font=("Segoe UI", 14, "bold"),
         bg="#E6CCFF", fg="#4B0082").pack(pady=10)

frame = tk.Frame(root, bg="#E6CCFF")
frame.pack()

labels = ["p (prima)", "g", "x (private key)", "k (acak)"]
entries = []

for i, text in enumerate(labels):
    tk.Label(frame, text=text, **label_style).grid(row=i, column=0, sticky="w")
    e = tk.Entry(frame, width=20)
    e.grid(row=i, column=1)
    entries.append(e)

entry_p, entry_g, entry_x, entry_k = entries

tk.Label(root, text="PLAINTEXT (HURUF)", **label_style).pack(pady=5)
entry_plain = tk.Entry(root, width=60)
entry_plain.pack()

tk.Button(root, text="ENKRIPSI", command=encrypt_text,
          **button_style).pack(pady=8)

tk.Label(root, text="CIPHERTEXT (DAPAT DISALIN)", **label_style).pack()

text_cipher = tk.Text(root, height=4, width=90)
text_cipher.pack()
text_cipher.config(state="disabled")

tk.Button(root, text="DEKRIPSI", command=decrypt_text,
          **button_style).pack(pady=8)

tk.Label(root, text="PROSES PERHITUNGAN", **label_style).pack()

text_output = tk.Text(root, height=18, width=90)
text_output.pack()
text_output.config(state="disabled")

root.mainloop()
