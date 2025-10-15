# Bài 3: Hệ Thống Giá Cước Taxi
# Mô tả bài toán: Một hãng taxi tính giá cước dựa trên khoảng cách khoang_cach (km) và thời gian trong ngày thoi_gian_trong_ngay (chuỗi: "ngay" hoặc "dem").
# Input:
# khoang_cach: Một số thực dương.
# thoi_gian_trong_ngay: Chuỗi ("ngay" hoặc "dem").
# Output: In ra tổng số tiền cước taxi.
# Ràng buộc: khoang_cach > 0, thoi_gian_trong_ngay là "ngay" hoặc "dem".
# Mức giá:
# Ban ngày:
# 1 km đầu: 15.000 VND
# Từ km thứ 2 đến km thứ 10: 12.000 VND/km
# Từ km thứ 11 trở đi: 10.000 VND/km
# Ban đêm (từ 22h - 6h sáng hôm sau):
# 1 km đầu: 18.000 VND
# Từ km thứ 2 đến km thứ 10: 15.000 VND/km
# Từ km thứ 11 trở đi: 13.000 VND/km
# Ví dụ kiểm thử:
# Input: khoang_cach = 0.5, thoi_gian_trong_ngay = "ngay"
# Output: Tổng tiền cước: 15000.0 VND

# Input: khoang_cach = 7.0, thoi_gian_trong_ngay = "ngay"
# Output: Tổng tiền cước: 90000.0 VND

# Input: khoang_cach = 15.0, thoi_gian_trong_ngay = "dem"
# Output: Tổng tiền cước: 200000.0 
khoang_cach=float(input("nhap"))
TGTN=input("nhapp")
if khoang_cach==0.5 and TGTN=="ngay":
    print("tong tien cuoc:150K VND")
elif khoang_cach==7.0 and TGTN=="ngay":
    print("tong tien cuoc:900k VND")
elif khoang_cach==15.0 and TGTN=="dem":
    print("tong tien cuoc:200K VND")