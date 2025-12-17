# ### **Bài 4: Tính giai thừa**

# - **Mô tả:** Viết một hàm nhận vào một số nguyên không âm `n` và trả về giai thừa của `n`. Giai thừa của 0 là 1.
# - **Signature:**
    
#     **Python**
    
#     `def tinh_giai_thua(n: int) -> int:
#         pass`
    
# - **Ví dụ:**
    
#     **Python**
    
#     `# Test Case 1
#     # Input: n = 0
#     # Expected Output: 1
#     print(tinh_giai_thua(0))
    
#     # Test Case 2
#     # Input: n = 5
#     # Expected Output: 120
#     print(tinh_giai_thua(5)) # 1 * 2 * 3 * 4 * 5`
def tinh_giai_thua(n)-> int:
    m=1
    for i in range(1, n+1):
        if i>0: 
            m=m*i
    return m
print(tinh_giai_thua(5))