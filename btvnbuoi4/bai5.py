n = int(input("Nhập số lượng phần tử của mảng: "))

a = []
for i in range(n):
    xau = input(f"Nhập phần tử thứ {i + 1}: ")
    a.append(xau)

b = tuple(a)

print("Tuple b:", b)

count = 0
for x in b:
    if x.isdigit():
        count += 1

print("Số phần tử trong b có dạng số là:", count)