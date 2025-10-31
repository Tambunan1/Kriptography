# Program untuk mencetak teks dari kiri, kanan, dan tengah

text = input("Input Text: ")  # Input teks dari pengguna

print("Teks dari kiri:")  # Bagian pertama: Cetak dari kiri
for i in range(1, len(text) + 1):
    print(text[:i])  # Cetak substring dari awal hingga i karakter

print("\nTeks dari kanan:")  # Bagian kedua: Cetak dari kanan
for i in range(1, len(text) + 1):
    print(text[-i:])  # Cetak substring dari akhir hingga i karakter

print("\nTeks dari tengah:")  # Bagian ketiga: Cetak dari tengah
middle = len(text) // 2  # Hitung indeks tengah (pembulatan ke bawah)
for i in range(middle + 1):
    start = middle - i  # Indeks awal
    end = middle + i + 1  # Indeks akhir
    print(text[start:end])  # Cetak substring dari start hingga end
