n= 12
s=0
for i in range(1 , n):
    if n % i==0:
        s=s+i
if s==n:
    print("so hoan hao")
else:
    print("ko phai so hoan hao")