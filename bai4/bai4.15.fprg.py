print("Sinh Vien : Trần Võ Sóng Hồng")
print("MSSV : 235752020710005")
input_string = input('Nhập các từ tiếng Anh: ')
words = input_string.split()
words.sort()
print('Các từ theo thứ tự từ điển:')
for word in words:
    print(word)
