n = int(input("nhap so"))
kiemtra= True
for i in range(2,n//2+1):
    if n% i ==0:
        kiemtra =False
        break
    else :
        kiemtra = True

print("so nguyen to" if kiemtra else "ko phai so nguyen to " )    