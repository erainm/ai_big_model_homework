# Created by erainm on 2025/7/18 23:28.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 列表操作
"""
定义一个列表my_list，包含至少五个元素，例如[1, 2, 3, 4, 5]。
将列表my_list中的元素进行相加，并将结果输出。
将列表my_list中的元素重复两次，并将结果输出。
判断数字3是否在列表my_list中，并输出判断结果。
使用max()函数找出列表中的最大值，并输出。
使用min()函数找出列表中的最小值，并输出。
"""

class ListOperate(object):
    def __init__(self, my_list):
        self.my_list = my_list
    # 将列表my_list中的元素进行相加，并将结果输出。
    def sum_list(self):
        return sum(self.my_list)
    # 将列表my_list中的元素重复两次，并将结果输出。
    def repeat_list(self):
        return self.my_list * 2
    # 判断数字3是否在列表my_list中，并输出判断结果。
    def check_number(self):
        return 3 in self.my_list
    # 使用max()函数找出列表中的最大值，并输出。
    def find_max(self):
        return max(self.my_list)
    # 使用min()函数找出列表中的最小值，并输出。
    def find_min(self):
        return min(self.my_list)

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    list_operate = ListOperate(my_list)
    print("列表元素相加：",list_operate.sum_list())
    print("列表元素重复两次：",list_operate.repeat_list())
    print("判断3是否在列表：",list_operate.check_number())
    print("找出列表最大值：",list_operate.find_max())
    print("找出列表最小值：",list_operate.find_min())