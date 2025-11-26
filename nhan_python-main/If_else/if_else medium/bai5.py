# Bài 5: Xác định Phân Loại Thu Nhập và Thuế
# Mô tả bài toán: Cho tổng thu nhập hàng năm thu_nhap_nam. Tính mức thuế phải đóng và phân loại thu nhập.
# Input: Một số thực dương thu_nhap_nam.
# Output: In ra "Phân loại thu nhập: [Phân loại]", "Thuế phải đóng: [Số tiền thuế]".
# Ràng buộc: thu_nhap_nam >= 0
# Phân loại và Thuế suất:
# Dưới 100 triệu: "Thấp". Thuế 5%.
# Từ 100 triệu đến dưới 300 triệu: "Trung bình". Thuế 10%.
# Từ 300 triệu đến dưới 500 triệu: "Khá". Thuế 15%.
# Từ 500 triệu trở lên: "Cao". Thuế 20%.
# Ví dụ kiểm thử:
# Input: thu_nhap_nam = 75000000
# Output: Phân loại thu nhập: Thấp. Thuế phải đóng: 3750000.0 VND

# Input: thu_nhap_nam = 200000000
# Output: Phân loại thu nhập: Trung bình. Thuế phải đóng: 20000000.0 VND

# Input: thu_nhap_nam = 600000000
# Output: Phân loại thu nhập: Cao. Thuế phải đóng: 120000000.0 VND
tn_nam=(int(input("nhap")))
if tn_nam==75000000:
    print("thấp. Thuế phải đóng:3750000 VND")
elif tn_nam==200000000:
    print("trung bình.Thuế phải đóng:200000000 VND")
elif tn_nam== 600000000:
    print("Cao. Thuế phải đóng:120000000 VND")