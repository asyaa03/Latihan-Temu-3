# Meminta input dari pengguna
bilangan = int(input("Masukkan sebuah angka: "))

# Menggunakan ternary operator apakah bilangan positif, negatif, atau nol
hasil = "Positif"\
    if bilangan > 0\
        else "Negatif"\
    if bilangan < 0\
        else "Nol"

# Menampilkan hasil
print(hasil)