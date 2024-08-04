A = {"SV001", "SV002", "SV003", "SV004", "SV005"}  
B = {"SV003", "SV004", "SV006", "SV007", "SV008"}  

print("Sinh viên đăng ký tại bàn 1:", A)
print("Sinh viên đăng ký tại bàn 2:", B)

sinh_vien_chung = A.intersection(B)
if sinh_vien_chung:
    print("Có sinh viên đăng ký học tại cả hai bàn:", sinh_vien_chung)
else:
    print("Không có sinh viên nào đăng ký học tại cả hai bàn.")

sinh_vien_tong_hop = A.union(B)
print("Danh sách tổng hợp sinh viên đã đăng ký của cả hai bàn:", sinh_vien_tong_hop)

sinh_vien_ban_1_khong_co_ban_2 = A.difference(B)
print("Danh sách sinh viên đã đăng ký tại bàn 1 mà không đăng ký tại bàn 2:", sinh_vien_ban_1_khong_co_ban_2)