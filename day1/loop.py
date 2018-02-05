"""
Created on 2018/2/5
@Author: Jeff Yang
"""

# count = 0
# while True:
#     print("count: ", count)
#     count = count + 1  # count += 1
#     if count == 1000:
#         break  # 跳出循环

# for i in range(0, 10, 2):  # 2为步长
#     print("loop", i)

# for i in range(10):
#     if i < 3:
#         print("loop ", i)
#     else:
#         continue  # 跳出本次循环，执行下一次循环
#     print("=======")

for i in range(10):
    print("------", i)
    for j in range(10):
        print(j)
        if j >= 5:
            break  # 跳出j的这个循环，整个循环执行60次
