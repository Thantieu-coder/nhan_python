# ### **Bài 8: Tìm số nhỏ nhất trong danh sách**

# - **Mô tả:** Viết một hàm nhận vào một danh sách các số nguyên và trả về số nhỏ nhất trong danh sách đó. Giả định danh sách không rỗng.
# - **Signature:**
    
#     **Python**
    
#     `def tim_min_list(danh_sach: list[int]) -> int:
#         pass`
    
# - **Ví dụ:**
    
#     **Python**
    
#     `# Test Case 1
#     # Input: danh_sach = [5, 2, 9, 1, 7]
#     # Expected Output: 1
#     print(tim_min_list([5, 2, 9, 1, 7]))
    
#     # Test Case 2
#     # Input: danh_sach = [-10, 0, 5]
#     # Expected Output: -10
#     print(tim_min_list([-10, 0, 5]))`
def tim_min_list(danh_sach) -> int:
    print(min(danh_sach))
    return min(danh_sach)
print(tim_min_list([5,2,9,1,7]))
