# Fungsi untuk memeriksa tipe input
def valid_input(input_str):
    try:
        # Mengubah input menjadi integer
        value = int(input_str)
        return value
    except ValueError:
        # Mengembalikan None jika input tidak valid
        return None

    # Meminta input dari user
sisi1 = valid_input(input("Masukkan sisi 1: "))
sisi2 = valid_input(input("Masukkan sisi 2: "))
sisi3 = valid_input(input("Masukkan sisi 3: "))

    # Memeriksa apakah ada input yang tidak valid
if sisi1 is None or sisi2 is None or sisi3 is None:
    print("Input yang Anda masukkan tidak valid.")
else:
    # Memeriksa kesamaan sisi-sisi segitiga
    if sisi1 == sisi2 == sisi3:
        print("3 sisi sama")
    elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
        print("2 sisi sama")
    else:
        print("Tidak ada yang sama")
