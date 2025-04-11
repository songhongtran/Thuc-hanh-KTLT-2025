print("Sinh Vien : Trần Võ Sóng Hồng")
print("MSSV : 235752020710005")
ds = input('Nhập chuỗi: ').split()
try:
    position = ds.index('abc')
    print("Vị trí của chuỗi 'abc' là:", position)
except ValueError:
    print("'abc' không có trong danh sách.")
