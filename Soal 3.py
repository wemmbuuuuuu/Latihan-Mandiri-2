total = 0
count = 0

while True:
    data = input("masukkan angka(jika sudah ketik 'Q'): ")

    if data == 'Q':
        break

    total += float(data)
    count += 1

if count > 0:
    print("Rata-rata:", total / count)