def konversi_suhu(suhu, satuan): #1. Konversi suhu C ke F
    if satuan == "C":
        hasil = (suhu * 9/5) + 32
        return hasil
    elif satuan == "F":
        hasil = (suhu - 32) * 5/9
        return hasil
    else:
        return "Satuan tidak valid"

# Input dari pengguna
suhu = float(input("Masukkan suhu: "))
satuan = input("Masukkan satuan (C/F): ").upper()

hasil = konversi_suhu(suhu, satuan)

if satuan == "C":
    print(suhu, "°C =", hasil, "°F")
elif satuan == "F":
    print(suhu, "°F =", hasil, "°C")
else:
    print(hasil)



luas_lingkaran = lambda r: 3.14 * r ** 2  #2. Membuat lambda function untuk jari-jari lingkaran

# Input jari-jari
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung luas
hasil = luas_lingkaran(jari_jari)