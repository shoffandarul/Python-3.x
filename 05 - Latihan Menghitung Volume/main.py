print("===== Aplikasi Penghitung Volume =====\n")

phi = 3.14 

print("===== Volume Kubus =====")
print("Rumus = sisi x sisi x sisi")
# input
rusukKubus = float(input("Masukkan panjang rusuk = "))
# hitung
volumeKubus = rusukKubus * rusukKubus * rusukKubus
print("Volume Kubus = ", volumeKubus, "\n")

print("===== Volume Balok =====")
print("Rumus = panjang x lebar x tinggi")
# input
panjangBalok = float(input("Masukkan panjang balok = "))
lebarBalok = float(input("Masukkan lebar balok = "))
tinggiBalok = float(input("Masukkan tinggi balok = "))
# hitung
volumeBalok = panjangBalok * lebarBalok * tinggiBalok
print("Volume Balok = ", volumeBalok, "\n")

print("===== Volume Tabung =====")
print("Rumus = phi x jari-jari x jari-jari x tinggi")
# input
jariTabung = float(input("Masukkan jari-jari Tabung = "))
tinggiTabung = float(input("Masukkan tinggi Tabung = "))
# hitung
volumeTabung = phi * jariTabung * jariTabung * tinggiTabung
print("Volume Tabung = ", volumeTabung, "\n")

print("===== Volume Prisma =====")
print("Rumus = luas alas x tinggi")
# input
luasAlasPrisma = float(input("Masukkan luas alas Prisma = "))
tinggiPrisma = float(input("Masukkan tinggi Prisma = "))
# hitung
volumePrisma = luasAlasPrisma * tinggiPrisma
print("Volume Prisma = ", volumePrisma, "\n")

print("===== Volume Limas =====")
print("Rumus = 1/3 x phi x luas alas x tinggi")
# input
luasAlasLimas = float(input("Masukkan luas alas Limas = "))
tinggiLimas = float(input("Masukkan tinggi Limas = "))
# hitung
volumeLimas = luasAlasLimas * tinggiLimas / 3
print("Volume Limas = ", volumeLimas, "\n")

print("===== Volume Kerucut =====")
print("Rumus = 1/3 x phi x jari-jari x jari-jari x tinggi")
# input
jariKerucut = float(input("Masukkan jari-jari Kerucut = "))
tinggiKerucut = float(input("Masukkan tinggi Kerucut = "))
# hitung
volumeKerucut = phi * jariKerucut * jariKerucut * tinggiKerucut / 3
print("Volume Kerucut = ", volumeKerucut, "\n")

print("===== Volume Bola =====")
print("Rumus = 4/3 x phi x jari-jari x jari-jari x jari-jari")
# input
jariBola = float(input("Masukkan jari-jari Bola = "))
# hitung
volumeBola = 4/3 * phi * jariBola * jariBola * jariBola
print("Volume Bola = ", volumeBola, "\n")

