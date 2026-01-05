# ---

# ### **Bài 1: Tổng của hai số trong một phạm vi**

# - **Mô tả:** Viết một hàm nhận vào ba số nguyên: `a`, `b`, và `gioi_han_tong`. Hàm sẽ trả về tổng của `a` và `b` **chỉ khi** tổng đó **nhỏ hơn** `gioi_han_tong`. Nếu tổng `a` và `b` lớn hơn hoặc bằng `gioi_han_tong`, hàm sẽ trả về `0`.
# - **Signature:**
    
#     ```python
#     def tinh_tong_co_gioi_han(a: int, b: int, gioi_han_tong: int) -> int:
#         pass
#     ```
    
# - **Ví dụ:**
    
#     ```python
#     # Test Case 1
#     # Input: a = 5, b = 3, gioi_han_tong = 10
#     # Expected Output: 8 (vì 5 + 3 = 8 < 10)
#     print(tinh_tong_co_gioi_han(5, 3, 10))
    
#     # Test Case 2
#     # Input: a = 10, b = 20, gioi_han_tong = 25
#     # Expected Output: 0 (vì 10 + 20 = 30 >= 25)
#     print(tinh_tong_co_gioi_han(10, 20, 25))
#     ```
def tinh_tong_co_gioi_han(a: int, b: int, gioi_han_tong: int) -> int:
    if a+b < gioi_han_tong:
        return a+b
    else:
        return 0
print(tinh_tong_co_gioi_han(5, 3, 10))