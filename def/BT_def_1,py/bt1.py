# ### **Bài 1: Tổng của hai số**

# - **Mô tả:** Viết một hàm nhận vào hai số nguyên và trả về tổng của chúng.
# - **Signature:**
    
#     **Python**
    
#     `def tinh_tong(a: int, b: int) -> int:
#         pass`
    
# - **Ví dụ:**
    
#     **Python**
    
#     `# Test Case 1
#     # Input: a = 5, b = 3
#     # Expected Output: 8
#     print(tinh_tong(5, 3))
    
#     # Test Case 2
#     # Input: a = -10, b = 20
#     # Expected Output: 10
#     print(tinh_tong(-10, 20))`

def tinh_tong(a,b)->int:
    tinh_tong=a+b

    return tinh_tong
print(tinh_tong(5,3))