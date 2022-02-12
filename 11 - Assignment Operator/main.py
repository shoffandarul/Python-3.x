# Assignment Operator

print(20*"=")
print("Assignment Operator")
print(20*"=" + "\n")

nilai = float(input("Masukkan nilai awal = "))
operator = float(input("Masukkan nilai operator = "))

print(f"\n{nilai} + {operator} = ", end = "")
nilai += operator
print(nilai)

print(f"{nilai} - {operator} = ", end = "")
nilai -= operator
print(nilai)

print(f"{nilai} x {operator} = ", end = "")
nilai *= operator
print(nilai)

print(f"{nilai} / {operator} = ", end = "")
nilai /= operator
print(nilai)

print(f"{nilai} % {operator} = ", end = "")
nilai %= operator
print(nilai)

