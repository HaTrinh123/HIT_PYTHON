# Tính tổng các chữ số trong một số nguyên dương
h = int(input('Nhap vao mot so nguyen duong h = '))
sum = 0
while h > 0:
    sum += h % 10
    h //= 10
print('Tong cac chu so trong so nguyen duong do =', sum)
#Tính tổng các ước số của một số nguyên dương
n = int(input('Nhap vao mot so nguyen duong n = '))
sum = 0
for i in range(1,n + 1,1):
    if n % i == 0:
        sum += i
print('Tong cac uoc so cua n = ',sum)
#Kiểm tra tam giác:
a = int(input('Nhap so nguyen duong a = '))
b = int(input('Nhap so nguyen duong b = '))
c = int(input('Nhap so nguyen duong c = '))
if a + b > c and a + c > b and b + c > a:
    print('Day la tam giac')
    if a == b or a == c or b == c:
        print('Day la tam giac can')
    elif a == b and b == c:
        print('Day la tam giac deu')
    elif a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
        print('Day la tam giac vuong')
    elif a * a > b * b + c * c or b * b > a * a + c * c or c * c > a * a + b * b:
        print('Day la tam giac tu')
    else:
        print('Day la tam giac nhon')
else:
    print('Day khong phai la tam giac')

