# ### **Bài 7: Kiểm tra Palindrome**

# - **Mô tả:** Viết một hàm nhận vào một chuỗi và trả về `True` nếu chuỗi đó là palindrome (đọc xuôi và đọc ngược như nhau), ngược lại trả về `False`. (Không phân biệt chữ hoa, chữ thường và bỏ qua khoảng trắng).
# - **Signature:**
    
#     **Python**
    
#     `def kiem_tra_palindrome(s: str) -> bool:
#         pass`
    
# - **Ví dụ:**
    
#     **Python**
    
#     `# Test Case 1
#     # Input: s = "madam"
#     # Expected Output: True
#     print(kiem_tra_palindrome("madam"))
    
#     # Test Case 2
#     # Input: s = "Racecar"
#     # Expected Output: True
#     print(kiem_tra_palindrome("Racecar"))
    
#     # Test Case 3
#     # Input: s = "hello"
#     # Expected Output: False
#     print(kiem_tra_palindrome("hello"))
    
#     # Test Case 4
#     # Input: s = "A man a plan a canal Panama"
#     # Expected Output: True
#     print(kiem_tra_palindrome("A man a plan a canal Panama"))`
def kiem_tra_palindrome(s) -> bool:
    l=s[: : -1]
    if s==l:
        return True
    else :
        return False
print(kiem_tra_palindrome("madam"))