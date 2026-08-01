while True:
    N = int(input("hitung fibbonanci ke: "))
    if N <= 0:
        print("masukkan angka positif real")
    else:
        break
    
a, b = 0, 1

for i in range(N):
    a, b = b, a + b

print("hasil dari fibbonanci ke", N, "adalah", a)