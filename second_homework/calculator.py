# Created by erainm on 2025/7/19 00:18.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 加减乘除计算器
class Calculator(object):
    def __init__(self):
        self.result = 0
        self.num1 = None
        self.num2 = None

    def add(self):
        self.result = self.num1 + self.num2
        return self.result

    def subtract(self):
        self.result = self.num1 - self.num2
        return self.result

    def multiply(self):
        self.result = self.num1 * self.num2
        return self.result

    def divide(self):
        if self.num2 == 0:
            raise ValueError("除数不能为0")
        self.result = self.num1 / self.num2
        return self.result

if __name__ == '__main__':
    calculator = Calculator()
    calculator.num1 = 12
    calculator.num2 = 13
    calculator.add()
    print("加法计算结果为：", calculator.add())
    print("减法计算结果为：", calculator.subtract())
    print("乘法计算结果为：", calculator.multiply())
    print("除法计算结果为：", calculator.divide())