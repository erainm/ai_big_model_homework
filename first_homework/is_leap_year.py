# Created by erainm on 2025/7/16 10:38.
# @Description: TODO: 判断输入的年份是否为闰年
"""
输入一个年份，判断该年份是否为闰年，并输出相应的提示信息
具体要求：
    · 如果输入的年份能被4整除但不能被100整除，或者能被400整除，则被认为是闰年
    · 如果输入的年份不满足以上条件，则倍认为不是闰年
"""

def is_leap_year():
    try:
        year = int(input("请输入一个年份："))
        if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year}是闰年。")
        else:
            print(f"{year}不是闰年。")
    except ValueError:
        print("输入无效，请输入一个有效的年份数字。")


if __name__ == '__main__':
    is_leap_year()