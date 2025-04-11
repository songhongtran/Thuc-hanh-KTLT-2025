print("Sinh Vien : Trần Võ Sóng Hồng")
print("MSSV : 235752020710005")
ds = input('Nhập chuỗi: ').split()
try:
    ds.remove('123')
except ValueError:
    print("'123' không có trong danh sách.")
for ch in ds:
    print(ch)
