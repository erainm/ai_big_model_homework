# Created by erainm on 2025/7/16 10:30.
# @Description: TODO 判断整数的正负
"""
请输入一个整数，判断该整数是否为正数、负数、还是0，并输出相应的提示信息。
具体要求：
    · 如果输入的整数大于0，输出：“该数是整数”
    · 如果输入的整数小于0，输出：“该数是负数”
    · 如果输入的整数等于0，输出：“该数是零”
"""

def judge_integer():
    # 请输入一个整数，判断
    try:
        num = int(input("请输入一个整数："))
        if num > 0:
            print("该数是正数")
        elif num < 0:
            print("该数是负数")
        else:
            print("该数是零")
    except ValueError:
        print("输入无效，请输入一个整数。")

if __name__ == '__main__':
    judge_integer()