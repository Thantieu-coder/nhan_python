# **Bài 16: Đếm số lần xuất hiện của một phần tử**

# - **Mô tả bài toán:** Cho một danh sách số nguyên và một số nguyên cần tìm. Đếm xem số đó xuất hiện bao nhiêu lần trong danh sách.
# - **Input:**
#     - Danh sách số nguyên (ví dụ: `[1, 2, 2, 3, 2, 4]`)
#     - Số nguyên cần tìm (ví dụ: `2`)
# - **Output:** 
#     - Số lần xuất hiện.
# - **Ví dụ kiểm thử:**
#     - Input: `[1, 2, 2, 3, 2, 4]`, `2`
#     - Output: `3`
# - **Gợi ý:** Dùng vòng lặp `for` để duyệt từng phần tử và dùng `if` để kiểm tra.
x=[1,2,3,4,2,5,1,2,3,2,2]
a= x.count(2)
print(a)