print("Sinh Vien:Trần Võ Sóng Hồng")
print("MSSV:235752020710005")
a, b = 1, 2
total = 0
print(a, end=" ")
while (a <= 4000000-1):
    if a % 2 == 0:
        total += a
    a, b = b, a+b
    print(a, end=" ")
print("\n Tổng các số chẵn trong dãy Fibonacci là: ", total)
