# Assignment Operator

print(20*"=")
print("Assignment Operator")
print(20*"=" + "\n")

nilai = 10
operator = 3
# nilai = float(input("Masukkan nilai awal = "))
# operator = float(input("Masukkan nilai operator = "))

print(f"\n{nilai} + {operator} = ", end = "")
nilai += operator # nilai = nilai + operator
print(nilai)

print(f"{nilai} - {operator} = ", end = "")
nilai -= operator # nilai = nilai - operator
print(nilai)

print(f"{nilai} x {operator} = ", end = "")
nilai *= operator # nilai = nilai x operator
print(nilai)

print(f"{nilai} / {operator} = ", end = "")
nilai /= operator # nilai = nilai / operator
print(nilai)

print(f"{nilai} // {operator} = ", end = "")
nilai //= operator # nilai = nilai / operator lalu dibulatkan ke bawah
print(nilai)

print(f"{nilai} ** {operator} = ", end = "")
nilai **= operator # nilai = nilai dipangkat operator
print(nilai)

print(f"{nilai} % {operator} = ", end = "")
nilai %= operator # nilai = nilai dimodulus operator
print(nilai)

# operasi bitwise
# OR
a = True
a |= True
print(f"\nTrue or True = {a}")

a = True
a |= False
print(f"True or False = {a}")

a = False
a |= False
print(f"False or False = {a}")

# AND
a = True
a &= True
print(f"\nTrue and True = {a}")

a = True
a &= False
print(f"True and False = {a}")

a = False
a &= False
print(f"False and False = {a}")

# XOR
a = True
a ^= True
print(f"\nTrue xor True = {a}")

a = True
a ^= False
print(f"True xor False = {a}")

a = False
a ^= False
print(f"False xor False = {a}")

# geser geser
d = 0b0100
print("\nnilai d =", format(d, '04b'))
d >>= 2
print("nilai d >>= 2, menjadi =", format(d, '04b'))
d <<= 1
print("nilai d <<= 1, menjadi =", format(d, '04b'))