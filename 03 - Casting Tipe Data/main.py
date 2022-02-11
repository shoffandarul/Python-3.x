"""
    Casting : mengubah data dari satu tipe ke tipe lain
"""

data_int = 9
print("data : ", data_int, " tipenya : ", type(data_int))

# casting 
data_float = float(data_int)
data_string = str(data_int)
data_bool = bool(data_int)
print("data : ", data_float, " tipenya : ", type(data_float))
print("data : ", data_string, " tipenya : ", type(data_string))
print("data : ", data_bool, " tipenya : ", type(data_bool))

# dari int    ke bool akan bernilai true, kecuali nilainya 0
# dari float  ke integer akan dibulatkan ke bawah
# data string (huruf) tidak bisa diubah ke integer, tapi kalau angka bisa
# data string ke bool akan selalu bernilai true, kecuali jika stringnya kosong