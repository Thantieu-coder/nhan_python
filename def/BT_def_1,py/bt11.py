# ### **Bài 11: Kiểm tra năm nhuận**

# - **Mô tả:** Viết một hàm nhận vào một số nguyên là năm và trả về `True` nếu đó là năm nhuận, ngược lại trả về `False`.
#     - Năm nhuận là năm chia hết cho 4, trừ những năm chia hết cho 100 mà không chia hết cho 400.
# - **Signature:**
    
#     **Python**
    
#     `def kiem_tra_nam_nhuan(nam: int) -> bool:
#         pass`
    
# - **Ví dụ:**  
    
#     **Python**
    
#     `# Test Case 1
#     # Input: nam = 2024
#     # Expected Output: True
#     print(kiem_tra_nam_nhuan(2024))
    
#     # Test Case 2
#     # Input: nam = 2000
#     # Expected Output: True
#     print(kiem_tra_nam_nhuan(2000))
    
#     # Test Case 3
#     # Input: nam = 1900
#     # Expected Output: False
#     print(kiem_tra_nam_nhuan(1900))
    
#     # Test Case 4
#     # Input: nam = 2023
#     # Expected Output: False
#     print(kiem_tra_nam_nhuan(2023))`
def kiem_tra_nam_nhuan(nam) -> bool:
    return True if (nam%4==0 and nam%100!= 0) or (nam%400==0) else False
ketqua=kiem_tra_nam_nhuan(2000)
print(ketqua)