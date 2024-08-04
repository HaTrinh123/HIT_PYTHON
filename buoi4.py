# #khai báo tuple
# t0 = tuple()

# t1 =()

# t2 = ("Hello", 1, 2, ["some text", 1, 2])
# t3 =("Hello", 1, 2, ["some text", 1, 2])
# print(f"t0={t0}\t({type(t0)}")
# print(f"t1={t1}\t({type(t1)}")
# print(f"t2={t2}\t({type(t2)}")
# print(f"t3={t3}\t({type(t3)}")
      
# print("t2[1]=",t2[1])
# print("t2[3][2]= ",t2[3][2])
# t2 = list(t2)
# t2[0] = "Hi"
# t2 = tuple(t2)
# print(t2)

# s = {1, 2, 1, 2, 3, 6, 5, 4}
# print(s)
# s.add(10)
# print(s)

# s.update([11, 12, 13])
# print(s)

# s.remove(10)
# print(s)
# print(s.pop())
# print(s)

# s.clear()
# print(s)
# s.discard(4)
# print(s)
# s1 ={1, 2, 3, 4, 5}
# print(s1)
# print(s1.issubset(s))
# print(s.issubset(s1))

# s = {'blue', 'greeen', 'red'}
# s1 = {'black', 'red', 'pink'}
# print(s|s1)
# print(s & s1)
# print(s - s1)
# print(s ^ s1)

#string = "Hoc lap trinh Python cung Hit"
#('H', "o",....)

# s = "Hoc lap trinh Python cung HIT"
#cach 1
# print(s.split())
# t = []
# for i in s:
#     if i == " ":
#         continue
#     t.append(i)
# print(tuple(t))

#cach 2
# result2 =[]
# for index in range(len(s)):
#     if s[index] == " ":
#         continue
#     result2.append(s[index])
# print("Tuple2=", tuple(result2))
# #cach3
# result3 = [char for char in s if char is not " "]
# print("Tuple3= ", (result3))

# #
# count = 0
# occurences_char_o = [count +1 for char in s if char == 'o']
# print("o occurences= ", len(occurences_char_o))
   
#dem so luong phan tu ma chu o xuat hien trong typle
# print(s.count('o'))

s = [1, 2, 3, 4, 5, 6, 7]
s = set(s)
l = list(s)
print(l[-2])


