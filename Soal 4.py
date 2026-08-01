while True:
    N = int(input("masukkan angka faktorial: "))
    if N <= 0:
        print("masukkan angka positif real")
    else:
        break

faktorial = 1

for i in range(1, 1 + N):
    faktorial *= i

print(N, "faktorial adalah", faktorial) 