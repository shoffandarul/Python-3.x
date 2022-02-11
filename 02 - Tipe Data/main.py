# Angka satuan / integer
data_integer = 1
print("data : ", data_integer, ", bertipe :", type(data_integer))

# Angka dengan koma / float
data_float = 7.5
print("data : ", data_float, ", bertipe :", type(data_float))

# Kumpulan karakter / string
data_string = "Goodbye World"
print("data : ", data_string, ", bertipe :", type(data_string))

# biner true or false / boolean
data_bool = True
print("data : ", data_bool, ", bertipe :", type(data_bool))

# Tipe data khusus

# Bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex, ", bertipe :", type(data_complex))

# Tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double, ", bertipe :", type(data_c_double))