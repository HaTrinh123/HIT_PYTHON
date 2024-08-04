import itertools

n = int(input("Nhập số lượng phần tử của tập hợp: "))

tap_hop = set()
for _ in range(n):
    phan_tu = int(input("Nhập phần tử: "))
    tap_hop.add(phan_tu)

tong_toi_da = int(input("Nhập tổng tối đa: "))

phan_tu = sorted(tap_hop, reverse=True)

tap_hop_con_tot_nhat = []

for r in range(len(phan_tu) + 1):
    for tap_hop_con in itertools.combinations(phan_tu, r):
        tong_tap_hop_con = sum(tap_hop_con)
        if tong_tap_hop_con <= tong_toi_da and len(tap_hop_con) > len(tap_hop_con_tot_nhat):
            tap_hop_con_tot_nhat = tap_hop_con

tap_hop_con_lon_nhat = set(tap_hop_con_tot_nhat)

print("Tập hợp con lớn nhất thỏa mãn điều kiện là:", tap_hop_con_lon_nhat)