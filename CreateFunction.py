def konversi_suhu(suhu, satuan):
    konversi = {
        "C": ((suhu * 9/5) + 32, "°F"),
        "F": ((suhu - 32) * 5/9, "°C")
    }

    return konversi[satuan]


# Input dari pengguna
suhu = float(input("Masukkan suhu: "))
satuan = input("Masukkan satuan (C/F): ").upper()


hasil, simbol = konversi_suhu(suhu, satuan)


simbol_awal = {"C": "°C", "F": "°F"}[satuan]


print(f"{suhu} {simbol_awal} = {hasil:.2f} {simbol}")



luas_lingkaran = lambda r: 3.14 * r ** 2  #2. Membuat lambda function untuk jari-jari lingkaran

# Input jari-jari
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung luas
hasil = luas_lingkaran(jari_jari)

# Menampilkan hasil
print("Luas lingkaran:", hasil)