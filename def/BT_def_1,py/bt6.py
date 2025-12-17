# ### **Bài 6: Đảo ngược chuỗi**

# - **Mô tả:** Viết một hàm nhận vào một chuỗi và trả về chuỗi đó theo thứ tự đảo ngược.
# - **Signature:**
    
#     **Python**
    
#     `def dao_nguoc_chuoi(s: str) -> str:
#         pass`
    
# - **Ví dụ:**
    
#     **Python**
    
#     `# Test Case 1
#     # Input: s = "Python"
#     # Expected Output: "nohtyP"
#     print(dao_nguoc_chuoi("Python"))
    
#     # Test Case 2
#     # Input: s = "hello"
#     # Expected Output: "olleh"
#     print(dao_nguoc_chuoi("hello"))
    
#     # Test Case 3
#     # Input: s = ""
#     # Expected Output: ""
#     print(dao_nguoc_chuoi(""))`
def chuoi_dao_nguoc(s)-> str:
    l=s[: : -1]
    return l
print(chuoi_dao_nguoc("hello"))
