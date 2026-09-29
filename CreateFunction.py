def konversi_suhu(suhu, satuan):
    if satuan == "C":
        hasil = (suhu * 9/5) + 32
        return hasil
    elif satuan == "F":
        hasil = (suhu - 32) * 5/9
        return hasil
    else:
        return "Satuan tidak valid"