# Bài 20: Kiểm tra danh sách có chứa phần tử trùng lặp không

# Mô tả bài toán: Cho một danh sách các số nguyên. Kiểm tra xem danh sách đó có bất kỳ phần tử nào bị trùng lặp hay không.
# Input:
# Danh sách số nguyên (ví dụ: [1, 2, 3, 2])
# Output:
# True nếu có trùng lặp, False nếu không.
# Ví dụ kiểm thử:
# Input: [1, 2, 3, 2]
# Output: True
# Input: [1, 2, 3]
# Output: False
# Gợi ý: Dùng vòng lặp lồng nhau để so sánh từng cặp phần tử, hoặc dùng một danh sách phụ để lưu các phần tử đã thấy.
x=[1,2,3,2]
y = set(x)
if len(x)>len(y):
  print("True")
else:
  print("false")