# Bài 22: Lọc các số dương từ danh sách

# Mô tả bài toán: Cho một danh sách các số nguyên (có thể có số âm, số dương và số 0). Tạo một danh sách mới chỉ chứa các số dương.
# Input:
# Danh sách số nguyên (ví dụ: [-1, 5, -3, 8, 0])
# Output:
# Danh sách các số dương.
# Ví dụ kiểm thử:
# Input: [-1, 5, -3, 8, 0]
# Output: [5, 8]
# Gợi ý: Dùng vòng lặp for và điều kiện if để kiểm tra từng số.
x=[-1,5,-3,8,0]
y=[]
for i in x:
  if i > 0:
    y.append(i)
  print(y)