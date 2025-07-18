# Created by erainm on 2025/7/18 22:01.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: 矩形面积计算模块
# 请编写两个函数，实现以下功能：
#   1. 第一个函数名为calculate_rectangle_area，接受两个参数length和width，分别为矩形的长度和宽度。
#       · 函数内部计算并返回矩形的面积。
#   2. 第二个函数名为calculate_composite_area，接受两个参数a和b，分别为两个矩形的长度和宽度。
#       · 函数内部调用calculate_rectangle_area函数，计算两个矩形的面积之和，并返回结果。
#   3.调用函数calculate_composite_area，将矩形1的长度为3，宽度为4，矩形2的长度为5，宽度为6，作为参数传入，并输出结果。

def calculate_rectangle_area(length, width):
    return length * width

def calculate_composite_area(a_length, a_width, b_length, b_width):
    """
    计算两个矩形面积之和
    参数:
        a_length (float): 第一个矩形长度
        a_width (float): 第一个矩形宽度
        b_length (float): 第二个矩形长度
        b_width (float): 第二个矩形宽度
    返回:
        float: 两个矩形面积之和
    """
    area_a = calculate_rectangle_area(a_length, a_width)
    area_b = calculate_rectangle_area(b_length, b_width)
    return area_a + area_b

if __name__ == '__main__':
    print(calculate_composite_area(3, 4, 5, 6))