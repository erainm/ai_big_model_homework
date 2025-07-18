# Created by erainm on 2025/7/18 21:34.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 列表元素平均值

def list_element_avg(list_data):
    # 先判断列表是否为空，为空直接返回0
    if not list_data:
        return 0
    # 定义一个空列表，用于存储列表中的数字元素
    filtered_data = []
    # 遍历原列表
    for element in list_data:
        # 1. 判断是否为数字，是则加入到创建的新列表中
        if isinstance(element, (int, float)):
            filtered_data.append(element)
        # 2. 判断是否为字符串，并且字符串可以转为数字，则加入到创建的新列表中
        elif isinstance(element, str) and element.isdigit():
            filtered_data.append(int(element))
    # 判断新列表是否为空，为空则返回0
    if not filtered_data:
        return 0
    # 计算列表元素的平均值
    return sum(filtered_data) / len(filtered_data)

if __name__ == '__main__':
    lis1 = [1,'11',2,3,4,5,6,7,8,9,10,'a']
    print(list_element_avg(lis1))
