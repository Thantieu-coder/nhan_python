# **Bài 15: Tạo danh sách từ Dữ liệu người dùng nhập**

# - **Mô tả bài toán:** Nhập 3 số nguyên từ người dùng. Tạo danh sách từ 3 số đó. In danh sách.
# - **Input:** 3 số nguyên (ví dụ: `10`, `20`, `30`).
# - **Output:** Danh sách chứa các số đã nhập.
# - **Ví dụ kiểm thử:** `[10, 20, 30]`
# -  
# **Gợi ý:** Dùng `input()` và `int()` cho mỗi số, sau đó tạo danh sách.
l=[]
for i in range (3):
    x=int(input("nhap")) 
    l.append( x  )
print(l)