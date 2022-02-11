# tipenya default dari input adalah string
data = input("Masukkan data: ") 
print("datanya: ", data, ", tipenya: ", type(data)) 

# untuk mengambil int/float bisa dengan meng-casting
angka = int(input("Masukkan bilangan bulat: ")) 
print("datanya: ", angka, ", tipenya: ", type(angka)) 

# untuk mengambil bool bisa dengan meng-casting ke int dulu
biner = bool(int(input("Masukkan nilai boolean [1/0]: ")))
print("datanya:", biner, ", tipenya: ", type(biner)) 