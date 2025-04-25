print("Sinh vien : Trần Võ Sóng Hồng")
print("MSSV : 235752020710005")
class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Tạo đối tượng từ class Nam và Nu
aNam = Nam()
aNu = Nu()

print(aNam.getGender())
print(aNu.getGender())
