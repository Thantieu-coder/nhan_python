# ### **Bài 12: Đếm số lần xuất hiện của phần tử trong list**

# - **Mô tả:** Viết một hàm nhận vào một danh sách và một phần tử, sau đó trả về số lần phần tử đó xuất hiện trong danh sách.
# - **Signature:**
    
#     **Python**
    
#     `def dem_so_lan_xuat_hien(danh_sach: list, phan_tu: any) -> int:
#         pass`
    
# - **Ví dụ:**
    
#     **Python**
    
#     `# Test Case 1
#     # Input: danh_sach = [1, 2, 2, 3, 2, 4], phan_tu = 2
#     # Expected Output: 3
#     print(dem_so_lan_xuat_hien([1, 2, 2, 3, 2, 4], 2))
    
#     # Test Case 2
#     # Input: danh_sach = ['a', 'b', 'a', 'c'], phan_tu = 'a'
#     # Expected Output: 2
#     print(dem_so_lan_xuat_hien(['a', 'b', 'a', 'c'], 'a'))
    
#     # Test Case 3
#     # Input: danh_sach = [1, 2, 3], phan_tu = 5
#     # Expected Output: 0
#     print(dem_so_lan_xuat_hien([1, 2, 3], 5))`
def dem_so_lan_xuat_hien(danh_sach: list, phan_tu: any) -> int:
    if  danh_sach in phan_tu:
        return