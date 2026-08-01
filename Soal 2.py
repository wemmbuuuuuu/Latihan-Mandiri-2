while True:
    angka = int(input("hitung sampai angka: "))
    if angka <= 0:
        print("masukkan angka positif real")
    else:
        break
         
X = 1
Y = 0

while X <= angka:
    Y += X        
    X += 1        

print("Jumlah semua bilangan dari 1 hingga", angka, "adalah:", Y)

