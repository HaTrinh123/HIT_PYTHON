 #Các cách khởi tạo chuỗi
# my_string = 'Hello'

# my_string = "Hello"

# my_string = '''Hello'''

# # Sử dụng 3 dấu nháy kép để kéo dài chuỗi thành nhiều dòng
# my_string = '''Hello, welcome to 
# the world of Python'''

# print(my_string)

# print('\a')
# s = 'ab\nc'
# print(s)

# #Chuỗi trần 
# src = r'D:\coding\tennis_analysis'
# print(src)

# #Định dạng chuỗi 
# #Giữ chỗ: {},
# # s1 = 'hệ nhị phân của {0} được biểu diễn là {0:b}'. format(12)
# # print(s1)
# # s2 = 'Biểu diễn dưới dạng mũ: {0:e}'.format(1566.345)
# # print(s2)

# # #Làm tròn số
# # s3 = 'Một phần ba: {0:.3f}'.format(1/3)
# # print(s3)

# # #Căn lề
# # s4 = '|{:<10}|{:^10}|{:>10}|'.format('list', 'tuple', 'set')
# # print(s4)

# s1 = "HIT"
# s2 = "PYTHON"
# # Nối chuỗi
# s = s1 + s2 
# print(s)

# #Nhân bản chuỗi
# s = s1 * 3
# print(s)

# s = 'HIT PYTHON'

# # for i in s:
# #     print(i, end=' ')
# # print()
# # for i in range(len(s)):
# #     print(s[i], end=' ')
# print(s[0:-3:2])
# s = input()

#Thay đổi hoặc xóa một chuỗi
# s = 'HIT PYTHON'
# #Thay đổi
# # s = '....'
# # print(s)

# #xóa chuỗi
# # del s
# # print(s)

# #Một số phương thức xử lý chuỗi
# s = s.lower()
# print(s)
# s1 = 'hit python'
# s2 = 'hit python'
# print(s == s1)
# print(id(s))
# print(id(s1))
# print(id(s2))

# s =input()
# s1 = s.split()
# num = len(s1)
# print(num)

# print(len(input().split()))

#Danh sách
# l = [1, 2, [3, 4, 5], 6]
# print(l[2][-2])

# l = [x for x in range(10)]
# print(l)

# l = [int(input()) for _ in range(10)]
# print(l)
# l = [[1, 2, 3], [4, 5, 6]]
# ll = [i for l in l for i in l]
# print(ll)

# l = [x for x in range(10) if x % 2 == 0]

# print(l)

# l = []
# for x in range(10):
#     if x % 2 == 0:
#         l.append(x)
# print(l)

# l = [1, 2, 3, 4, 5]
# print(l[0:4])

#Đảo ngược list
# l = [1, 2, 3, 4]
# l1 = l[::-1]
#Chèn, sửa, xóa phần tử trong list
# l[1:] = [10, 9, 8]
# l[:-3] = [10, 9, 8]
# l[:] = []
# print(l)

# l = [1, 2, 3, 4, 5]
# l1 = l.copy()
# print(id(l))
# print(id(l1))

n = int(input())

a =[int(input()) for _ in range(n)]
b = [int(input()) for _ in range(n)]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
print(a)

b = b * 2
b = b[::-1]
c = b + a
print(c)