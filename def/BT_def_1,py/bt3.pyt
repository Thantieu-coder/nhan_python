# ### **Bài 3: Tìm số lớn nhất trong hai số**

# - **Mô tả:** Viết một hàm nhận vào hai số nguyên và trả về số lớn hơn.
# - **Signature:**
    
#     **Python**
    
#     `def tim_lon_nhat(x: int, y: int) -> int:
#         pass`
    
# - **Ví dụ:**
    
#     **Python**
    
#     `# Test Case 1
#     # Input: x = 10, y = 5
#     # Expected Output: 10
#     print(tim_lon_nhat(10, 5))
    
#     # Test Case 2
#     # Input: x = -3, y = -8
#     # Expected Output: -3
#     print(tim_lon_nhat(-3, -8))`
def lon_nhat(x,y)-> int:
    if x>y:
        print(x)
    else :
        print(y)
        return 
print(lon_nhat(30,20))