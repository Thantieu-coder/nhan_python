# Bài 19: Đảo ngược thứ tự danh sách (không dùng slicing [::-1])

# Mô tả bài toán: Cho một danh sách các số nguyên. Đảo ngược thứ tự các phần tử trong danh sách đó mà không dùng cú pháp cắt lát (slicing) [::-1].
# Input:
# Danh sách số nguyên (ví dụ: [1, 2, 3, 4, 5])
# Output:
# Danh sách đã đảo ngược.
# Ví dụ kiểm thử:
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
# Gợi ý: Dùng vòng lặp for để duyệt từ cuối danh sách gốc và thêm vào một danh sách mới, hoặc sử dụng phương thức .reverse() nếu đã học.
x=[1,2,3,4,5]
x.reverse()
print(x)