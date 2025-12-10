# Bài 18: Xóa tất cả các lần xuất hiện của một phần tử

# Mô tả bài toán: Cho một danh sách số nguyên và một số nguyên cần xóa. Xóa tất cả các lần số đó xuất hiện trong danh sách.
# Input:
# Danh sách số nguyên (ví dụ: [1, 2, 2, 3, 2, 4])
# Số nguyên cần xóa (ví dụ: 2)
# Output:
# Danh sách sau khi đã xóa các phần tử.
# Ví dụ kiểm thử:
# Input: [1, 2, 2, 3, 2, 4], 2
# Output: [1, 3, 4]
# Gợi ý: Tạo một danh sách mới và chỉ thêm vào đó những phần tử không bị xóa.
x=[1,2,2,3,2,4]
for i in x:
    x.remove(2)
print(x)