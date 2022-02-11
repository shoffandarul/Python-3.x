a = 4
b = 2

# lebih besar dari (>)
print("=== lebih besar dari (>) ===")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# lebih kecil dari (<)
print("\n=== lebih kecil dari (<) ===")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari sama dengan (>=)
print("\n=== lebih dari sama dengan (>=) ===")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# kurang dari sama dengan (<=)
print("\n=== kurang dari sama dengan (<=) ===")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan (==)
print("\nsama dengan (==)")
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

# tidak sama dengan (!=)
print("\ntidak sama dengan (!=)")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# object identity (is)
print("\nobject identity (is)")
x = 5 # assignment membuat object
y = 5
print("nilai x =", x, ", id =", hex(id(x)))
print("nilai y =", y, ", id =", hex(id(y)))
hasil = x is y
print("x is y =", hasil, "\n")

x = 5 # assignment membuat object
y = 6
print("nilai x =", x, ", id =", hex(id(x)))
print("nilai y =", y, ", id =", hex(id(y)))
hasil = x is y
print("x is y =", hasil, "\n")

# object identity (is not)
print("\nobject identity (is not)")
x = 5 # assignment membuat object
y = 5
print("nilai x =", x, ", id =", hex(id(x)))
print("nilai y =", y, ", id =", hex(id(y)))
hasil = x is not y
print("x is not y =", hasil, "\n")

x = 5 # assignment membuat object
y = 6
print("nilai x =", x, ", id =", hex(id(x)))
print("nilai y =", y, ", id =", hex(id(y)))
hasil = x is not y
print("x is not y =", hasil, "\n")