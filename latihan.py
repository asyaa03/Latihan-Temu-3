# Contoh 3.1: Demam atau tidak
try:
    # Meminta input suhu tubuh dari user
    suhu = float(input("Masukkan suhu tubuh Kamu (dalam derajat Celcius): "))

    # Mengecek apakah user demam atau tidak
    if suhu >= 38:
        print("Kamu mengalami demam.")
    else:
        print("Kamu tidak mengalami demam.")
except ValueError:
    # Penanganan jika input bukan angka
    print("Input tidak valid. Harap masukkan angka.")




# Contoh 3.2: Positif, Negatif, atau Nol
try:
    # Meminta input bilangan dari user
    bilangan = int(input("Masukkan sebuah bilangan: "))

    # Mengecek apakah bilangan positif, negatif, atau nol
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    else:
        print("Nol")
except ValueError:
    # Penanganan jika input bukan angka
    print("Input tidak valid. Harap masukkan angka.")




# Contoh 3.3: Menentukan bilangan terbesar
try:
    # Meminta input tiga bilangan dari user
    a = float(input("Masukkan bilangan pertama: "))
    b = float(input("Masukkan bilangan kedua: "))
    c = float(input("Masukkan bilangan ketiga: "))

    # Menentukan bilangan terbesar
    if a > b and a > c:
        print(f"Bilangan terbesar adalah: {a}")
    elif b > a and b > c:
        print(f"Bilangan terbesar adalah: {b}")
    else:
        print(f"Bilangan terbesar adalah: {c}")
except ValueError:
    # Penanganan jika input bukan angka
    print("Input tidak valid. Harap masukkan angka.")