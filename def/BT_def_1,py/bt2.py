# ### **Bài 2: Kiểm tra số chẵn/lẻ**

# - **Mô tả:** Viết một hàm nhận vào một số nguyên và trả về chuỗi "Chẵn" nếu số đó là số chẵn, ngược lại trả về "Lẻ".
# - **Signature:**
    
#     **Python**
    
#     `def kiem_tra_chan_le(so: int) -> str:
#         pass`
    
# - **Ví dụ:**
    
#     **Python**
    
#     `# Test Case 1
#     # Input: so = 4
#     # Expected Output: "Chẵn"
#     print(kiem_tra_chan_le(4))
    
#     # Test Case 2
#     # Input: so = 7
#     # Expected Output: "Lẻ"
#     print(kiem_tra_chan_le(7))`
def kiem_tra_chan_le(so: int)-> str:

    if so % 2 == 0:
        print("chan")
    else:
        print("le")
    return so
print(kiem_tra_chan_le(100))