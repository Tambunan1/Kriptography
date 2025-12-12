# rsa_gui_purple.py
import tkinter as tk
from tkinter import scrolledtext
import random
import math

# =============================
# 1. PRIME CHECK
# =============================
def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False
    r = int(math.isqrt(n))
    for i in range(3, r+1, 2):
        if n % i == 0:
            return False
    return True

def random_prime_in_range(a, b):
    primes = [x for x in range(a, b+1) if is_prime(x)]
    return random.choice(primes)

# =============================
# 2. EXTENDED GCD + MOD INVERSE
# =============================
def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = extended_gcd(b, a % b)
    return (g, y1, x1 - (a // b)*y1)

def mod_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise ValueError("Inverse modular tidak tersedia.")
    return x % phi

# =============================
# 3. PILIH e
# =============================
def choose_e(phi):
    candidates = [x for x in range(3, phi) if math.gcd(x, phi)==1]
    return random.choice(candidates)

# =============================
# 4. RSA OPERASI
# =============================
def rsa_encrypt(m, e, n):
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    return pow(c, d, n)

def text_to_num_blocks(text, n):
    b = text.encode()
    blocks = []
    block_size = 0
    while pow(256, block_size+1) <= n-1:
        block_size += 1
    for i in range(0, len(b), block_size):
        blocks.append(b[i:i+block_size])
    return blocks, block_size

def bytes_to_int(b):
    return int.from_bytes(b, 'big')

def int_to_bytes(v, length):
    return v.to_bytes(length, 'big')

# =============================
# 5. GUI FUNCTION
# =============================
def generate_rsa():
    log_box.delete(1.0, tk.END)

    p = random_prime_in_range(50,200)
    q = random_prime_in_range(50,200)
    while q == p:
        q = random_prime_in_range(50,200)

    n = p*q
    phi = (p-1)*(q-1)
    e = choose_e(phi)
    d = mod_inverse(e, phi)

    global RSA_P, RSA_Q, RSA_N, RSA_PHI, RSA_E, RSA_D
    RSA_P, RSA_Q, RSA_N, RSA_PHI, RSA_E, RSA_D = p, q, n, phi, e, d

    log = ""
    log += "=== GENERATE RSA RANDOM (50–200) ===\n"
    log += f"p terpilih = {p}\n"
    log += f"q terpilih = {q}\n"
    log += f"n = p*q = {n}\n"
    log += f"phi(n) = {phi}\n"
    log += f"e = {e}\n"
    log += f"d = {d}\n"
    log += "====================================\n"

    log_box.insert(tk.END, log)


def do_encrypt():
    if RSA_N is None:
        log_box.insert(tk.END, "Generate kunci RSA terlebih dahulu!\n")
        return

    plaintext = entry_plain.get()
    if plaintext.strip() == "":
        log_box.insert(tk.END, "Masukkan plaintext terlebih dahulu.\n")
        return

    blocks, block_size = text_to_num_blocks(plaintext, RSA_N)

    log = "\n=== ENKRIPSI RSA ===\n"
    log += f"Plaintext: {plaintext}\n"
    log += f"Ukuran blok = {block_size} byte\n\n"

    cipher_list = []

    for idx, b in enumerate(blocks, 1):
        m = bytes_to_int(b)
        log += f"Blok {idx}: bytes {b} -> m = {m}\n"
        c = rsa_encrypt(m, RSA_E, RSA_N)
        cipher_list.append(c)
        log += f"   c = m^e mod n = {m}^{RSA_E} mod {RSA_N} = {c}\n\n"

    global LAST_CIPHER
    LAST_CIPHER = cipher_list

    log_box.insert(tk.END, log)
    log_box.insert(tk.END, f"Ciphertext final (list angka):\n{cipher_list}\n")


def do_decrypt():
    if RSA_N is None or LAST_CIPHER is None:
        log_box.insert(tk.END, "Belum ada ciphertext untuk didekripsi.\n")
        return

    plaintext = entry_plain.get()
    blocks, block_size = text_to_num_blocks(plaintext, RSA_N)

    log = "\n=== DEKRIPSI RSA ===\n"
    recovered = b""

    for idx, c in enumerate(LAST_CIPHER, 1):
        log += f"Blok {idx}: c = {c}\n"
        m = rsa_decrypt(c, RSA_D, RSA_N)
        log += f"   m = c^d mod n = {c}^{RSA_D} mod {RSA_N} = {m}\n"
        blk = int_to_bytes(m, len(blocks[idx-1]))
        log += f"   bytes -> {blk}\n\n"
        recovered += blk

    try:
        text = recovered.decode()
    except:
        text = "(tidak dapat decode)"

    log_box.insert(tk.END, log)
    log_box.insert(tk.END, f"Hasil dekripsi: {text}\n")

# =============================
# 6. GUI TKINTER (PURPLE THEME)
# =============================
root = tk.Tk()
root.title("RSA GUI – Purple Theme")
root.geometry("950x620")
root.configure(bg="#2b2142")  # UNGU GELAP, PREMIUM

label_title = tk.Label(root, text="RSA Encryption & Decryption ",
                       font=("Courier New", 18, "bold"),
                       fg="#d8b7ff", bg="#2b2142")
label_title.pack(pady=10)

frame_top = tk.Frame(root, bg="#2b2142")
frame_top.pack()

tk.Label(frame_top, text="Plaintext:",
         font=("Courier New", 12),
         fg="#e6d4ff", bg="#2b2142").grid(row=0, column=0, padx=5)

entry_plain = tk.Entry(frame_top, width=50,
                       font=("Courier New", 12),
                       bg="#3c2a57", fg="#f2e9ff",
                       insertbackground="white")
entry_plain.grid(row=0, column=1, padx=5)

btn_generate = tk.Button(frame_top, text="Generate RSA Key",
                         font=("Courier New", 12),
                         bg="#543a75", fg="#ffffff",
                         command=generate_rsa)
btn_generate.grid(row=1, column=0, pady=10)

btn_encrypt = tk.Button(frame_top, text="Encrypt",
                        font=("Courier New", 12),
                        bg="#543a75", fg="#ffffff",
                        command=do_encrypt)
btn_encrypt.grid(row=1, column=1, sticky="w", pady=10)

btn_decrypt = tk.Button(frame_top, text="Decrypt",
                        font=("Courier New", 12),
                        bg="#543a75", fg="#ffffff",
                        command=do_decrypt)
btn_decrypt.grid(row=1, column=1, sticky="e", pady=10)

# LOG AREA
log_box = scrolledtext.ScrolledText(
    root, width=115, height=25,
    font=("Consolas", 11),
    bg="#1e1830",  # UNGU GELAP
    fg="#e9ddff",
    insertbackground="white"
)
log_box.pack(pady=10)

# VARIABEL GLOBAL
RSA_P = RSA_Q = RSA_N = RSA_PHI = RSA_E = RSA_D = None
LAST_CIPHER = None

root.mainloop()
