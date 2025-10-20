# ### **Bài 5: Kiểm tra số có 2 chữ số**

# - **Mô tả:** Cho một số nguyên `so`. Kiểm tra xem số đó có phải là số có hai chữ số hay không (từ 10 đến 99 hoặc từ -99 đến -10).
# - **Yêu cầu:** In ra "Đây là số có hai chữ số" nếu đúng. Ngược lại, in ra "Đây KHÔNG phải là số có hai chữ số".
# - **Thiết lập ban đầu:**
    
#     **Python**
    
#     `so = 42 # Thay đổi giá trị này`
    
# - **Ví dụ kiểm thử:**
#     - **Input:** `so = 25` **Output:** `Đây là số có hai chữ số`
#     - **Input:** `so = 7` **Output:** `Đây KHÔNG phải là số có hai chữ số`
#     - **Input:** `so = 100` **Output:** `Đây KHÔNG phải là số có hai chữ số`
#     - **Input:** `so = -55` **Output:** `Đây là số có hai chữ số`
#     - **Input:** `so = -5` **Output:** `Đây KHÔNG phải là số có hai chữ số`
so=int(input("nhap"))
if 10<=so<=99:
    print("đây là số có hai chữ số")
if -10<=so<=-99:
    print("đây là số có hai chữ số")
else :
    print("đây ko phải là số hàng chục")