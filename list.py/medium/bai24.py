# **Bài 24: Tìm vị trí (chỉ số) của một phần tử**

# - **Mô tả bài toán:** Cho một danh sách các số nguyên và một số nguyên cần tìm. Tìm chỉ số của lần xuất hiện **Thứ 2** của số đó trong danh sách. Nếu số đó không có trong danh sách, in ra thông báo "Không tìm thấy".
# - **Input:**
#     - Danh sách số nguyên (ví dụ: `[10, 20, 30, 20]`)
#     - Số nguyên cần tìm (ví dụ: `20`)
# - **Output:**
#     - 3
# - **Ví dụ kiểm thử:**
#     - Input: `[10, 20, 30, 20]`, `20`
#     - Output: 3
#     - Input: `[10, 20, 30]`, `40`
#     - Output: `Không tìm thấy`
# - **Gợi ý:** Duyệt danh sách bằng chỉ số (`range(len())`), dùng `if` để kiểm tra.
# x=[10,20,30,20]
# dem=0
# for i in range(len(x)):
#     if dem == x:
#         dem+1

#     if dem==2:

        