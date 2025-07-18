# Created by erainm on 2025/7/16 11:37.
# @Description: TODO :输出1～10所有奇数

# 编写程序，使用while……else循环语句，从1到10的数字中，输出所有奇数，并在循环完成后输出“已完成”
num = 1
while num <= 10:
    if num % 2 != 0:
        print(num)
    num += 1
else:
    print("已完成")
