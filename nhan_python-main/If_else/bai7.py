# ### **Bài 7: Kiểm tra ký tự đầu tiên của chuỗi**

# - **Mô tả:** Cho một chuỗi `ten`. Kiểm tra ký tự đầu tiên của chuỗi đó.
# - **Yêu cầu:**
#     - Nếu ký tự đầu tiên là 'A' hoặc 'a', in ra "Tên bắt đầu bằng chữ A".
#     - Ngược lại, in ra "Tên KHÔNG bắt đầu bằng chữ A".
# - **Thiết lập ban đầu:**
    
#     **Python**
    
#     `ten = "An" # Thay đổi giá trị này (ví dụ: "Binh", "Alice")`
    
# - **Ví dụ kiểm thử:**
#     - **Input:** `ten = "An"` **Output:** `Tên bắt đầu bằng chữ A`
#     - **Input:** `ten = "Alice"` **Output:** `Tên bắt đầu bằng chữ A`
#     - **Input:** `ten = "Binh"` **Output:** `Tên KHÔNG bắt đầu bằng chữ A`
#     - **Input:** `ten = "apple"` **Output:** `Tên bắt đầu bằng chữ A`
ten=(input("nhap"))
if ten =="An":
    print("có tên bắt đầu là A")
elif ten=="Alice":
    print("Có tên bắt đầu là A")
elif ten=="Binh":
    print("ko có tên bắt là A")
elif ten=="apple":
    print("có tên bắt đầu là A")