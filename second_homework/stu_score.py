# Created by erainm on 2025/7/18 22:20.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 学生成绩
# 假设你正在开发一个学生成绩管理系统，需要编写Python代码来计算学生的总成绩和平均成绩。请完成以下要求：
# 已知一个学生的成绩列表 scores = [80, 90, 85, 95, 70] ，其中每个元素表示学生的一门成绩。请使用函数嵌套调用的方式编写代码，实现以下功能：
#   · 创建一个函数 calculate_total(scores)，计算学生的总成绩，并返回结果。
#   · 创建一个函数 calculate_average(scores)，计算学生的平均成绩，并返回结果。
#   · 在 calculate_average(scores) 函数内部，通过调用 calculate_total(scores) 函数来获取学生的总成绩，并计算平均成绩。
#   · 在主程序中调用 calculate_average(scores) 函数，并输出学生的总成绩和平均成绩。
# 请编写上述要求的代码，并输出学生的总成绩和平均成绩。
def calculate_total(scores):
    total = sum(scores)
    return total

def calculate_average(scores):
    total = calculate_total(scores)
    average = total / len(scores)
    return average

if __name__ == '__main__':
    # 这里就不再判断列表中元素是否为数字，以及是否可转为数字，可参考list_element_avg.py
    scores = [80, 90, 85, 95, 70]
    total = calculate_total(scores)
    average = calculate_average(scores)
    print("Total score:", total)
    print("Average score:", average)

