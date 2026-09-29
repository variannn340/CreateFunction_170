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