# python ga punya do while, tapi kita bisa memodifikasi while 
# agar bertindak seperti do while

secret_word = "python"
counter = 0

while True:
    word = input("Masukkan password: ")
    counter += 1

    if word == secret_word:
        print("Benar")
        break
    if word != secret_word and counter >= 3:
        print("Gagal")
        break

# dengan kondisi while true, looping pasti akan dieksekusi minimal sekali