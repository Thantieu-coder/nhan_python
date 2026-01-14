# ### **Bài 9: Tổng các phần tử trong danh sách theo điều kiện**

# - **Mô tả:** Viết một hàm nhận vào một danh sách các số nguyên và một số nguyên `nguong`. Hàm sẽ trả về tổng của tất cả các phần tử trong danh sách đó **chỉ khi** phần tử đó **lớn hơn** `nguong`.
# - **Signature:**
    
#     **Python**
    
#     ```python
#     def tinh_tong_theo_nguong(danh_sach: list[int], nguong: int) -> int:
#         pass
#     ```
    
# - **Ví dụ:**
    
#     **Python**
    
#     ```python
#     # Test Case 1
#     # Input: danh_sach = [1, 2, 3, 4, 5], nguong = 3
#     # Expected Output: 9 (4 + 5)
#     print(tinh_tong_theo_nguong([1, 2, 3, 4, 5], 3))
    
#     # Test Case 2
#     # Input: danh_sach = [10, 20, 30], nguong = 50
#     # Expected Output: 0
#     print(tinh_tong_theo_nguong([10, 20, 30], 50))
#     ```
def tinh_tong_theo_nguong(danh_sach: list[int], nguong: int) -> int:
    tong= 0
    for i in danh_sach:
        if i > nguong:
            tong=tong +i
    return tong
print(tinh_tong_theo_nguong([10, 20, 30], 50))
        