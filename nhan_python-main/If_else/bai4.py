# ### **Bài 4: Xác định loại nhiệt độ**

# - **Mô tả:** Cho nhiệt độ `temp` (số nguyên).
# - **Yêu cầu:**
#     - Nếu `temp` lớn hơn hoặc bằng 30, in ra "Rất nóng".
#     - Nếu `temp` từ 20 đến 29 (bao gồm), in ra "Ấm áp".
#     - Nếu `temp` từ 10 đến 19 (bao gồm), in ra "Mát mẻ".
#     - Ngược lại (dưới 10), in ra "Lạnh".
# - **Thiết lập ban đầu:**
    
#     **Python**
    
#     `temp = 15 # Thay đổi giá trị này`
    
# - **Ví dụ kiểm thử:**
#     - **Input:** `temp = 35` **Output:** `Rất nóng`
#     - **Input:** `temp = 25` **Output:** `Ấm áp`
#     - **Input:** `temp = 10` **Output:** `Mát mẻ`
#     - **Input:** `temp = 5` **Output:** `Lạnh`

# ---
Temp =int(input("nhapp   "))
if Temp>=30:
    print("rất nóng")
  elif  20<=Temp<=29:
    print("ấm áp")
elif 10<=Temp<=29:
    print("mát mẻ")
else:
    print("lạnh")
    