# Đọc dữ liệu đầu vào
n = map(int, input().split())
arr = list(map(int, input().split()))
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))
# Khởi tạo biến happiness
happiness = 0

# Duyệt qua từng phần tử trong mảng
for num in arr:
    if num in set_A:
        happiness += 1
    elif num in set_B:
        happiness -= 1

# In ra tổng mức độ hạnh phúc
print(happiness)