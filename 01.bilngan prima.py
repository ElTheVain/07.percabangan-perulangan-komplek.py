def bilangan_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0:
            return False
    return True
n = int(input("Tolong masukkan bilangan: "))
for i in range(n - 1, 1, -1):  
    if bilangan_prima(i): 
        print(f"Bilangan prima terdekat yang lebih kecil dari {n} adalah {i}")
        break
