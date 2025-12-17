# ### **Bài 9: Tổng các phần tử trong danh sách**

# - **Mô tả:** Viết một hàm nhận vào một danh sách các số nguyên và trả về tổng của tất cả các phần tử trong danh sách đó.
# - **Signature:**
    
#     **Python**
    
#     `def tinh_tong_list(danh_sach: list[int]) -> int:
#         pass`
    
# - **Ví dụ:**
    
#     **Python**
    
#     `# Test Case 1
#     # Input: danh_sach = [1, 2, 3, 4, 5]
#     # Expected Output: 15
#     print(tinh_tong_list([1, 2, 3, 4, 5]))
    
#     # Test Case 2
#     # Input: danh_sach = []
#     # Expected Output: 0
#     print(tinh_tong_list([]))
    
#     # Test Case 3
#     # Input: danh_sach = [-1, 0, 1]
#     # Expected Output: 0
#     print(tinh_tong_list([-1, 0, 1]))`
def tinh_tong_list(danh_sach)-> int:
    print(sum(danh_sach))
    return sum(danh_sach)
print(tinh_tong_list([3,6,8,10]))