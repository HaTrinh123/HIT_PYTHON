n = int(input("Nhap so phan tu cua list: "))
lst = []
for i in range(n):
    lst.append(int(input()))
print("lst =",lst)

so_yeu_thich = {1, 3, 5, 7, 9}
a = []
for num in lst:
    if num % 10 in so_yeu_thich:
        a.append(num)

a.sort()
print("so luong so thay Ba thich trong cac so Nasus co la: ",len(a))
print(" cac so thay Ba thich theo thu tu tang dan ma Nasus co la: ",a)