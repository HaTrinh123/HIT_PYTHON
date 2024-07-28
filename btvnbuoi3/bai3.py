# Nhập chuỗi s1 và s2 từ bàn phím
s1 = input("Nhap chuoi s1: ")
s2 = input("Nhap chuoi s2: ")

# In ra đảo ngược của chuỗi s1
dao_nguocs1 = s1[::-1]
print("Đảo ngược của chuỗi s1:", dao_nguocs1)

# Nhập vào 2 số nguyên a và b
a = int(input("Nhap so nguyen a (1 <= a < b <= len(s2)): "))
b = int(input("Nhap so nguyen b: "))

# In ra chuỗi s2 sau khi đảo ngược từ vị trí a đến b
dao_nguocs2 = s2[:a-1] + s2[a-1:b][::-1] + s2[b:]
print("Chuoi s2 sau khi đao nguoc tu vi tri a đen b:", dao_nguocs2)

# In ra chuỗi s3 là chuỗi s1 sau khi xóa các kí tự vị trí chẵn
s3 = s1[::2]
print("Chuoi s3 sau khi xoa cac ki tu vi tri chan:", s3)

# Trả về chuỗi s4 là đan xen các kí tự của s1 và s2
s4 = ''.join([x + y for x, y in zip(s1, s2)])
print("Chuoi s4 đan xen cac ki tu cua s1 va s2:", s4)

# Đổi chỗ 2 ký tự đầu tiên của 2 chuỗi và in ra kết quả
doi_cho_s1 = s2[:2] + s1[2:]
doi_cho_s2 = s1[:2] + s2[2:]
print("Ket qua sau khi doi cho 2 ky tu đau tien:")
print("s1 =", doi_cho_s1)
print("s2 =",doi_cho_s2)