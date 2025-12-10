# **Bài 23: Tính trung bình cộng của các số trong danh sách**

# - **Mô tả bài toán:** Cho một danh sách các số nguyên hoặc số thực. Tính trung bình cộng của các số đó. (Giả sử danh sách không rỗng).
# - **Input:**
#     - Danh sách số (ví dụ: `[10, 20, 30]`)
# - **Output:**
#     - Trung bình cộng (số thực).
# - **Ví dụ kiểm thử:**
#     - Input: `[10, 20, 30]`
#     - Output: `20.0`
# - **Gợi ý:** Sử dụng hàm `sum()` để tính tổng và hàm `len()` để lấy số lượng phần tử.
x=[10,20,30]
print(sum(x)//len(x))

