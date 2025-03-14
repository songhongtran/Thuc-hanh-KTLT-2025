print("Sinh Vien : Trần Võ Sóng Hồng")
print("MSSV : 235752020710005")
import math

pos = [0, 10]

while True:
    s = input("Nhập lệnh di chuyển hoặc enter: ")
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])

    if direction == "UP":
        pos[0] -= steps
    elif direction == "DOWN":
        pos[0] += steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps

distance = round(math.sqrt(pos[0]**2 + pos[1]**2))
print("Khoảng cách từ vị trí hiện tại đến bạn đầu là:", distance)
