print("Sinh Vien: Trần Võ Sóng Hồng")
print("MSSV:235752020710005")
str=input("Nhập một chuỗi:")
dict = { }
for n in str:
    keys = dict.keys()
    if n in keys:
        dict [n] += 1
    else:
        dict [n] = 1
print (dict)
