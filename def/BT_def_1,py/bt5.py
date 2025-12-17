# ### **Bài 5: Đếm số lượng chữ cái nguyên âm**

# - **Mô tả:** Viết một hàm nhận vào một chuỗi và đếm số lượng các chữ cái nguyên âm (a, e, i, o, u, A, E, I, O, U) trong chuỗi đó.
# - **Signature:**
    
#     **Python**
    
#     `def dem_nguyen_am(chuoi: str) -> int:
#         pass`
    
# - **Ví dụ:**
    
#     **Python**
    
#     `# Test Case 1
#     # Input: chuoi = "Hello World"
#     # Expected Output: 3 (e, o, o)
#     print(dem_nguyen_am("Hello World"))
    
#     # Test Case 2
#     # Input: chuoi = "Python"
#     # Expected Output: 1 (o)
#     print(dem_nguyen_am("Python"))
    
#     # Test Case 3
#     # Input: chuoi = "Rhythm"
#     # Expected Output: 0
#     print(dem_nguyen_am("Rhythm"))`
def chuoi_nguyen_am(c)-> str:
    if c in 'euoai':
        return True
    else:
        return False
ketqua= chuoi_nguyen_am("j")
print(ketqua)
chuoi="Tin Hoc Sao Viet Nam"
dem=0
for i in chuoi:
    if chuoi_nguyen_am(i):
        dem=dem+1
    else:
        pass
print(dem)