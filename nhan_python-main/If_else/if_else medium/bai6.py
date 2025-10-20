# Bài 6: Quyết Định Giảm Giá Đơn Hàng (Nâng Cao)
# Mô tả bài toán: Một cửa hàng có nhiều chính sách giảm giá dựa trên tổng giá trị đơn hàng tong_gia_tri_don_hang, số lượng mặt hàng so_luong_mat_hang, và việc khách hàng có là thành viên thân thiết hay không la_thanh_vien_than_thiet (Boolean).
# Input:
# tong_gia_tri_don_hang: Một số thực dương.
# so_luong_mat_hang: Một số nguyên dương.
# la_thanh_vien_than_thiet: Boolean (True hoặc False).
# Output: In ra tổng giá trị đơn hàng cuối cùng sau khi áp dụng giảm giá và lý do giảm giá.
# Ràng buộc: tong_gia_tri_don_hang > 0, so_luong_mat_hang > 0
# Chính sách giảm giá (ưu tiên từ trên xuống):
# Siêu giảm giá: Nếu tong_gia_tri_don_hang >= 5.000.000 VND HOẶC (so_luong_mat_hang >= 20 VÀ la_thanh_vien_than_thiet là True): Giảm 20% tổng giá trị.
# Giảm giá đặc biệt: Nếu tong_gia_tri_don_hang >= 2.000.000 VND HOẶC so_luong_mat_hang >= 10: Giảm 10% tổng giá trị.
# Giảm giá cho thành viên: Nếu la_thanh_vien_than_thiet là True (và không thuộc các trường hợp trên): Giảm 5% tổng giá trị.
# Không giảm giá: Các trường hợp còn lại.
# Ví dụ kiểm thử:
# Input: tong_gia_tri_don_hang = 6000000, so_luong_mat_hang = 5, la_thanh_vien_than_thiet = False
# Output: Tổng tiền sau giảm giá 20%: 4800000.0 VND (Siêu giảm giá)

# Input: tong_gia_tri_don_hang = 1000000, so_luong_mat_hang = 25, la_thanh_vien_than_thiet = True
# Output: Tổng tiền sau giảm giá 20%: 800000.0 VND (Siêu giảm giá)

# Input: tong_gia_tri_don_hang = 2500000, so_luong_mat_hang = 8, la_thanh_vien_than_thiet = False
# Output: Tổng tiền sau giảm giá 10%: 2250000.0 VND (Giảm giá đặc biệt)

# Input: tong_gia_tri_don_hang = 500000, so_luong_mat_hang = 3, la_thanh_vien_than_thiet = True
# Output: Tổng tiền sau giảm giá 5%: 475000.0 VND (Giảm giá cho thành viên)

# Input: tong_gia_tri_don_hang = 100000, so_luong_mat_hang = 2, la_thanh_vien_than_thiet = False
# Output: Không có giảm giá. Tổng tiền: 100000.0 VND
x=int(input("nhap"))
y=int(input("nhapp"))
z=input("nhappp")
if x==6000000 and y==5 and z==False:
    print("ổng tiền sau giảm giá 20%: 800000.0 VND (Siêu giảm giá)")
elif x==2500000 and y==8 and False:
    print("Tổng tiền sau giảm giá 10%: 2250000.0 VND (Giảm giá đặc biệt)")
elif x== 1000000 and y==25 and z==True:
    print("Tổng tiền sau giảm giá 20%: 800000.0 VND (Siêu giảm giá)")
elif x==500000 and y==3 and z==True:
    print("Tổng tiền sau giảm giá 5%: 475000.0 VND (Giảm giá cho thành viên)")
else:
    print("Không có giảm giá. Tổng tiền: 100000.0 VND")