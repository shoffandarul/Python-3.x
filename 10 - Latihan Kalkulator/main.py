# Latihan kalkulator sederhana

print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka1 = float(input("    Angka pertama = "))
operator = input("Operator [+,-,x,/]= ")
angka2 = float(input("      Angka kedua = "))

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "x" or operator == "*": 
    hasil = angka1 * angka2
elif operator == "/":
    hasil = angka1 / angka2
else:
    print("Operator salah")

print(f"Hasilnya adalah {hasil}")
print("\nAkhir program")