# ### **Bài 10: Liệt kê số nguyên tố trong phạm vi**

# - **Mô tả:** Viết một hàm nhận vào hai số nguyên `bat_dau` và `ket_thuc`, và trả về một danh sách (list) chứa tất cả các số nguyên tố trong khoảng từ `bat_dau` đến `ket_thuc` (bao gồm cả `bat_dau` và `ket_thuc`).
#     - Gợi ý: Bạn có thể cần một hàm phụ để kiểm tra một số có phải là nguyên tố không.
# - **Signature:**
    
#     **Python**
    
#     `def liet_ke_snt(bat_dau: int, ket_thuc: int) -> list[int]:
#         pass`
    
# - **Ví dụ:**
    
#     **Python**
    
#     `# Test Case 1
#     # Input: bat_dau = 2, ket_thuc = 10
#     # Expected Output: [2, 3, 5, 7]
#     print(liet_ke_snt(2, 10))
    
#     # Test Case 2
#     # Input: bat_dau = 11, ket_thuc = 19
#     # Expected Output: [11, 13, 17, 19]
#     print(liet_ke_snt(11, 19))
    
#     # Test Case 3
#     # Input: bat_dau = 20, ket_thuc = 22
#     # Expected Output: []
#     print(liet_ke_snt(20, 22))`
def liet_ke_snt(bat_dau,ket_thuc) -> list[int]:
    for i in range(bat_dau,ket_thuc):
        if  2 == 0:
print(liet_ke_snt) 