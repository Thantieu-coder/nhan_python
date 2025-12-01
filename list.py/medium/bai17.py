# **Bài 17: Tạo danh sách số chẵn/lẻ từ danh sách khác**

# - **Mô tả bài toán:** Cho một danh sách các số nguyên. Tạo ra hai danh sách mới: một danh sách chỉ chứa các số chẵn, và một danh sách chỉ chứa các số lẻ.
# - **Input:**
#     - Danh sách số nguyên (ví dụ: `[1, 2, 3, 4, 5, 6]`)
# - **Output:**
#     - Hai danh sách riêng biệt (danh sách số chẵn, danh sách số lẻ).
# - **Ví dụ kiểm thử:**
#     - Input: `[1, 2, 3, 4, 5, 6]`
#     - Output: `Chẵn: [2, 4, 6]`, `Lẻ: [1, 3, 5]`
# - **Gợi ý:** Dùng vòng lặp `for` để duyệt, toán tử `%` để kiểm tra chẵn/lẻ, và phương thức `append()` để thêm vào danh sách mới.
x=[1,2,3,4,5,6]
chan=[]
le=[]
for i in range(len(x)):
    if x[i]%2==0:
        chan.append(x[i])
    else:
        le.append(x[i])
print(chan,le)