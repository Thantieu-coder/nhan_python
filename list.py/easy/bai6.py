# **Bài 6: Xóa Phần tử theo Vị trí**

# - **Mô tả bài toán:** Cho `numbers = [10, 20, 30, 40]`. Xóa phần tử ở chỉ số 2. In danh sách mới.
# - **Input:** `numbers`
# - **Output:** Danh sách đã xóa.
# - **Ví dụ kiểm thử:** `[10, 20, 40]`
# - **Gợi ý:** Có thể dùng `del` hoặc `pop()`.
numbers = [10, 20, 30, 40]
del numbers[2]
print(numbers)  