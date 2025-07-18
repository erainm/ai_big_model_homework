# Created by erainm on 2025/7/16 10:46.
# @Description: TODO: 判断三角形类型
"""
根据输入的三角形三条边长，判断它是等边三角形、等腰三角形还是普通三角形。并输出相应信息。
具体要求：
    · 如果三边相等，则是等边三角形
    · 如果有两边相等，则是等腰三角形
    · 否则是普通三角形
"""
def check_triangle_type():
    try:
        # 输入三条边
        a = float(input("请输入第一条边长："))
        b = float(input("请输入第二条边长："))
        c = float(input("请输入第三条边长："))
        # 先判断三条边是否能构成三角形
        if a+b>c and a+c>b and b+c >a:
            # 再判断三角形类型
            if a == b == c:
                print("这是一个等边三角形。")
            elif a == b or b == c or a == c:
                print("这是一个等腰三角形。")
            else:
                print("这是一个普通三角形。")
        else:
            print("您输入的三条边不能构成有效的三角形。")
    except ValueError:
        print("输入无效，请输入有效的数字。")

if __name__ == '__main__':
    check_triangle_type()