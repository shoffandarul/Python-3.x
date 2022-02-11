# Kubus
print("=====KUBUS=====")
print("RUMUS MENGHITUNG KUBUS --> sisi * sisi * sisi")
sisi = int(input("Masukan Nilai Sisi :"))
volumeKubus = sisi * sisi * sisi
print(sisi, '*',sisi, '*',sisi)
print("Volume Kubus Adalah :",volumeKubus)

# Balok
print("\n=====BALOK=====")
print("RUMUS MENGHITUNG Balok --> p * l * t")
p = int(input("Masukan Nilai Panjang :"))
l = int(input("Masukan Nilai Lebar :"))
t = int(input("Masukan Nilai Tinggi :"))
volumeBalok = p * l * t
print(p, '*', l, '*', t)
print("Volume Balok Adalah :",volumeBalok)

# Tabung
print("\n=====Tabung=====")
print("RUMUS MENGHITUNG Tabung --> 3.14 * Jari-Jari kuadrat * t")
phi = float(3.14)
jariJari = int(input("Masukan Nilai Jari-Jari :"))
t = int(input("Masukan Nilai Tinggi :"))
volumeTabung = phi * (jariJari * jariJari) * t
print(phi, '*', (jariJari,'*',jariJari), '*', t)
print("Volume Tabung Adalah :",volumeTabung)

# Prisma
print("\n=====Prisma=====")
print("RUMUS MENGHITUNG Prisma --> Luas alas * t")
luasAlas = int(input("Masukan Nilai Luas Alas :"))
t = int(input("Masukan Nilai Tinggi :"))
volumePrisma = luasAlas * t
print(luasAlas, '*', t)
print("Volume Prisma Adalah :",volumePrisma)

# Limas
print("\n=====Limas=====")
print("RUMUS MENGHITUNG Limas --> 0.34 * Luas Alas * t")
sepertiga = float(0.34)
luasAlas = int(input("Masukan Nilai Luas Alas :"))
t = int(input("Masukan Nilai Luas Tinggi :"))
volumeLimas = sepertiga * luasAlas * t
print(sepertiga, '*', luasAlas, '*', t)
print("Volume Limas Adalah :",volumeLimas)

# Kerucut
print("\n=====Kerucut=====")
print("RUMUS MENGHITUNG Kerucut --> 0.34 * 3.14 * (Jari-jari * Jari-jari) * t")
sepertiga = float(0.34)
phi = float(3.14)
jariJari = int(input("Masukan Nilai Jari-jari :"))
t = int(input("Masukan Nilai Tinggi :"))
volumeKerucut = sepertiga * phi * (jariJari * jariJari) * t
print(sepertiga, '*', phi, '*', (jariJari, '*', jariJari))
print("Volume Kerucut Adalah :",volumeKerucut)

# Bola
print("\n=====Bola=====")
print("RUMUS MENGHITUNG Bola --> 1.3 * 3.14 * (Jari-jari * Jari-jari) * t")
patpertiga = float(1.3)
phi = float(3.14)
jariJari = int(input("Masukan Nilai Jari-jari :"))
volumeBola = patpertiga * phi * (jariJari * jariJari * jariJari)
print(patpertiga, '*', phi, '*', (jariJari,'*', jariJari))
print("Volume Bola Adalah :",volumeBola)






