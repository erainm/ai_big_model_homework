# Created by erainm on 2025/7/16 11:42.
# @Description: TODO 判断输入的数是否为质数

def check_prime_num():
    try:
        num = int(input("请输入一个大于1的整数："))
        if num <= 1:
            print(f"{num}不是质数")
            return

        for i in range(2, int(num**0.5) +1):
            if num % 2 == 0:
                print(f"{num} 不是质数")
                return
        print(f'{num} 是质数')
    except ValueError:
        print("请输入有效数字。")


if __name__ == '__main__':
    check_prime_num()