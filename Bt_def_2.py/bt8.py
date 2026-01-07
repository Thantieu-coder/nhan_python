# ### **Bài 8: Tìm số nhỏ nhất và vị trí của nó trong danh sách**

# - **Mô tả:** Viết một hàm nhận vào một danh sách các số nguyên. Hàm sẽ trả về một list chứa (số nhỏ nhất, vị trí (index) đầu tiên của số nhỏ nhất). Giả định danh sách không rỗng.
# - **Signature:**
    
#     **Python**
    
#     ```python
#     def tim_min_va_vi_tri(danh_sach: list[int]) -> list:
#         pass
#     ```
    
# - **Ví dụ:**
    
#     **Python**
    
#     ```python
#     # Test Case 1
#     # Input: danh_sach = [5, 2, 9, 1, 7]
#     # Expected Output: [1, 3]
#     print(tim_min_va_vi_tri([5, 2, 9, 1, 7]))
    
#     # Test Case 2
#     # Input: danh_sach = [-10, 0, 5, -10]
#     # Expected Output: [-10, 0]
#     print(tim_min_va_vi_tri([-10, 0, 5, -10]))
#     ```
def tim_min_va_vi_tri(danh_sach: list[int]) -> list:
    l=min(danh_sach)
    m=danh_sach.index(l)
    return (l,m)
print(tim_min_va_vi_tri([5, 2, 9, 1, 7]))