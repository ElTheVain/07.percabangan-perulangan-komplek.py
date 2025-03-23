def segitiga(n):
    for i in range(n, 0, -1):
        faktorial = 1
        for j in range(1, i + 1):
            faktorial *= j
        baris = [str(faktorial)] + [str(k) for k in range(i, 0, -1)]
        print(" ".join(baris))

n = int(input("Tolong masukkan nilai n: "))
segitiga(n)
