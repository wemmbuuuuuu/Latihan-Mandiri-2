while True:
    tinggi = int(input("tinggi segitiga siku-siku: "))

    if tinggi <= 0:
        print("masukkan angka lebih dari 0")
    else:
        break
      
i = 1

while i <= tinggi:
    print("*" * i)
    i += 1
    