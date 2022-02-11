status = "y"
print("\n===== Selamat datang di program penghitung volume =====\n")

while status == "y" or status == "Y":

    bangunRuang = input("1. Kubus\n2. Balok\n3. Tabung\n4. Prisma\n5. Limas\n6. Kerucut\n7. Bola\n \nPilih Bangun Ruang yang akan dihitung (angka): ")
    phi = float(3.14)
    
    if bangunRuang == "1":
        print("\n===== Menghitung Volume Kubus =====\n")
        print("Volume Kubus : sisi x sisi x sisi")
        sisiKubus = float(input("Masukkan panjang sisi : "))
        volumeKubus = float(sisiKubus * sisiKubus * sisiKubus)
        print("Volume Kubus :", volumeKubus)

    elif bangunRuang == "2":
        print("\n===== Menghitung Volume Balok ===== \n")
        print("Volume Balok : panjang x lebar x tinggi")
        panjangBalok = float(input("Masukkan panjang balok : "))
        lebarBalok = float(input("Masukkan lebar balok : "))
        tinggiBalok = float(input("Masukkan tinggi balok : "))
        volumeBalok = float(panjangBalok * lebarBalok * tinggiBalok)
        print("Volume Balok :", volumeBalok)

    elif bangunRuang == "3":
        print("\n===== Menghitung Volume Tabung ===== \n")
        print("Volume Tabung : phi x jari-jari x jari-jari x tinggi")
        jariTabung = float(input("Masukkan jari-jari tabung : "))
        tinggiTabung = float(input("Masukkan tinggi tabung : "))
        volumeTabung = float(phi * jariTabung * jariTabung * tinggiTabung)
        print("Volume Tabung :", volumeTabung)

    elif bangunRuang == "4":
        print("\n===== Menghitung Volume Prisma ===== \n")
        print("Volume Prisma : luas alas x tinggi")
        alasPrisma = float(input("Masukkan luas alas prisma : "))
        tinggiPrisma = float(input("Masukkan tinggi prisma : "))
        volumePrisma = float(alasPrisma * tinggiPrisma)
        print("Volume Prisma :", volumePrisma)

    elif bangunRuang == "5":
        print("\n===== Menghitung Volume Limas ===== \n")
        print("Volume Limas : 1/3 x luas alas x tinggi")
        alasLimas = float(input("Masukkan luas alas limas : "))
        tinggiLimas = float(input("Masukkan tinggi limas : "))
        volumeLimas = float(alasLimas * tinggiLimas / 3)
        print("Volume Limas :", volumeLimas)

    elif bangunRuang == "6":
        print("\n===== Menghitung Volume Kerucut ===== \n")
        print("Volume Kerucut : 1/3 x phi x jari-jari x jari-jari x tinggi")
        jariKerucut = float(input("Masukkan jari-jari kerucut : "))
        tinggiKerucut = float(input("Masukkan tinggi kerucut : "))
        volumeKerucut = float(phi * jariKerucut * jariKerucut * tinggiKerucut / 3)
        print("Volume Kerucut :", volumeKerucut)

    elif bangunRuang == "7":
        print("\n===== Menghitung Volume Bola ===== \n")
        print("Volume Bola : 4/3 x phi x jari-jari x jari-jari x jari-jari")
        jariBola = float(input("Masukkan jari-jari bola : "))
        volumeBola = float(4 / 3 * phi * jariBola * jariBola * jariBola)
        print("Volume Bola :", volumeBola)

    else:
        print("\nAngka yang diinput salah (pilih 1-7)")

    status = input("\nCoba lagi [y/n] ? ")

else:
    print("\nTerima kasih sudah menggunakan program ini\n")