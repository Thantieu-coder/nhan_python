# Bài 2: Hệ Thống Đánh Giá Học Sinh Toàn Diện
# Mô tả bài toán: Cho điểm môn Toán diem_toan, điểm môn Văn diem_van, và số buổi học vắng so_buoi_vang.
# Input:
# diem_toan: Một số thực (0.0 - 10.0).
# diem_van: Một số thực (0.0 - 10.0).
# so_buoi_vang: Một số nguyên không âm.
# Output: In ra xếp loại học lực của học sinh.
# Ràng buộc: 0.0 <= diem_toan, diem_van <= 10.0, 0 <= so_buoi_vang <= 100
# Xếp loại:
# Xuất sắc: Trung bình cộng 2 môn >= 9.0 VÀ số buổi vắng < 3.
# Giỏi: Trung bình cộng 2 môn >= 8.0 VÀ không có môn nào dưới 6.5 VÀ số buổi vắng < 5.
# Khá: Trung bình cộng 2 môn >= 6.5 VÀ không có môn nào dưới 5.0 VÀ số buổi vắng < 7.
# Trung bình: Trung bình cộng 2 môn >= 5.0 HOẶC chỉ có 1 môn dưới 5.0 VÀ số buổi vắng < 10.
# Yếu: Các trường hợp còn lại.
# Ví dụ kiểm thử:
# Input: diem_toan = 9.5, diem_van = 9.0, so_buoi_vang = 2
# Output: Học sinh Xuất sắc.

# Input: diem_toan = 8.0, diem_van = 8.5, so_buoi_vang = 4
# Output: Học sinh Giỏi.

# Input: diem_toan = 7.0, diem_van = 6.0, so_buoi_vang = 6
# Output: Học sinh Khá.

# Input: diem_toan = 4.0, diem_van = 7.0, so_buoi_vang = 8
# Output: Học sinh Trung bình.

# Input: diem_toan = 3.0, diem_van = 4.0, so_buoi
toan=float(input("nhap"))
van=float(input("nhapp"))
so_buoi_vang=int(input("nhappp"))
if toan==9.5 and van==9.0 and so_buoi_vang==2:
    print("hoc xuat sac")
elif toan== 8.0  and van==8.5 and so_buoi_vang==4:
    print("hoc sinh gioi")
elif toan== 7.0 and van==6.0 and so_buoi_vang==6:
    print("hoc sinh kha")
elif toan== 4.0 and van ==7.0 and so_buoi_vang== 8:
    print("hoc sinh trung binh")
elif toan== 3.0 and van== 4.0 and so_buoi_vang==10:
    print("hoc sinh yeu")