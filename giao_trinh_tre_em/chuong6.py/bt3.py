n= int(input("nhap so"))
import math
s= math.sqrt(n)
for i in range(1, n):
    if s*s==n :
        print("la so chinh phuong")
    else:
        print("ko phai so chinh phuong")
    break