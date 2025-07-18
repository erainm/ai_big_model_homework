# Created by erainm on 2025/7/16 11:53.
# @Description: TODO 简单计算器
def calculator():
    global num1, num2
    print("欢迎使用简单计算器！")
    print("可用运算符：+（加法）、-（减法）、*（乘法）、/（除法）")
    print("输入'q' 或 'quit' 退出程序\n")

    while True:
        try:
            num1_input = input("请输入第一个数字（或输入q退出）：")
            if num1_input.lower() in ['q', 'quit']:
                print("感谢使用计算器，再见！")
                break

            try:
                num1 = float(num1_input)
            except ValueError:
                print("错误：第一个数字输入无效！\n")
                continue

            num2_input = input("请输入第二个数字（或输入q退出）：")
            if num2_input.lower() in ['q', 'quit']:
                print("感谢使用计算器，再见！")
                break

            try:
                num2 = float(num2_input)
            except ValueError:
                print("错误：第二个数字输入无效！\n")
                continue

            operator = input("请输入运算符（+ ，-，*，/）：").strip()
            if not operator:
                print("错误：运算符不能为空！\n")
                continue

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("错误，除数不能为0！")
                    continue
                result = num1 / num2
            else:
                print("无效运算符！")
                continue

            print(f"计算结果为：{num1} {operator} {num2} = {result:.4f}\n")

        except ZeroDivisionError:
            print("错误：除数不能为零！\n")
        except Exception as e:
            print(f"发生未知错误：{e}\n")

if __name__ == '__main__':
    calculator()