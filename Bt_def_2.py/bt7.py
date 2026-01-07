# ### **Bài 7: Kiểm tra Palindrome và số lượng ký tự**

# - **Mô tả:** Viết một hàm nhận vào một chuỗi. Hàm sẽ trả về `True` nếu chuỗi đó là palindrome (không phân biệt chữ hoa, chữ thường và bỏ qua khoảng trắng), **VÀ** chuỗi đó phải có độ dài **ít nhất 5 ký tự** (sau khi đã làm sạch - không tính khoảng trắng). Ngược lại trả về `False`.
# - **Signature:**
    
#     **Python**
    
#     ```python
#     def kiem_tra_palindrome_nang_cao(s: str) -> bool:
#         pass
#     ```
    
# - **Ví dụ:x`**
    
#     **Python**
    
#     ```python
#     # Test Case 1
#     # Input: s = "madam"
#     # Expected Output: True
    
#     # (Palindrome, độ dài 5)
#     print(kiem_tra_palindrome_nang_cao("madam"))
    
#     # Test Case 2
#     # Input: s = "Racecar"
#     # Expected Output: True 
#     #(Palindrome, độ dài 7)
#     print(kiem_tra_palindrome_nang_cao("Racecar"))
    
#     # Test Case 3
#     # Input: s = "hih"
#     # Expected Output: False
#     # (Palindrome, nhưng độ dài chỉ 3 < 5)
#     print(kiem_tra_palindrome_nang_cao("hih"))
    
#     # Test Case 4
#     # Input: s = "A man a plan a canal Panama"
#     # Expected Output: True 
#     #(Palindrome, độ dài sau làm sạch > 5)
#     print(kiem_tra_palindrome_nang_cao("A man a plan a canal Panama"))
#     ```
def kiem_tra_palindrome_nang_cao(s: str) -> bool:
    if s[::-1] and len(s)>= 5:
        return True
    else :
        return False
print(kiem_tra_palindrome_nang_cao("hih"))
