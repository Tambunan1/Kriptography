import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import math

class RSAEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA Encryption - Proses Lengkap")
        self.root.geometry("900x700")
        self.root.configure(bg="#4B0082")  # Latar belakang ungu gelap
        
        # Nilai tetap RSA
        self.p = 17
        self.q = 11
        self.e = 7
        
        self.setup_ui()
        
    def setup_ui(self):
        # Frame header
        header_frame = tk.Frame(self.root, bg="#6A0DAD")
        header_frame.pack(fill="x", padx=10, pady=10)
        
        title_label = tk.Label(
            header_frame, 
            text="ENKRIPSI RSA - PROSES LENGKAP", 
            font=("Arial", 18, "bold"),
            bg="#6A0DAD",
            fg="white"
        )
        title_label.pack(pady=10)
        
        # Frame untuk parameter tetap
        params_frame = tk.Frame(self.root, bg="#9370DB", relief=tk.RAISED, borderwidth=2)
        params_frame.pack(fill="x", padx=10, pady=(0, 10))
        
        tk.Label(
            params_frame,
            text="PARAMETER TETAP RSA",
            font=("Arial", 12, "bold"),
            bg="#9370DB",
            fg="white"
        ).pack(pady=5)
        
        params_text = tk.Text(params_frame, height=3, width=80, font=("Courier", 10))
        params_text.pack(padx=10, pady=5)
        params_text.insert("1.0", f"p = {self.p}, q = {self.q}, e = {self.e}")
        params_text.config(state="disabled", bg="#E6E6FA")
        
        # Frame input pesan
        input_frame = tk.Frame(self.root, bg="#4B0082")
        input_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(
            input_frame,
            text="MASUKKAN PESAN UNTUK DIENKRIPSI:",
            font=("Arial", 11, "bold"),
            bg="#4B0082",
            fg="white"
        ).pack(anchor="w", pady=(0, 5))
        
        self.message_entry = tk.Entry(input_frame, font=("Arial", 12), width=50)
        self.message_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.message_entry.insert(0, "HELLO")
        
        encrypt_button = tk.Button(
            input_frame,
            text="PROSES ENKRIPSI",
            command=self.process_encryption,
            font=("Arial", 11, "bold"),
            bg="#8A2BE2",
            fg="white",
            activebackground="#9932CC",
            activeforeground="white"
        )
        encrypt_button.pack(side=tk.LEFT)
        
        # Frame untuk proses perhitungan
        process_frame = tk.Frame(self.root, bg="#4B0082")
        process_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        tk.Label(
            process_frame,
            text="PROSES PERHITUNGAN LENGKAP:",
            font=("Arial", 11, "bold"),
            bg="#4B0082",
            fg="white"
        ).pack(anchor="w", pady=(0, 5))
        
        # Text area untuk menampilkan proses
        self.process_text = scrolledtext.ScrolledText(
            process_frame,
            width=100,
            height=25,
            font=("Courier", 10),
            bg="#F8F8FF",
            fg="#4B0082"
        )
        self.process_text.pack(fill="both", expand=True)
        
        # Frame hasil enkripsi
        result_frame = tk.Frame(self.root, bg="#4B0082")
        result_frame.pack(fill="x", padx=10, pady=(0, 10))
        
        tk.Label(
            result_frame,
            text="HASIL ENKRIPSI:",
            font=("Arial", 11, "bold"),
            bg="#4B0082",
            fg="white"
        ).pack(anchor="w", pady=(0, 5))
        
        self.result_text = tk.Text(result_frame, height=3, width=80, font=("Courier", 10))
        self.result_text.pack()
        self.result_text.config(state="disabled", bg="#E6E6FA")
        
    def mod_pow(self, base, exponent, modulus):
        """Menghitung (base^exponent) mod modulus secara efisien"""
        result = 1
        base = base % modulus
        
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent = exponent // 2
            base = (base * base) % modulus
            
        return result
    
    def extended_gcd(self, a, b):
        """Algoritma Extended Euclidean untuk mencari invers modulo"""
        if a == 0:
            return b, 0, 1
        
        gcd, x1, y1 = self.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        
        return gcd, x, y
    
    def mod_inverse(self, a, m):
        """Mencari invers modulo a mod m"""
        gcd, x, _ = self.extended_gcd(a, m)
        
        if gcd != 1:
            return None  # Invers tidak ada
        else:
            return x % m
    
    def process_encryption(self):
        # Ambil pesan dari input
        message = self.message_entry.get().upper()
        
        if not message:
            messagebox.showwarning("Peringatan", "Masukkan pesan terlebih dahulu!")
            return
        
        # Clear text area
        self.process_text.delete(1.0, tk.END)
        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        
        # Tambahkan header proses
        self.process_text.insert(tk.END, "="*80 + "\n")
        self.process_text.insert(tk.END, "PROSES ENKRIPSI RSA ")
        self.process_text.insert(tk.END, "="*80 + "\n\n")
        
        # Langkah 1: Hitung n = p * q
        self.process_text.insert(tk.END, "LANGKAH 1: MENGHITUNG n = p × q\n")
        self.process_text.insert(tk.END, f"  p = {self.p}\n")
        self.process_text.insert(tk.END, f"  q = {self.q}\n")
        n = self.p * self.q
        self.process_text.insert(tk.END, f"  n = {self.p} × {self.q} = {n}\n")
        self.process_text.insert(tk.END, f"  → n = {n}\n\n")
        
        # Langkah 2: Hitung φ(n) = (p-1)*(q-1)
        self.process_text.insert(tk.END, "LANGKAH 2: MENGHITUNG φ(n) = (p-1) × (q-1)\n")
        phi_n = (self.p - 1) * (self.q - 1)
        self.process_text.insert(tk.END, f"  φ(n) = ({self.p}-1) × ({self.q}-1)\n")
        self.process_text.insert(tk.END, f"  φ(n) = {self.p-1} × {self.q-1} = {phi_n}\n")
        self.process_text.insert(tk.END, f"  → φ(n) = {phi_n}\n\n")
        
        # Langkah 3: Verifikasi e
        self.process_text.insert(tk.END, "LANGKAH 3: VERIFIKASI NILAI e\n")
        self.process_text.insert(tk.END, f"  e = {self.e}\n")
        
        # Cek apakah e valid (1 < e < φ(n) dan gcd(e, φ(n)) = 1)
        if self.e <= 1 or self.e >= phi_n:
            self.process_text.insert(tk.END, f"  ❌ e tidak valid: harus 1 < e < {phi_n}\n")
            messagebox.showerror("Error", f"e tidak valid! Harus 1 < e < {phi_n}")
            return
        
        # Cek gcd(e, φ(n))
        gcd_value = math.gcd(self.e, phi_n)
        self.process_text.insert(tk.END, f"  gcd(e, φ(n)) = gcd({self.e}, {phi_n}) = {gcd_value}\n")
        
        if gcd_value != 1:
            self.process_text.insert(tk.END, f"  ❌ e tidak valid: gcd(e, φ(n)) harus 1\n")
            messagebox.showerror("Error", f"e tidak valid! gcd({self.e}, {phi_n}) = {gcd_value}, harus 1")
            return
        
        self.process_text.insert(tk.END, f"  ✓ e valid\n\n")
        
        # Langkah 4: Hitung kunci privat d (d = e^(-1) mod φ(n))
        self.process_text.insert(tk.END, "LANGKAH 4: MENGHITUNG KUNCI PRIVAT d = e^(-1) mod φ(n)\n")
        self.process_text.insert(tk.END, f"  Mencari d dimana: d × {self.e} ≡ 1 mod {phi_n}\n")
        
        d = self.mod_inverse(self.e, phi_n)
        
        if d is None:
            self.process_text.insert(tk.END, f"  ❌ Tidak dapat menghitung invers modulo untuk e = {self.e} mod {phi_n}\n")
            messagebox.showerror("Error", f"Tidak dapat menghitung invers modulo untuk e = {self.e} mod {phi_n}")
            return
        
        self.process_text.insert(tk.END, f"  d = {self.e}^(-1) mod {phi_n} = {d}\n")
        self.process_text.insert(tk.END, f"  Verifikasi: {d} × {self.e} mod {phi_n} = {(d * self.e) % phi_n}\n")
        self.process_text.insert(tk.END, f"  → Kunci privat d = {d}\n\n")
        
        # Langkah 5: Tampilkan kunci publik dan privat
        self.process_text.insert(tk.END, "LANGKAH 5: KUNCI RSA\n")
        self.process_text.insert(tk.END, f"  Kunci Publik: (e, n) = ({self.e}, {n})\n")
        self.process_text.insert(tk.END, f"  Kunci Privat: (d, n) = ({d}, {n})\n\n")
        
        # Langkah 6: Konversi pesan ke angka
        self.process_text.insert(tk.END, "LANGKAH 6: KONVERSI PESAN KE ANGKA\n")
        self.process_text.insert(tk.END, f"  Pesan: '{message}'\n")
        self.process_text.insert(tk.END, "  Konversi karakter ke kode ASCII (A=0, B=1, ..., Z=25):\n")
        
        # Konversi karakter ke angka (A=0, B=1, ..., Z=25)
        numeric_values = []
        for char in message:
            if 'A' <= char <= 'Z':
                numeric_value = ord(char) - ord('A')
                numeric_values.append(numeric_value)
                self.process_text.insert(tk.END, f"    '{char}' → {numeric_value}\n")
            else:
                # Untuk karakter non-alfabet, gunakan nilai default
                numeric_values.append(0)
                self.process_text.insert(tk.END, f"    '{char}' → 0 (karakter non-alfabet)\n")
        
        self.process_text.insert(tk.END, f"  Nilai numerik pesan: {numeric_values}\n\n")
        
        # Langkah 7: Enkripsi setiap karakter
        self.process_text.insert(tk.END, "LANGKAH 7: PROSES ENKRIPSI\n")
        self.process_text.insert(tk.END, f"  Rumus enkripsi: C = M^e mod n, dimana M adalah nilai karakter\n")
        self.process_text.insert(tk.END, f"  Dengan e = {self.e}, n = {n}\n\n")
        
        encrypted_values = []
        for i, m in enumerate(numeric_values):
            # Enkripsi: c = m^e mod n
            c = self.mod_pow(m, self.e, n)
            encrypted_values.append(c)
            
            self.process_text.insert(tk.END, f"  Karakter {i+1}: '{message[i]}' (M = {m})\n")
            self.process_text.insert(tk.END, f"    C = {m}^{self.e} mod {n}\n")
            
            # Tampilkan perhitungan step-by-step
            step_result = 1
            for exp in range(1, self.e + 1):
                step_result = (step_result * m) % n
                if exp < self.e:
                    self.process_text.insert(tk.END, f"    Langkah {exp}: ({m}^{exp} mod {n}) = {step_result}\n")
            
            self.process_text.insert(tk.END, f"    Hasil: C = {c}\n\n")
        
        # Langkah 8: Dekripsi (untuk verifikasi)
        self.process_text.insert(tk.END, "LANGKAH 8: VERIFIKASI DEKRIPSI\n")
        self.process_text.insert(tk.END, f"  Rumus dekripsi: M = C^d mod n\n")
        self.process_text.insert(tk.END, f"  Dengan d = {d}, n = {n}\n\n")
        
        decrypted_values = []
        decrypted_chars = []
        for i, c in enumerate(encrypted_values):
            # Dekripsi: m = c^d mod n
            m_decrypted = self.mod_pow(c, d, n)
            decrypted_values.append(m_decrypted)
            
            # Konversi kembali ke karakter
            if 0 <= m_decrypted <= 25:
                char_decrypted = chr(m_decrypted + ord('A'))
            else:
                char_decrypted = '?'
            
            decrypted_chars.append(char_decrypted)
            
            self.process_text.insert(tk.END, f"  Cipher {i+1}: C = {c}\n")
            self.process_text.insert(tk.END, f"    M = {c}^{d} mod {n} = {m_decrypted} → '{char_decrypted}'\n")
        
        self.process_text.insert(tk.END, "\n")
        self.process_text.insert(tk.END, "="*80 + "\n")
        self.process_text.insert(tk.END, "RINGKASAN PROSES\n")
        self.process_text.insert(tk.END, "="*80 + "\n")
        self.process_text.insert(tk.END, f"Pesan asli      : '{message}'\n")
        self.process_text.insert(tk.END, f"Nilai numerik   : {numeric_values}\n")
        self.process_text.insert(tk.END, f"Hasil enkripsi  : {encrypted_values}\n")
        self.process_text.insert(tk.END, f"Hasil dekripsi  : {decrypted_values} → '{''.join(decrypted_chars)}'\n")
        
        # Tampilkan hasil enkripsi
        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Pesan: '{message}'\n")
        self.result_text.insert(tk.END, f"Hasil Enkripsi: {encrypted_values}")
        self.result_text.config(state="disabled")
        
        # Scroll ke atas
        self.process_text.see(1.0)

def main():
    root = tk.Tk()
    app = RSAEncryptionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()